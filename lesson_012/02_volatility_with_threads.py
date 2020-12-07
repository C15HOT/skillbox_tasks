# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
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

import threading
from collections import defaultdict
from itertools import islice
from sorter import take_dirs, get_stat
from lesson_012.python_snippets.utils import time_track


class Parser(threading.Thread):

    def __init__(self, file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file = file

    def collect(self):
        prices = []
        with open(file=self.file, mode='r', encoding='utf8') as file:
            for line in islice(file, 1, None):
                secid, tradetime, price, quantity = line.split(',')
                tiker_id = secid
                prices.append(float(price))
            half_sum = ((max(prices) + min(prices)) / 2)
            volatility = ((max(prices) - min(prices)) / half_sum) * 100
            return tiker_id, round(volatility, 3)


@time_track
def main():
    stat = defaultdict(int)
    files_dir = take_dirs('trades')
    files = [Parser(file=file) for file in files_dir]
    for file in files:
        file.start()
        key, value = file.collect()
        stat[key] = value
        file.join()
    get_stat(stat=stat)


if __name__ == '__main__':
    main()
