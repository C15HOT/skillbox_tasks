import re

import requests
from bs4 import BeautifulSoup


class WeatherMaker:
    R = re.compile("[а-яА-Я]+")

    # стиль кода
    def __init__(self):
        # self.DAYS = days
        self.response = None
        self.dates = {}
        self.temperature = []
        self.states = []
        self.allstates = []
        self.moments = ['Ночь', 'Утро', 'День', 'Вечер']

        self.data = {}
        self.coop = {}

        self.headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 '
                          'Safari/537.36 OPR/40.0.2308.81',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'DNT': '1',
            'Accept-Encoding': 'gzip, deflate, lzma, sdch',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'
        }

    def parse(self, days):

        self.response = requests.get('https://www.gismeteo.ru/weather-odintsovo-11938/3-days/', headers=self.headers)

        if self.response.status_code == 200:
            html_doc = BeautifulSoup(self.response.text, features='html.parser')
            list_of_values = html_doc.find_all('span', {'class': 'unit unit_temperature_c'})
            list_of_dates = html_doc.find_all('div', {'class': 'header_item js_head_item frame_4 showed clearfix'})
            list_of_states = html_doc.find_all('span', {'class': 'tooltip'})

            for temp in list_of_states:
                text = re.findall(self.R, str(temp))
                self.allstates.append(text)

            for day in range(days):
                for temp in range(day * 4, day * 4 + 4):
                    self.temperature.append(list_of_values[temp].text)
                for state in range(day * 4, day * 4 + 4):
                    self.states.append(self.allstates[state])

                for moment in range(4):
                    self.coop[self.moments[moment]] = [self.states[moment], self.temperature[moment]]
                    self.data[list_of_dates[day].text] = self.coop
                self.coop = {}

                self.states = []
                self.temperature = []

        return self.data


if __name__ == '__main__':
    parser = WeatherMaker()
    print(parser.parse(days=3))
