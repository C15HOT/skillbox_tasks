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

def one_day():
    number=randint(1,13)
    if number <=7:
        return number
    elif number == 8:
        raise IamGodError('Я бог')
    elif number ==9:
        raise DrunkError('Я напился')
    elif number ==10:
        raise CarCrashError('Я разбился на машине')
    elif number ==11:
        raise GluttonyError('Я объелся')
    elif number ==12:
        raise DepressionError('Я в депрессии')
    elif number ==13:
        raise SuicideError('Я самоубился')
with open(file='log.txt', mode='w+', encoding='utf8') as file:
    while total < ENLIGHTENMENT_CARMA_LEVEL:

            try:
                total += one_day()

            except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as exc:
                file.write(f'{exc}''\n')
    print(total)
# https://goo.gl/JnsDqu
