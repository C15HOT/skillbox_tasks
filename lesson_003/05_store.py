# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Каждая запись отображает сколько и по какой цене закупалось товаров.
#
# Задание: вывести суммарную стоимость каждого ВИДА товара на складе c помощью циклов
#
# Формат вывода:
#   <товар_1> - <кол-во_товара_1> шт, стоимость <общая_стоимость_товара_1> руб
#   <товар_2> - <кол-во_товара_2> шт, стоимость <общая_стоимость_товара_2> руб
#   <товар_4> - <кол-во_товара_3> шт, стоимость <общая_стоимость_товара_3> руб
#
# Например:
#   Стул - 1111 шт, стоимость 8888 руб
#   Диван - 2222 шт, стоимость 9999 руб
#   и так далее
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе

for name, item in goods.items():
    amount = 0
    sum = 0
    for code in range(len(store[item])):
        #  Нэйминг, вместо 'j' можно и нужно придумать что-то полезное, хоть как-то описывающее данные внутри
        #  Здесь цикл надо запускать по списку, а не по его длине
        #  Да и зачастую метод запуска цикла по range(len(список)) - плохая практика
        # Если нужны индексы - можно использовать enumerate
        # for index, element in enumerate(список)
        # Я пытался сделать цикл разными способами, во всех других у меня выдает ошибки.
        # В случае прохода цикла по спику выдает
        # TypeError: list indices must be integers or slices, not str
        amount += (store[item][code]['quantity'])
        sum += (store[item][code]['quantity']) * (store[item][code]['price'])
    print(name, '-', amount, 'шт.,', 'стоимость -', sum)
