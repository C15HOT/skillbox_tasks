# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

import zipfile

class CharStat:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.total = 0
        self.new_dict={}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self.line_stat(line=line)

        for char in self.stat.values():
            self.total += char

    def line_stat(self,line):
        for char in line:
            if char.isalpha():

                if char in self.stat:
                    self.stat[char] += 1
                else:
                    self.stat[char] = 1

    def sorter(self,metod_sort):
        if metod_sort == 'алфавит вверх':

            for key in sorted(self.stat):
                self.new_dict[key] = self.stat[key]
        elif metod_sort == 'алфавит вниз':
            for key in sorted(self.stat, reverse=True):
                self.new_dict[key] = self.stat[key]
        else:
            for key, item in sorted(self.stat.items(), key=lambda para : para[1]):
                self.new_dict[key] = self.stat[key]

    # #  выделите сортировку в отдельный метод и её переопределяйте, чтобы не дублировать код

    def print_stat(self):
        print('+{txt:-^20}+'.format(txt='+'))
        print('|{txt:^9}|{txt2:^10}|'.format(txt='Буква', txt2='Частота'))
        print('+{txt:-^20}+'.format(txt='+'))
        for key, item in self.new_dict.items():
            print('|{txt:^9}|{txt2:^10}|'.format(txt=key, txt2=item))
        print('+{txt:-^20}+'.format(txt='+'))
        print('|{txt:^9}|{txt2:^10}|'.format(txt='Итого', txt2=self.total))
        print('+{txt:-^20}+'.format(txt='+'))

    def run(self,metod):
        self.collect()
        self.sorter(metod_sort=metod)
        self.print_stat()
    #  Тут нужно ещё один метод создать, общий(обычно его называют как-нибудь вроде run), который будет объединять
    #  Нужные шаги и запускать их в правильном порядке
    #  открытие файла - сбор данных - сортировка - печать

vim = CharStat(file_name='python_snippets/voyna-i-mir.txt.zip')
vim.run(metod='алфавит вниз')
# vim.collect()
# vim.sorter(metod_sort='алфави вниз')
# vim.print_stat()
# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
