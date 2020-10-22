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


point = sd.get_point(300, 300)


def triangle(point, length, angle=0):
    # TODO Вместо дублирования векторов можно написать цикл
    # цикл по диапазону углов (0, 360, шаг_угла)
    #     вектор(точка, переменная цикла...)
    #     точка = концу_вектора
    # TODO Такой цикл позволит сильно сократить код.
    # TODO Помимо этого расширит возможности, позволяя рисовать множество разных многоугольников одной функцией
    # TODO (т.е. это будет заделкой на вторую часть задания как раз)
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
    v3.draw()
    # TODO Если приблизить итоговую фигуру, нарисованную векторами, будет заметен разрыв между последней стороной
    # TODO и начальной точкой.
    # TODO Этот разрыв надо убрать.
    # TODO Происходит это потому, что вектор рисуется из одной точки, а координаты второй рассчитываются
    # TODO Расчёты округляются до целых чисел (тк нельзя нарисовать пол пикселя)
    # TODO Из-за этого появляются неточности, которые копятся с каждой стороной и в итоге происходит разрыв.
    # TODO В нашем случае решить это можно с помощью sd.line() вместо последнего вектора.

# TODO ПРИМЕР:
# TODO Первый вариант с расчётом всех 3 углов для треугольника
start_angle = 20
step = 120
print('start 1')
for cur_angle in range(0, 360, step):  # TODO Тут будет 3 итерации
    print(cur_angle, start_angle, cur_angle + start_angle)
print('end 1')
print('start 2')
for cur_angle in range(0, 360 - step, step):  # TODO Тут 1 итерация убирается (за счёт уменьшения 360 на один шаг)
    print(cur_angle, start_angle, cur_angle + start_angle)
print('end 2')
# TODO Таким образом мы можем 1) Рассчитывать углы при помощи цикла
# TODO 2) Управлять количеством итераций цикла. Это нужно чтобы последнюю сторону нарисовать линией.

# TODO Попробуйте использовать эти приёмы и реализовать
# TODO 1) Расчёт угла в цикле
# TODO 2) Передачу начального угла (который задан параметром) и угла из цикла в вектор
# TODO 3) Нарисовать последнюю линию при помощи sd.line
# TODO (или хотя бы для начала не рисовать последнюю сторону вообще)

# TODO Код в файле нужно разделить на части
# TODO Сперва идут импорты
# TODO Затем идут def-ы (создание функций)
# TODO А уже затем исполняемый код, который создает точки и вызывает функции
point_0 = sd.get_point(300, 300)
triangle(point=point_0, angle=0, length=200)


def square(point, length, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=3)
    v4.draw()


point_1 = sd.get_point(100, 100)
square(point=point_1, angle=0, length=200)


def pentagon(point, length, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 72 * 2, length=length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 72 * 3, length=length, width=3)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 72 * 4, length=length, width=3)
    v5.draw()


point_2 = sd.get_point(400, 500)
pentagon(point=point_2, angle=0, length=100)


def hexagon(point, length, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=3)
    v5.draw()

    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length, width=3)
    v6.draw()


point_3 = sd.get_point(700, 200)
hexagon(point=point_3, angle=0, length=100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
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
