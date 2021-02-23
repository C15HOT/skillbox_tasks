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

import requests
from bs4 import BeautifulSoup
import re
import cv2

r = re.compile("[а-яА-Я]+")


class WeatherMaker:
    DAYS = 3

    def __init__(self):
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
        print(self.data)


class ImageMaker:
    PATTERN = 'python_snippets/external_data/probe.jpg'
    LINKS = {
        'Пасмурно': 'png/gray.png',
        'Ясно': 'png/clear.png',
        'снег': 'png/snow.png',
        'Облачно': 'png/cloudy.png',
        'Мокрый снег': 'png/snow_rain.png',
        'Дождь с грозой': 'png/thunder.png',
        'Небольшая облачность': 'png/little_cloudy.png',
        'Небольшой снег': 'png/little_snow.png'
    }

    def viewImage(self, image, name_of_window):
        cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
        cv2.imshow(name_of_window, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def put_data(self, state, data):

        y = 50
        for day, values in data.items():
            image = cv2.imread(self.PATTERN)

            cv2.putText(image, day, (10, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            for states, items in values.items():
                y += 80
                # text = (f"{states}: {','.join(items[0])}, Температура: {items[1]}")
                text = (f"{states}: {items[0][0]}, Температура: {items[1]}")
                print(text)
                cv2.putText(image, text, (10, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            y = 50

            img = self.put_image(background=image, state=state)

            self.viewImage(img, 'Line')
            # cv2.imwrite(f'images/image_{day}.jpg',img)


    def put_image(self, background, state):
        img1 = background
        img2 = cv2.imread(self.LINKS[state])


        rows, cols, channels = img2.shape
        roi = img1[0:rows, 0:cols]


        img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)


        img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)


        img2_fg = cv2.bitwise_and(img2, img2, mask=mask)


        dst = cv2.add(img1_bg, img2_fg)
        img1[0:rows, 0:cols] = dst

        return img1






class DatabaseUpdater:
    pass


if __name__ == '__main__':
    parse = WeatherMaker()
    parse.parse()
    data = parse.data
    img = ImageMaker()
    img.put_data(state='Пасмурно', data=data)

    # for day, values in parse.data.items():
    #     print(day)
    #     for states, items in values.items():
    #         text = (f"{states}: {','.join(items[0])}, Температура: {items[1]}")
    #         print(text)
