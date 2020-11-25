# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
import random
from random import randint

ENLIGHTENMENT_CARMA_LEVEL = 777
total = 0


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


my_exceptions = [IamGodError('Я бог'), DrunkError('Я напился'), CarCrashError('Я разбился на машине'),
                 GluttonyError('Я объелся'), DepressionError('Я в депрессии'), SuicideError('Я самоубился')]


def one_day():
    number = randint(1, 13)
    #  Нам нужно симулировать вероятность 1 к 13. Т.е. приступать к выбору исключения
    #  надо тогда, когда мы поймаем одно из чисел от 1 до 13, например 1
    #  сейчас же вероятность выше :)
    #  можно добавить ещё одно случайное число, уже в нужном нам диапазоне
    #  а можно использовать random.choice для выбора случайного исключения из набора
    #  (например из списка, в котором можно хранить эти исключения)
    if number == 1:
        raise random.choice(my_exceptions)
    elif number > 1:
        #  кстати исключения можно собрать в список или словарь и вызывать их оттуда по индексу/ключу
        return number



with open(file='log.txt', mode='w+', encoding='utf8') as file:
    while total < ENLIGHTENMENT_CARMA_LEVEL:

        try:
            total += one_day()

        except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as exc:
            file.write(f'{exc}''\n')
    print(total)
# https://goo.gl/JnsDqu
