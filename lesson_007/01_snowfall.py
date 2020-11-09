# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self):
        self.x = 100
        self.y = 500
        self.length = 50
        self.step = 10

    def clear_previous_picture(self):
        self.point = sd.get_point(self.x, self.y)
        # TODO все атрибуты, которые используются в объекте - должны быть сперва инициализированы
        # TODO в init
        sd.snowflake(center=self.point, length=self.length, color=sd.background_color)

    def move(self):
        self.y -= self.step

    def draw(self):
        self.point = sd.get_point(self.x, self.y)
        sd.snowflake(center=self.point, length=self.length, color=sd.COLOR_WHITE)

    def can_fall(self):
        if self.y > 50:
            # TODO В данном случае if/else блок лишний, можно оставить просто return с условием
            # TODO Т.к. само по себе условие равно либо True, либо False
            # TODO пример return a > b
            return True

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
        flake.x *= i  # TODO чтобы не добавлять подобные "костыли" - можно задавать снежинкам случайные значения
        flakes.append(flake)
    return flakes


def get_fallen_flakes():
    global count
    # Еще раз вопрос по поводу глобальной переменной. Если здесь count не объявлять, то выдаст ошибку
    # что переменная используется до объявления,
    # хотя ниже по коду перед циклом count =0, получается функция не работает с ней
    # TODO операция += говорит пайтону о том, что переменная должна быть локальной, если явно не задана её глобальность
    # TODO отсюда и необходимость global
    # TODO но на самом деле от глобальных переменных стоит уходить
    # TODO и применять их только в редких случаях.
    # TODO (они создают зависимость между функцией и внешней переменной,
    # TODO чем меньше таких зависимостей - тем лучше)
    # TODO при этом эта функция должна независимо проходить по всей снежинкам и выдавать список упавших
    # TODO как в 06 было
    if flake.y < 50:  # TODO только тут можно использовать метод can_fall вместо явного сравнения
        count += 1
        return count


def append_flakes(count):

    for i in range(count):
        flake = Snowflake()
        flake.x *=i


        flakes.append(flake)



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


count = 0
while True:

    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
        fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        flakes=[]
        append_flakes(count=fallen_flakes)
        count = 0
        # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
