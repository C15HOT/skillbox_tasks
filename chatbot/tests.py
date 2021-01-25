from copy import deepcopy
from unittest import TestCase
from unittest.mock import patch, Mock, ANY
from bot import Bot
import settings
from vk_api.bot_longpoll import VkBotMessageEvent


class Test1(TestCase):
    RAW_EVENT = {'type': 'message_new', 'object': {'message': {'date': 1608217802,
                                                               'from_id': 79363018, 'id': 63, 'out': 0,
                                                               'peer_id': 79363018,
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
        obj = {'a': 1}
        events = [obj] * count
        long_poller_mock = Mock(return_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock

        with patch('bot.vk_api.VkApi'):
            with patch('bot.VkBotLongPoll', return_value=long_poller_listen_mock):
                bot = Bot('', '')
                bot.on_event = Mock()
                bot.run()

                bot.on_event.assert_called()
                bot.on_event.assert_any_call(obj)
                assert bot.on_event.call_count == count

    INPUTS = [
        'Привет',
        'А когда?',
        'Где будет конференция?',
        'Зарегистрируй меня',
        'Вениамин',
        'Мой адрес email@email',
        'email@email.ru'
    ]

    EXPECTED_OUTPUTS = [
        settings.DEFAULT_ANSWER,
        settings.INTENTS[0]['answer'],
        settings.INTENTS[1]['answer'],
        settings.SCENARIOS['registration']['steps']['step1']['text'],
        settings.SCENARIOS['registration']['steps']['step2']['text'],
        settings.SCENARIOS['registration']['steps']['step2']['failure_text'],
        settings.SCENARIOS['registration']['steps']['step3']['text'].format(name='Вениамин', email='email@email.ru'),

    ]

    def test_run_ok(self):
        send_mock = Mock()
        api_mock = Mock()
        api_mock.messages.send = send_mock

        events = []
        for input_text in self.INPUTS:
            event = deepcopy(self.RAW_EVENT)
            event['object']['message']['text'] = input_text
            events.append(VkBotMessageEvent(event))
        long_poller_mock = Mock()
        long_poller_mock.listen = Mock(return_value=events)

        with patch('bot.VkBotLongPoll', return_value=long_poller_mock):
            bot = Bot('', '')
            bot.api = api_mock
            bot.run()
        assert send_mock.call_count == len(self.INPUTS)

        real_outputs = []
        for call in send_mock.call_args_list:
            args, kwargs = call
            real_outputs.append(kwargs['message'])
        for real, expec in zip(real_outputs, self.EXPECTED_OUTPUTS):
            print(real)
            print('-' * 50)
            print(expec)
            print('-' * 50)
            print(real == expec)
            print('_' * 50)
        assert real_outputs == self.EXPECTED_OUTPUTS
