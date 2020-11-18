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


class Sorter:
    folder = []
    pathes = []
    dates = []

    def __init__(self, input_path_name, output_path_name):
        self.input_path_name = input_path_name
        self.output_path_name = output_path_name

    def take_dirs(self):
        for i in os.walk(self.input_path_name):
            Sorter.folder.append(i)
        for address, dirs, files in Sorter.folder:
            for file in files:
                Sorter.pathes.append(address + '\\' + file)

    def get_time(self):
        for file in Sorter.pathes:
            file_time = time.gmtime(os.path.getmtime(file))
            Sorter.dates.append([file_time.tm_year, file_time.tm_mon])

    def make_dir(self):
        for date in Sorter.dates:
            out_dir = os.path.normpath(self.output_path_name + '\\' + 'sorted_icons' + '\\' +
                                       str(date[0]) + '\\' + str(date[1]))
            if not os.path.exists(out_dir):
                os.makedirs(our_dir)


our_dir = os.getcwd()
path = os.path.normpath(our_dir + '\\' + 'icons')
sort = Sorter(input_path_name=path, output_path_name=our_dir)
dir = sort.take_dirs()
print(Sorter.pathes)
sort.get_time()
print(Sorter.dates)
sort.make_dir()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
