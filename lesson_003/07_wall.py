# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
COLOR_YELLOW = (255, 255, 0)
slide = 0

sd.resolution = 1000, 600

point_x, point_y = 100, 50
for row, y in enumerate(range(0, 1000, 50)):
    x0 = -50 if row % 2 == 0 else 0
    for x in range(x0, 1000, 100):
        left = sd.get_point(0 + x, 0 + y)
        right = sd.get_point(point_x + x, point_y + y)
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
#зачёт!