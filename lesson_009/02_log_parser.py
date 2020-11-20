# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

class Parser:
    keys_year = []
    keys_mon = []
    keys_hour = []

    def __init__(self, filename):
        self.filename = filename
        self.stat = {}
        self.year_dict = {}
        self.mon_dict = {}
        self.hour_dict = {}

    def collect(self):
        with open(file=self.filename, mode='r', encoding='utf8') as file:
            for line in file:
                self.line_stat(line)

    def line_stat(self, line):
        if 'NOK' in line:
            key = line[0:17]  # TODO по сути единственное, что надо было изменить это число 17
            # TODO вернитесь к прошлой реализации первой части
            # TODO задайте число 17 при помощи атрибута
            # TODO затем, создайте наследников от этого класса
            # TODO и в каждом наследнике измените этот атрибут
            # TODO чтобы срез шёл от начала до нужной части строки (до часа, до месяца, до года)
            # TODO чтобы группировка шла не по [2018-05-14 19:39
            # TODO а например по [2018-05
            # TODO (кстати лучше не с 0 начинать а с 1, чтобы "[" убрать
            if key in self.stat:
                self.stat[key] += 1
            else:
                self.stat[key] = 1

    def give_stat(self):
        with open(file='stat.txt', mode='w+', encoding='utf8') as file:
            for key, item in self.stat.items():
                file.write(f'{key}]  {item}''\n')

    def sorter(self):
        # TODO создаете очень много лишних действий
        for key in self.stat.items():
            Parser.keys_year.append(str(key)[3:7])
            Parser.keys_mon.append(str(key)[8:10])
            Parser.keys_hour.append(str(key)[14:16])

        Parser.keys_year = set(Parser.keys_year)
        Parser.keys_mon = set(Parser.keys_mon)
        Parser.keys_hour = set(Parser.keys_hour)
        Parser.keys_year = sorted(list(Parser.keys_year))
        Parser.keys_mon = sorted(list(Parser.keys_mon))
        Parser.keys_hour = sorted(list(Parser.keys_hour))
        print(Parser.keys_year, Parser.keys_mon, Parser.keys_hour)

    def group(self, metod):
        # TODO и в этом методе много дублирования
        with open(file='stat.txt', mode='w+', encoding='utf8') as file:
            if metod == 'hour':
                for date in Parser.keys_hour:
                    for key, item in self.stat.items():

                        if str(key[12:14]) == date:

                            file.write(f'{key}]  {item}''\n')

            elif metod == 'mon':
                for date in Parser.keys_mon:
                    for key, item in self.stat.items():

                        if str(key[6:8]) == date:
                            file.write(f'{key}]  {item}''\n')
            else:
                for date in Parser.keys_year:
                    for key, item in self.stat.items():

                        if str(key[1:5]) == date:
                            file.write(f'{key}]  {item}''\n')

    def run(self, metod):
        self.collect()
        # self.give_stat()
        self.sorter()
        self.group(metod=metod)


logs = Parser(filename='events.txt')
logs.run(metod='hour')

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
