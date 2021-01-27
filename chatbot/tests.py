from copy import deepcopy
import datetime
from unittest import TestCase
from unittest.mock import patch, Mock
from bot import Bot
import settings
from vk_api.bot_longpoll import VkBotMessageEvent
from data_generator import Generator
import json

# Если что-то надо выполнить в начале тестов -- используйте метод setUp внутри класса с тестами
#  он будет вызываться перед вызовом методов
allraces = []
date = Generator()
date.append_races()
date.writer(file_name='date.json')

with open('date.json', 'r') as read_file:
    loaded_json_file = json.load(read_file)
    for race in loaded_json_file['Москва']['Лондон']:
        allraces.append(race)
    text_date = loaded_json_file['Москва']['Лондон'][allraces[0]][0]


def loader():
    dates = []
    allraces = []
    races = []
    user_date = datetime.datetime.strptime(text_date, '%d-%m-%Y')
    for day in range(5):
        last_date = user_date + datetime.timedelta(days=day)
        date = last_date.strftime("%d-%m-%Y")
        dates.append(date)
    with open('date.json', 'r') as read_file:
        loaded_json_file = json.load(read_file)

        for race in loaded_json_file['Москва']['Лондон']:
            allraces.append(race)
        for number in allraces:
            race = loaded_json_file['Москва']['Лондон'][number]
            for day in dates:
                if race[0] == day:
                    races.append((number, race[0], race[1]))
        return races


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

    races = loader()

    INPUTS = [
        'привет',
        '/help',
        '/ticket',
        'москва',
        'орел',
        'лондон',
        text_date,
        allraces[0],
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
        # и подгружать в ответы надо рейсы не вручную - а из json файла
        #  + подумайте - что можно сделать с длинными строками, так их оставлять нельзя
        settings.SCENARIOS['registration']['steps']['step4']['text'].format(races=races),
        settings.SCENARIOS['registration']['steps']['step5']['text'],
        #  длинную строку надо сделать поменьше
        #  возможно собрать данные в словаре и в формат передавать **словарь
        #  как это делается в самом боте при формировании строки
        settings.SCENARIOS['registration']['steps']['step6']['text'].format(source='Москва',
                                                                            destination='Лондон',
                                                                            selected_race=races[0], comment='-'),
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
