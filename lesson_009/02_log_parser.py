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

    def __init__(self, filename):
        self.filename = filename
        self.stat = {}
        self.year_dict = {}
        self.mon_dict = {}
        self.hour_dict = {}
        self.keys_year = []
        self.keys_mon = []
        self.keys_hour = []

    def collect(self):
        with open(file=self.filename, mode='r', encoding='utf8') as file:
            for line in file:
                self.line_stat(line)

    def change_border(self, left, right):
        self.right_border = right
        self.left_border = left

    def line_stat(self, line):
        self.change_border(left=1, right=17)
        if 'NOK' in line:
            key = line[self.left_border:self.right_border]
            if key in self.stat:
                self.stat[key] += 1
            else:
                self.stat[key] = 1

    def give_stat(self):
        with open(file='stat.txt', mode='w+', encoding='utf8') as file:
            for key, item in self.stat.items():
                file.write(f'{key}  {item}''\n')

    def sorter(self, metod):

        if metod == 'hour':

            any_list = self.keys_hour
        elif metod == 'mon':

            any_list = self.keys_mon
        else:

            any_list = self.keys_year

        for key, item in self.stat.items():
            any_list.append(str(key[self.left_border:self.right_border]))
        any_list = set(any_list)
        any_list = sorted(list(any_list))
        return any_list

    def group(self, metod):

        if metod == 'hour':
            self.change_border(left=11, right=13)
            iterable_stat = self.sorter(metod=metod)

            # iterable_stat = self.keys_hour
        elif metod == 'mon':
            self.change_border(left=5, right=7)
            self.sorter(metod=metod)

            iterable_stat = self.sorter(metod=metod)
        else:
            self.change_border(left=0, right=4)
            self.sorter(metod=metod)
            iterable_stat = self.sorter(metod=metod)

        with open(file='stat.txt', mode='w+', encoding='utf8') as file:
            for date in iterable_stat:
                for key, item in self.stat.items():
                    if str(key[self.left_border:self.right_border]) == date:
                        file.write(f'{key}  {item}''\n')

    def run(self, metod):
        self.collect()
        # self.give_stat()
        # self.sorter(metod=metod)
        self.group(metod=metod)


logs = Parser(filename='events.txt')
logs.run(metod='hour')

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
