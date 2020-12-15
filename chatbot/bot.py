from random import randint
from _token import token
import vk_api.bot_longpoll

group_id = 201143207


class Bot:
    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = vk_api.bot_longpoll.VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception as err:
                print(err)

    def on_event(self, event):
        if event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:
            self.api.messages.send(
                message='Отправляю такое же сообщение ' + event.object.message['text'],
                random_id=randint(0, 2 ** 20),
                peer_id=event.object.message['peer_id']
            )
        else:
            print('не обработано событие', event.type)


if __name__ == '__main__':
    bot = Bot(group_id=group_id, token=token)
    bot.run()
