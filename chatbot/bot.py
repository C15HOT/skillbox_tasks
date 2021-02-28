from random import randint

import requests
import vk_api
from pony.orm import db_session
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import logging
import time
import handlers

from chatbot.models import UserState, Registration

try:
    import settings
except ImportError:
    exit('Do cp settings.py.default settings.py and set token')

log = logging.getLogger('bot')


def configure_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(' %(levelname)s %(message)s'))

    file_handler = logging.FileHandler('bot.log', 'w', 'utf-8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s',
                                                datefmt=time.strftime("%d-%m-%Y %H:%M")))

    log.addHandler(stream_handler)
    log.addHandler(file_handler)

    log.setLevel(logging.DEBUG)
    stream_handler.setLevel(logging.INFO)
    file_handler.setLevel(logging.DEBUG)


# class UserState:
#     def __init__(self, scenario_name, step_name, context=None):
#         self.scenario_name = scenario_name
#         self.step_name = step_name
#         self.context = context or {}


class Bot:
    """
    Echo bot for vk.com
    use python 3.7
    """

    def __init__(self, group_id, token):
        """

        :param group_id: group id from vk group
        :param token:secret token
        """
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()
        # self.user_states = dict()  # user_id -> user_state

    def run(self):
        """
        run bot

        """
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception:
                log.exception('ошибка в обработке события')

    @db_session
    def on_event(self, event):
        """
        send text message
        :param event VkBotMessageEvent object
        """
        if event.type != VkBotEventType.MESSAGE_NEW:
            log.debug('отправляем сообщения назад')
            return

        user_id = event.object.message['peer_id']
        text = event.object.message['text']

        state = UserState.get(user_id=str(user_id))

        if state is not None:
            if text == '/ticket':
                state.delete()

                self.start_scenario(user_id, settings.INTENTS[1]['scenario'], text='Начинаем заказ билетов')
            else:
                self.continue_scenario(text=text, state=state, user_id=user_id)
        else:
            # search intent
            for intent in settings.INTENTS:
                log.debug(f'User gets {intent}')
                if any(token in text.lower() for token in intent['tokens']):
                    # run intent
                    if intent['answer']:

                        self.send_text(intent['answer'], user_id)
                    else:
                        self.start_scenario(user_id, intent['scenario'], text)
                    break
            else:

                self.send_text(settings.DEFAULT_ANSWER, user_id)



    def start_scenario(self, user_id, scenario_name, text):
        scenario = settings.SCENARIOS[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        self.send_step(step, user_id, text, context={})

        UserState(user_id=str(user_id), scenario_name=scenario_name, step_name=first_step, context={})



    def continue_scenario(self, text, state, user_id):

        steps = settings.SCENARIOS[state.scenario_name]['steps']
        step = steps[state.step_name]

        handler = getattr(handlers, step['handler'])
        if handler(text=text, context=state.context, step=state):

            # next step
            next_step = steps[step['next_step']]  # вот этот переход будет
            #  и в next_step['text'] вместо "Введите номер рейса",
            #  должно быть "Доступные рейсы: {races}. Введите номер рейса "
            self.send_step(next_step, user_id, text, state.context)
            # и тогда в этой строке мы подставим вместо races информацию из state.context['races']
            if next_step['next_step']:
                # switch to next step
                state.step_name = step['next_step']
            else:
                # finish
                log.info('Зарегистрирован {phone}'.format(**state.context))
                Registration(source=state.context['source'],
                             destination=state.context['destination'],
                             date=state.context['selected_race'][1],
                             race=state.context['selected_race'][0],
                             phone=state.context['phone'],
                             comment=state.context['comment'])
                state.delete()

        else:
            # retry current step
            text_to_send = step['failure_text'].format(**state.context)
            self.send_text(text_to_send, user_id)


    def send_text(self, text_to_send, user_id):
        self.api.messages.send(
            message=text_to_send,
            random_id=randint(0, 2 ** 20),
            peer_id=user_id
            )

    def send_image(self, image, user_id):
        upload_url = self.api.photos.getMessagesUploadServer()['upload_url']
        upload_data = requests.post(url=upload_url, files={'photo': ('image.png', image, 'image/png') }).json()
        image_data = self.api.photos.saveMessagesPhoto(**upload_data)
        owner_id = image_data[0]['owner_id']
        media_id = image_data[0]['id']
        attachment = f'photo{owner_id}_{media_id}'
        self.api.messages.send(
            attachment=attachment,
            random_id=randint(0, 2 ** 20),
            peer_id=user_id
        )




    def send_step(self, step, user_id, text, context):
        if 'text' in step:
            self.send_text(step['text'].format(**context), user_id)
        if 'image' in step:
            handler = getattr(handlers, step['image'])
            image = handler(text, context, step)
            self.send_image(image, user_id)

if __name__ == '__main__':
    configure_logging()
    bot = Bot(group_id=settings.GROUP_ID, token=settings.TOKEN)
    bot.run()
