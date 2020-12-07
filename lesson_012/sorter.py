from collections import defaultdict
import os


def take_dirs(path):
    for dir, _, files in os.walk(path):
        for file in files:
            file_dir = dir + '\\' + file
            yield file_dir


def get_stat(stat):
    my_stat = stat
    max_result = defaultdict(int)
    min_result = defaultdict(int)
    null = []
    for key, value in my_stat.items():
        if value == 0:
            null.append(key)
    null.sort(key=str)
    for key in null:
        my_stat.pop(key)
    for key, item in sorted(my_stat.items(), key=lambda para: para[1], reverse=True)[:3]:
        max_result[key] = my_stat[key]
    for key, item in sorted(my_stat.items(), key=lambda para: para[1])[:3]:
        min_result[key] = my_stat[key]
    max_res_list = sorted(max_result, reverse=True)
    min_res_list = sorted(min_result, reverse=True)
    print('Максимальная волатильность: ')
    for key in max_res_list:
        print(key, ' - ', max_result[key], '%')
    print('Минимальная волатильность: ')
    for key in min_res_list:
        print(key, ' - ', min_result[key], '%')
    print('Нулевая волатильность: ')
    print(', '.join(null))
