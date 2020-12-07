# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от полусуммы крайних значений цены за торговую сессию:
#   полусумма = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / полусумма) * 100%
# Например для бумаги №1:
#   half_sum = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / half_sum) * 100 = 8.7%
# Для бумаги №2:
#   half_sum = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / half_sum) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>
import os
from collections import defaultdict
from itertools import islice
from pprint import pprint


class Parser:
    # TODO Класс надо заточить под обработку одного файла, а вне класса пройтись по директории
    # TODO И для каждого файла создать по объекту для расчётов
    # TODO Потом пройти по всем объектам и собрать результаты вместе.
    # TODO Эти все сложности помогут легче выполнить два следующих задания)

    # TODO Ещё было бы удобно выделить сортировку и печать в отдельную функцию
    # TODO И ещё одну функцию-генератор создать, которая на вход будет получать путь к директории
    # TODO А на выход будет выдавать путь к файлу из директории
    # TODO Эти две функции можно будет вынести в отдельный модуль и импортировать в каждое из заданий этого модуля
    def __init__(self, dir):
        self.dir = dir
        self.stat = defaultdict(int)
        self.pathes = []
        self.max_result = defaultdict(int)
        self.min_result = defaultdict(int)
        self.null = []

    def take_dirs(self):

        for dir, _, files in os.walk(self.dir):
            for file in files:
                self.pathes.append(dir + '\\' + file)

    def collect(self):
        prices = []
        for file in self.pathes:
            with open(file=file, mode='r', encoding='utf8') as file:
                for line in islice(file, 1, None):
                    secid, tradetime, price, quantity = line.split(',')
                    tiker_id = secid
                    prices.append(float(price))
                half_sum = ((max(prices) + min(prices)) / 2)
                volatility = ((max(prices) - min(prices)) / half_sum) * 100
                self.stat[tiker_id] = volatility

    def get_stat(self):
        count = 0

        for key, item in sorted(self.stat.items(), key=lambda para: para[1], reverse=True)[:3]:
            self.max_result[key] = self.stat[key]
        for key, item in sorted(self.stat.items(), key=lambda para: para[1], )[:3]:
            self.min_result[key] = self.stat[key]
        for key, value in self.stat.items():
            if value == 0:
                self.null.append(key)
        print('Максимальная волатильность: ''\n')
        pprint(self.max_result)
        print('Минимальная волатильность: ''\n')
        pprint(self.min_result)
        print('Нулевая волатильность: ''\n')
        print(self.null)

    def run(self):
        self.take_dirs()
        self.collect()
        self.get_stat()

# TODO Старайтесь рабочий код оборачивать в if __name__ == '__main__'
# TODO С процессами на виндоус это вообще необходимая деталь, а так это просто хороший тон
# TODO чтобы код запускался только если модуль запускается явно
parser = Parser('trades')
parser.run()
