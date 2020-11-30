# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def print_fig(point, length, angle=0):
        steps = {3: 120, 4: 90, 5: 72, 6: 60}
        step = steps[n]
        end = point
        for cur_angle in range(0, 360 - step, step):
            v1 = sd.get_vector(start_point=point, angle=angle + cur_angle, length=length, width=3)
            v1.draw()
            point = v1.end_point

        sd.line(start_point=point, end_point=end, width=3)

    return print_fig


draw_triangle = get_polygon(n=6)
draw_triangle(point=sd.get_point(200, 200), length=100, angle=13)

sd.pause()
