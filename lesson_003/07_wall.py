# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
COLOR_YELLOW = (255, 255, 0)
slide=0
for y in range(0,1000,50):
    slide+=50
    for x in range(-1000,1000,100):
        left = sd.get_point(0+x+slide,0+y)
        right = sd.get_point(100 + x+slide, 50+ y)
        sd.rectangle(left_bottom=left, right_top=right, color=COLOR_YELLOW, width=1)
# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

sd.pause()
