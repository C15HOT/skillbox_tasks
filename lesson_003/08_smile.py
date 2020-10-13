# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random
# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(x,y,color):
    center = sd.get_point(x, y)
    left_eye = sd.get_point(x-20,y+20)
    right_eye = sd.get_point(x + 20, y + 20)
    point1 = sd.get_point(x - 20, y - 10)
    point2 = sd.get_point(x - 10, y - 20)
    point3 = sd.get_point(x + 10, y - 20)
    point4 = sd.get_point(x + 20, y - 10)
    sd.circle(center_position=center, radius=50, color=color, width=1)
    sd.circle(center_position=left_eye, radius=10, color=color, width=1)
    sd.circle(center_position=right_eye, radius=10, color=color, width=1)
    sd.line(start_point=point1, end_point=point2, color=color, width=1)
    sd.line(start_point=point2, end_point=point3, color=color, width=1)
    sd.line(start_point=point3, end_point=point4, color=color, width=1)

for _ in range(10):
    x=random.randint(1,500)
    y = random.randint(1, 500)
    color = sd.random_color()
    smile(x,y,color)

sd.pause()
