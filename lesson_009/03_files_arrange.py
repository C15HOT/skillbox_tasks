# -*- coding: utf-8 -*-


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени последней модификации файла
# (время создания файла берется по разному в разых ОС - см https://clck.ru/PBCAX - поэтому берем время модификации).
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником ОС в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит, см .gitignore в папке ДЗ)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4


import os
import os.path
import time
import shutil


class Sorter:


    def __init__(self, input_path_name, output_path_name):
        self.input_path_name = input_path_name
        self.output_path_name = output_path_name
        self.pathes = []
        self.dates = []
        self.finish_folder = []

    def take_dirs(self):
        #  попробуйте оставить один цикл по файлам,
        #  а внутри вызывать метод, который будет выполнять основную работу
        # тогда и промежуточные списки не будут нужны вообще
        for dir, _, files in os.walk(self.input_path_name):
            #  не стоит обращаться к атрибутам класса - используйте атрибуты объекта
            #  (чтобы классы могли работать независимо)
            for file in files:
                self.pathes.append(dir + '\\' + file)

    def get_time(self):
        for file in self.pathes:
            file_time = time.gmtime(os.path.getmtime(file))
            self.dates.append([file_time.tm_year, file_time.tm_mon])

    def make_dir(self):
        #  этот метод у вас работает очень долго
        #  и вы делаете очень много лишних итераций
        #  по сути у вас должен быть один цикл всего
        # по всем файлам папки icons
        #  нужно за одну итерацию формировать путь из даты файла
        #  и копировать его

        for file in self.pathes:
            file_time = time.gmtime(os.path.getmtime(file))
            output_dir = os.path.join(self.output_path_name, 'sorted_icons', str(file_time.tm_year),
                                      str(file_time.tm_mon))
            os.makedirs(output_dir, exist_ok=True)
            shutil.copy2(file, output_dir)

    def run(self):
        self.take_dirs()
        self.get_time()
        self.make_dir()


our_dir = os.getcwd()
path = os.path.normpath(our_dir + '\\' + 'icons')

sort = Sorter(input_path_name=path, output_path_name=our_dir)
# dir = sort.take_dirs()
sort.run()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
