# -*- coding: utf-8 -*-

import simple_draw as sd

sd.set_screen_size(1200, 800)
# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

#  Вместо дублирования векторов можно написать цикл
# цикл по диапазону углов (0, 360, шаг_угла)
#     вектор(точка, переменная цикла...)
#     точка = концу_вектора
# Такой цикл позволит сильно сократить код.
#  Помимо этого расширит возможности, позволяя рисовать множество разных многоугольников одной функцией
#  (т.е. это будет заделкой на вторую часть задания как раз)


point = sd.get_point(300, 300)


def triangle(point, length, angle=0):
    step = 120
    end = point
    for cur_angle in range(0, 360 - step, step):
        v1 = sd.get_vector(start_point=point, angle=angle + cur_angle, length=length, width=3)
        v1.draw()
        point = v1.end_point

    sd.line(start_point=point, end_point=end, width=3)


def square(point, length, angle=0):
    step = 90
    end = point
    for cur_angle in range(0, 360 - step, step):
        v1 = sd.get_vector(start_point=point, angle=angle + cur_angle, length=length, width=3)
        v1.draw()
        point = v1.end_point

    sd.line(start_point=point, end_point=end, width=3)


def pentagon(point, length, angle=0):
    step = 72
    end = point
    for cur_angle in range(0, 360 - step, step):
        v1 = sd.get_vector(start_point=point, angle=angle + cur_angle, length=length, width=3)
        v1.draw()
        point = v1.end_point

    sd.line(start_point=point, end_point=end, width=3)


def hexagon(point, length, angle=0):
    step = 60
    end = point
    for cur_angle in range(0, 360 - step, step):
        v1 = sd.get_vector(start_point=point, angle=angle + cur_angle, length=length, width=3)
        v1.draw()
        point = v1.end_point

    sd.line(start_point=point, end_point=end, width=3)


# triangle(point=point, length=100, angle=0)
# square(point=point, length=100, angle=0)
# pentagon(point=point, length=100, angle=0)
# hexagon(point=point, length=100, angle=0)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.

def print_fig(point, length, step, angle=0):
    end = point
    for cur_angle in range(0, 360 - step, step):
        v1 = sd.get_vector(start_point=point, angle=angle + cur_angle, length=length, width=3)
        v1.draw()
        point = v1.end_point

    sd.line(start_point=point, end_point=end, width=3)


def triangle_2(point, length, angle=0):
    point = point
    length = length
    step = 120
    print_fig(point, length, step, angle)


def square_2(point, length, angle=0):
    point = point
    length = length
    step = 90
    print_fig(point, length, step, angle)


def pentagon_2(point, length, angle=0):
    point = point
    length = length
    step = 72
    print_fig(point, length, step, angle)


def hexagon_2(point, length, angle=0):
    point = point
    length = length
    step = 60
    print_fig(point, length, step, angle)


triangle_2(point=point, length=100, angle=0)
square_2(point=point, length=100, angle=0)
pentagon_2(point=point, length=100, angle=0)
hexagon_2(point=point, length=100, angle=0)
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
#зачёт!