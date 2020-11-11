# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self):
        self.x = randint(100, 500)
        self.y = 500
        self.length = 25
        self.step = 10
        self.point = None

    def clear_previous_picture(self):
        self.point = sd.get_point(self.x, self.y)
        # все атрибуты, которые используются в объекте - должны быть сперва инициализированы
        #  в init
        sd.snowflake(center=self.point, length=self.length, color=sd.background_color)

    def move(self):
        self.y -= self.step

    def draw(self):
        self.point = sd.get_point(self.x, self.y)
        sd.snowflake(center=self.point, length=self.length, color=sd.COLOR_WHITE)

    def can_fall(self):
        return self.y > 50
        # if self.y > 50:
        #     #  В данном случае if/else блок лишний, можно оставить просто return с условием
        #     #  Т.к. само по себе условие равно либо True, либо False
        #     #  пример return a > b
        #     return True

    # def get_fallen_flakes(self):
    #     global count
    #
    #     if self.y <50:
    #         count +=1
    #         return count
    # def append_flakes(self,count):
    #     for i in range(count):
    #         flake = Snowflake()
    #         flake.x = randint(0,500)
    #         flakes.append(flake)


def get_flakes(count):
    flakes = []
    for i in range(count):
        flake = Snowflake()
        #  создаение случайного значения можео реализовать внутри класса
        #  в методе init у snowflake
        # flake.x *= randint(0, 7)  # чтобы не добавлять подобные "костыли" - можно задавать снежинкам случайные значения
        flakes.append(flake)
    return flakes


number_fallen_flakes = []


def get_fallen_flakes():
    # Эта функция должна проходить по списку снежинок и возвращать либо индексы упавших
    #  либо список самих снежинок
    # global count   глобальные переменные стоит убрать
    # Еще раз вопрос по поводу глобальной переменной. Если здесь count не объявлять, то выдаст ошибку
    # что переменная используется до объявления,
    # хотя ниже по коду перед циклом count =0, получается функция не работает с ней
    # операция += говорит пайтону о том, что переменная должна быть локальной, если явно не задана её глобальность
    #  отсюда и необходимость global
    #  но на самом деле от глобальных переменных стоит уходить
    #  и применять их только в редких случаях.
    #  (они создают зависимость между функцией и внешней переменной,
    #  чем меньше таких зависимостей - тем лучше)
    #  при этом эта функция должна независимо проходить по всей снежинкам и выдавать список упавших
    #  как в 06 было
    # if not flake.can_fall():  # только тут можно использовать метод can_fall вместо явного сравнения
    #     count += 1
    #     return count
    number_fallen_flakes = []
    for number, flake in enumerate(flakes):
        if not flake.can_fall():
            number_fallen_flakes.append(number)
    return number_fallen_flakes


def append_flakes(number_fallen_flakes):
    for i in number_fallen_flakes:
        flake = Snowflake()
        # flake.x *= randint(0, 7)
        flakes.pop(i)
        flakes.insert(i, flake)


# ещё нужна функция, которая удалит лишние снежинки из списка - #TODO добавил в append_flakes
# flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.05)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
N = 5
flakes = get_flakes(count=N)  # создать список снежинок

while True:

    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        # flakes = []
        append_flakes(number_fallen_flakes=fallen_flakes)

        # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
