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
        'привет',
        '/help',
        '/ticket',
        'москва',
        'орел',
        'лондон',
        '28-02-2021',  # TODO эту дату надо формировать не вручную
        # TODO лучше задавать дату через datetime, относительно текущей
        '174',
        '-',
        'да',
        '89990002211'
    ]

    EXPECTED_OUTPUTS = [
        settings.DEFAULT_ANSWER,
        settings.INTENTS[0]['answer'],
        settings.SCENARIOS['registration']['steps']['step1']['text'],
        settings.SCENARIOS['registration']['steps']['step2']['text'],
        settings.SCENARIOS['registration']['steps']['step2']['failure_text'],
        settings.SCENARIOS['registration']['steps']['step3']['text'],
        # TODO и подгружать в ответы надо рейсы не вручную - а из json файла
        # TODO + подумайте - что можно сделать с длинными строками, так их оставлять нельзя
        settings.SCENARIOS['registration']['steps']['step4']['text'].format(races= [('174', '28-02-2021', 5), ('175', '01-03-2021', 5)]),
        settings.SCENARIOS['registration']['steps']['step5']['text'],
        settings.SCENARIOS['registration']['steps']['step6']['text'].format(source='Москва', destination='Лондон', selected_race=('174', '28-02-2021',5), comment='-'),
        settings.SCENARIOS['registration']['steps']['step7']['text'],
        settings.SCENARIOS['registration']['steps']['step8']['text'].format(phone='89990002211'),


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
