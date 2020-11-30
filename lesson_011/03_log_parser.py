# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


def line_stat():
    stat={}
    with open(file='events.txt', mode='r', encoding='utf8') as file:
        for line in file:

            if 'NOK' in line:
                key = line[1:17]
                if key in stat:
                    stat[key] += 1

                else:
                    stat[key] = 1
                yield key, stat[key]




logs = line_stat()
for keys, count in logs:
    print(f'{keys} {count}')
#  файл завершается так:
# [2018-05-17 11:32:27.873687] OK
# [2018-05-17 11:32:29.873687] OK
# [2018-05-17 11:33:11.873687] NOK
# [2018-05-17 11:33:48.873687] OK
# [2018-05-17 11:34:16.873687] OK
# [2018-05-17 11:34:50.873687] NOK
# [2018-05-17 11:35:34.873687] OK
#  у вас ответ в конце такой
# 2018-05-17 11:33 4
# 2018-05-17 11:34 3
#  откуда лишние значения появляются?