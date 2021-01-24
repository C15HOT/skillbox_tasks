from random import randint
import json
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import logging
import time
import handlers
import data_generator

try:
    import settings
except ImportError:
    exit('Do cp settings.py.defoault settings.py and set token')

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


class UserState:
    def __init__(self, scenario_name, step_name, context=None):
        self.scenario_name = scenario_name
        self.step_name = step_name
        self.context = context or {}


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
        self.user_states = dict()  # user_id -> user_state

    def run(self):
        """
        run bot

        """
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception:
                log.exception('ошибка в обработке события')

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
        if user_id in self.user_states:

            text_to_send = self.continue_scenario(user_id, text=text)
        else:
            # search intent
            for intent in settings.INTENTS:
                log.debug(f'User gets {intent}')
                if any(token in text.lower() for token in intent['tokens']):
                    # run intent
                    if intent['answer']:
                        text_to_send = intent['answer']
                    else:
                        text_to_send = self.start_scenario(user_id, intent['scenario'])
                    break
            else:
                text_to_send = settings.DEFAULT_ANSWER

        self.api.messages.send(
            message=text_to_send,
            random_id=randint(0, 2 ** 20),
            peer_id=user_id
        )

    def start_scenario(self, user_id, scenario_name):
        scenario = settings.SCENARIOS[scenario_name]
        first_step = scenario['first_step']
        step = scenario['steps'][first_step]
        text_to_send = step['text']
        self.user_states[user_id] = UserState(scenario_name=scenario_name, step_name=first_step)

        return text_to_send

    def continue_scenario(self, user_id, text):
        state = self.user_states[user_id]
        steps = settings.SCENARIOS[state.scenario_name]['steps']
        step = steps[state.step_name]

        handler = getattr(handlers, step['handler'])
        if handler(text=text, context=state.context):


            # next step
            next_step = steps[step['next_step']]  #  вот этот переход будет
            #  и в next_step['text'] вместо "Введите номер рейса",
            #  должно быть "Доступные рейсы: {races}. Введите номер рейса "
            text_to_send = next_step['text'].format(**state.context)
            # и тогда в этой строке мы подставим вместо races информацию из state.context['races']
            if next_step['next_step']:
                # switch to next step
                state.step_name = step['next_step']
            else:
                # finish
                log.info('Зарегистрирован {phone}'.format(**state.context))
                self.user_states.pop(user_id)

        else:
            # retry current step
            text_to_send = step['failure_text'].format(**state.context)

        return text_to_send


if __name__ == '__main__':
    configure_logging()
    bot = Bot(group_id=settings.GROUP_ID, token=settings.TOKEN)
    bot.run()
