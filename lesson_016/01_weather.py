# -*- coding: utf-8 -*-

# В очередной спешке, проверив приложение с прогнозом погоды, вы выбежали
# навстречу ревью вашего кода, которое ожидало вас в офисе.
# И тут же день стал хуже - вместо обещанной облачности вас встретил ливень.

# Вы промокли, настроение было испорчено, и на ревью вы уже пришли не в духе.
# В итоге такого сокрушительного дня вы решили написать свою программу для прогноза погоды
# из источника, которому вы доверяете.

# Для этого вам нужно:

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}

# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю, должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.

# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database
import argparse
import datetime

import requests
from bs4 import BeautifulSoup
import re
import cv2

from playhouse.db_url import connect

import models

r = re.compile("[а-яА-Я]+")

re_date = re.compile(r'\d\d')


class WeatherMaker:


    def __init__(self, days):
        self.DAYS = days
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

    def parse(self):

        self.response = requests.get('https://www.gismeteo.ru/weather-odintsovo-11938/3-days/', headers=self.headers)

        if self.response.status_code == 200:
            html_doc = BeautifulSoup(self.response.text, features='html.parser')
            list_of_values = html_doc.find_all('span', {'class': 'unit unit_temperature_c'})
            list_of_dates = html_doc.find_all('div', {'class': 'header_item js_head_item frame_4 showed clearfix'})
            list_of_states = html_doc.find_all('span', {'class': 'tooltip'})

            for temp in list_of_states:
                text = re.findall(r, str(temp))
                self.allstates.append(text)

            for day in range(self.DAYS):
                for temp in range(day * 4, day * 4 + 4):
                    self.temperature.append(list_of_values[temp].text)
                for state in range(day * 4, day * 4 + 4):
                    self.states.append(self.allstates[state])

                # for moment in range(4):
                #     self.data[list_of_dates[day].text] = {self.moments[moment]: [self.states[moment], self.temperature[moment]]}
                for moment in range(4):
                    self.coop[self.moments[moment]] = [self.states[moment], self.temperature[moment]]
                    self.data[list_of_dates[day].text] = self.coop
                self.coop = {}

                # self.dates[list_of_dates[day].text] = self.temperature, self.states
                self.states = []
                self.temperature = []
        # print(self.dates)
        # print(self.data)


class ImageMaker:
    PATTERN = 'python_snippets/external_data/probe.jpg'
    LINKS = {
        'Пасмурно': 'python_snippets/external_data/weather_img/cloud.jpg',
        'Ясно': 'python_snippets/external_data/weather_img/sun.jpg',
        'снег': 'python_snippets/external_data/weather_img/snow.jpg',
        'Облачно': 'python_snippets/external_data/weather_img/cloud.jpg',
        'Мокрый снег': 'python_snippets/external_data/weather_img/snow.jpg',
        'Дождь с грозой': 'python_snippets/external_data/weather_img/rain.jpg',
        'Малооблачно': 'python_snippets/external_data/weather_img/cloud.jpg',
        'Небольшой снег': 'python_snippets/external_data/weather_img/snow.jpg',
        'дождь': 'python_snippets/external_data/weather_img/rain.jpg',
        'осадки': 'python_snippets/external_data/weather_img/rain.jpg'
    }

    def viewImage(self, image, name_of_window):
        cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
        cv2.imshow(name_of_window, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def put_data(self, data):

        y = 50

        img_x = 900
        for day, values in data.items():
            image = cv2.imread(self.PATTERN)
            image = self.gradient(image=image, state=data[day]['День'][0][0])

            cv2.putText(image, self.day_handler(day).strftime("%Y-%m-%d"), (50, y), cv2.FONT_HERSHEY_COMPLEX, 1,
                        (0, 0, 0), 2)
            for states, items in values.items():
                y += 100

                temp = items[1].replace('−', '-')
                # text = (f"{states}: {','.join(items[0])}, Температура: {items[1]}")
                text = (f"{states}: {items[0][0]}, Температура: {temp}")

                if len(items[0]) > 1:

                    if items[0][1] == 'небольшой' or items[0][1] == 'мокрый' or items[0][1] == 'небольшие' \
                            or items[0][1] == 'сильный':
                        if items[0][2] == 'мокрый':
                            state = items[0][3]
                        else:
                            state = items[0][2]


                    else:
                        state = items[0][1]

                else:
                    state = items[0][0]

                image = self.put_image(background=image, state=state, x=img_x, y=y)

                # print(text)
                cv2.putText(image, text, (50, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            y = 50

            # self.viewImage(image, 'Line')

            cv2.imwrite(f'images/image_{self.day_handler(day).strftime("%Y-%m-%d")}.jpg',image)

    def put_image(self, background, state, x, y):
        img1 = background

        img2 = cv2.imread(self.LINKS[state])

        scale_percent = 100  # Процент от изначального размера
        width = int(img2.shape[1] * scale_percent / 100)
        height = int(img2.shape[0] * scale_percent / 100)
        dim = (width, height)
        img2 = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)

        rows, cols, channels = img2.shape
        roi = img1[0:rows, 0:cols]

        img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)

        img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

        img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

        dst = cv2.add(img1_bg, img2_fg)
        img1[0 + y - 50:rows + y - 50, 0 + x:cols + x] = dst

        return img1

    def gradient(self, image, state):
        y = image.shape[0]
        x = image.shape[1]

        for i in range(y):
            for j in range(x):
                if state == 'Ясно':
                    k = j / x
                    k_g = 1
                    k_r = 1
                    k_b = k
                elif state == 'Дождь':
                    k = j / x
                    k_g = k
                    k_r = k
                    k_b = 1
                elif state == 'cнег':
                    k = j / x
                    k_g = 1
                    k_r = k
                    k_b = 1
                elif state == 'Пасмурно':
                    k = j / (j + 100)
                    k_g = k
                    k_r = k
                    k_b = k
                elif state == 'Малооблачно':
                    k = j / (j + 100)
                    k_g = k
                    k_r = k
                    k_b = k
                elif state == 'Облачно':
                    k = j / (j + 100)
                    k_g = k
                    k_r = k
                    k_b = k
                else:
                    k_g = 1
                    k_r = 1
                    k_b = 1

                g = 255 * k_g
                r = 255 * k_r
                b = 255 * k_b
                image[i, j] = (b, g, r)
        return image

    def day_handler(self, day):

        _, number, month = day.split(' ')

        equal = {'янв': 1, 'фев': 2,
                 'мар': 3, 'апр': 4,
                 'май': 5, 'июн': 6,
                 'июл': 7, 'авг': 8,
                 'сен': 9, 'окт': 10,
                 'ноя': 11, 'дек': 12,
                 }
        date = datetime.date(year=datetime.date.today().year, month=equal[month], day=int(number))
        return date


class DatabaseUpdater:
    def __init__(self):
        self.database = connect('sqlite:///weather.db')
        models.database_proxy.initialize(self.database)

        self.database.create_tables([models.Weather])



    def set_info(self, data):
        for day, values in data.items():
            date = ImageMaker().day_handler(day).strftime("%Y-%m-%d")

            try:
                info = models.Weather.create(
                    date=date,
                    night=f"{values['Ночь'][0][0]}, Температура: {values['Ночь'][1].replace('−', '-')}",
                    morning=f"{values['Утро'][0][0]}, Температура: {values['Утро'][1].replace('−', '-')}",
                    afternoon=f"{values['День'][0][0]}, Температура: {values['День'][1].replace('−', '-')}",
                    evening=f"{values['Вечер'][0][0]}, Температура: {values['Вечер'][1].replace('−', '-')}",
                )
            except:
                print('Повторение записи')

    def get_info(self, date_low=None, date_high=None):
        if (date_low is not None) and (date_high is not None):
            range_low = date_low
            range_high = date_high

            for weather in models.Weather.select().where((models.Weather.date >= range_low) &
                                                         (models.Weather.date <= range_high)):
                print(f'{weather.date}: '
                      f'Ночь: {weather.night},'
                      f' Утро: {weather.morning}, '
                      f'День: {weather.afternoon}, '
                      f'Вечер: {weather.evening}')
        else:
            for weather in models.Weather.select(models.Weather):
                print(f'{weather.date}: '
                      f'Ночь: {weather.night},'
                      f' Утро: {weather.morning}, '
                      f'День: {weather.afternoon}, '
                      f'Вечер: {weather.evening}')


class Parser:
    def parser_func(self):
        parser = argparse.ArgumentParser()

        parser.add_argument('--days_count', type=int)
        parser.add_argument('--date_low', type=str)
        parser.add_argument('--date_high', type=str)
        parser.add_argument('--create_ticket', default=False, type=bool)


        args = parser.parse_args()
        return args

if __name__ == '__main__':
    parser = Parser()
    args = parser.parser_func()
    parse = WeatherMaker(days=args.days_count)
    parse.parse()
    data = parse.data
    if args.create_ticket:
        img = ImageMaker()
        img.put_data(data=data)
    db = DatabaseUpdater()
    db.set_info(data=parse.data)
    db.get_info(date_low=args.date_low, date_high=args.date_high)


