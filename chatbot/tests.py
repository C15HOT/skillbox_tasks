
from unittest import TestCase
from unittest.mock import patch, Mock, ANY
from bot import Bot
from vk_api.bot_longpoll import VkBotMessageEvent

class Test1(TestCase):
    RAW_EVENT= {'type': 'message_new', 'object': {'message': {'date': 1608217802,
                                                         'from_id': 79363018, 'id': 63, 'out': 0, 'peer_id': 79363018,
                                                         'text': 'sdfds', 'conversation_message_id': 62,
                                                         'fwd_messages': [], 'important': False, 'random_id': 0,
                                                         'attachments': [], 'is_hidden': False},
                                             'client_info': {'button_actions': ['text', 'vkpay', 'open_app',
                                                                                'location', 'open_link',
                                                                                'intent_subscribe',
                                                                                'intent_unsubscribe'],
                                                             'keyboard': True, 'inline_keyboard': True,
                                                             'carousel': False, 'lang_id': 0}},
           'group_id': 201143207, 'event_id': '434f2834af92089e8e7f2e9e0e7fa97c2a236f84'}

    def test_ok(self):

        count = 5
        obj = {'a' : 1}
        events = [obj] * count
        long_poller_mock = Mock(return_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock

        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll', return_value=long_poller_listen_mock):
                bot = Bot('','')
                bot.on_event = Mock()
                bot.run()

                bot.on_event.assert_called()
                bot.on_event.assert_any_call(obj)
                assert bot.on_event.call_count == count

    def test_event(self):
        event = VkBotMessageEvent(raw=self.RAW_EVENT)

        send_mock = Mock()

        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll'):
                bot = Bot('', '')
                bot.api = Mock()
                bot.api.messages.send = send_mock

                bot.on_event(event)
        send_mock.assert_called_once_with(
                message=self.RAW_EVENT['object']['message']['text'],
                random_id=ANY,
                peer_id=self.RAW_EVENT['object']['message']['peer_id']
        )