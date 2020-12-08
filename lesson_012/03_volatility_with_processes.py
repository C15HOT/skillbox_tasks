# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
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
#

import multiprocessing
from collections import defaultdict
from itertools import islice
from sorter import take_dirs, get_stat
from lesson_012.python_snippets.utils import time_track


class Parser(multiprocessing.Process):

    def __init__(self, file, collector, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file = file
        self.tiker_id = None
        self.volatility = None
        self.collector = collector

    def run(self):
        prices = []
        with open(file=self.file, mode='r', encoding='utf8') as file:
            for line in islice(file, 1, None):
                secid, tradetime, price, quantity = line.split(',')
                self.tiker_id = secid
                prices.append(float(price))
            half_sum = ((max(prices) + min(prices)) / 2)
            self.volatility = ((max(prices) - min(prices)) / half_sum) * 100
            self.collector.put(dict(tiker_id=self.tiker_id, volatility=self.volatility))


@time_track
def main():
    collector = multiprocessing.Queue()
    stat = defaultdict(int)
    files_dir = take_dirs('trades')
    files = [Parser(file=file, collector=collector) for file in files_dir]
    for file in files:
        file.start()
    for file in files:
        file.join()
    while not collector.empty():
        data = collector.get()
        stat[data['tiker_id']] = data['volatility']

    get_stat(stat=stat)


if __name__ == '__main__':
    main()
