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

    def collect(self):
        with open(file=self.filename, mode='r', encoding='utf8') as file:
            for line in file:
                self.line_stat(line)

    def line_stat(self, line):
        if 'NOK' in line:
            key = line[0:17]
            if key in self.stat:
                self.stat[key] += 1
            else:
                self.stat[key] = 1

    def give_stat(self):
        with open(file='stat.txt', mode='w+', encoding='utf8') as file:
            for key, item in self.stat.items():
                file.write(f'{key}]  {item}''\n')

    # TODO и тут нужен "общий" метод
    # TODO и можно приступать ко второй части

logs = Parser(filename='events.txt')
logs.collect()
logs.give_stat()

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
