



from collections import defaultdict
import os
from pprint import pprint
def take_dirs(path):

    for dir, _, files in os.walk(path):
        for file in files:
            file_dir = dir + '\\' + file
            yield file_dir

def get_stat(stat):
    my_stat=stat
    max_result = defaultdict(int)
    min_result = defaultdict(int)
    null = []
    for key, value in my_stat.items():
        if value == 0:
            null.append(key)
    for key in null:
        my_stat.pop(key)
    for key, item in sorted(my_stat.items(), key=lambda para: para[1], reverse=True)[:3]:
        max_result[key] = my_stat[key]
    for key, item in sorted(my_stat.items(), key=lambda para: para[1])[:3]:
        min_result[key] = my_stat[key]

    print('Максимальная волатильность: ''\n')
    pprint(max_result)
    print('Минимальная волатильность: ''\n')
    pprint(min_result)
    print('Нулевая волатильность: ''\n')
    print(null)