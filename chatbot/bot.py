from random import randint

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import logging
import time

try:
    import settings
except ImportError:
    exit('Do cp settings.py.defoault settings.py and set token')


log = logging.getLogger('bot')

def configure_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(' %(levelname)s %(message)s'))

    file_handler = logging.FileHandler('bot.log',  'w', 'utf-8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s',
                                                datefmt=time.strftime("%d-%m-%Y %H:%M")))

    log.addHandler(stream_handler)
    log.addHandler(file_handler)

    log.setLevel(logging.DEBUG)
    stream_handler.setLevel(logging.INFO)
    file_handler.setLevel(logging.DEBUG)



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
        if event.type == VkBotEventType.MESSAGE_NEW:
            log.debug('отправляем сообщения назад')
            self.api.messages.send(
                message=event.object.message['text'],
                random_id=randint(0, 2 ** 20),
                peer_id=event.object.message['peer_id']
            )
        else:
            log.info('не обработано событие %s', event.type)


if __name__ == '__main__':
    configure_logging()
    bot = Bot(group_id=settings.GROUP_ID, token=settings.TOKEN)
    bot.run()
