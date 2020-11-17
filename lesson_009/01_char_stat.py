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
from pprint import pprint
class CharStat:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.total = 0

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

        for i in self.stat.values():
            self.total += i

    def line_stat(self,line):
        for char in line:
            if char.isalpha():

                if char in self.stat:
                    self.stat[char] += 1
                else:
                    self.stat[char] = 1

    def print_stat(self):
        print('+{txt:-^20}+'.format(txt='+'))
        print('|{txt:^9}|{txt2:^10}|'.format(txt='Буква', txt2='Частота'))
        print('+{txt:-^20}+'.format(txt='+'))
        for key, item in self.stat.items():
            print('|{txt:^9}|{txt2:^10}|'.format(txt=key, txt2=item))
        print('+{txt:-^20}+'.format(txt='+'))
        print('|{txt:^9}|{txt2:^10}|'.format(txt='Итого', txt2=self.total))
        print('+{txt:-^20}+'.format(txt='+'))


vim = CharStat(file_name='python_snippets/voyna-i-mir.txt.zip')
vim.collect()
vim.print_stat()
# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
