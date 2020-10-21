# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длина ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# def draw_branches(start_point, angle, length):
#     if length < 10:
#         return
#     v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
#     v1.draw()
#
#     next_point = v1.end_point
#     next_angle = angle - 30
#     next_angle2 = angle +30
#     next_length = length * .75
#     draw_branches(start_point=next_point, angle=next_angle, length=next_length)
#     draw_branches(start_point=next_point, angle=next_angle2, length=next_length)
#
#
# root_point = sd.get_point(300, 30)
#
# draw_branches(start_point=root_point, angle=90, length=100)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg
def random_draw_branches(start_point, angle, length):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
    v1.draw()
    ugl = sd.random_number(a=0, b=40)
    len = sd.random_number(a=0,b=20)
    next_point = v1.end_point
    next_angle = angle - 30*(1+ugl/100)
    next_angle2 = angle +30*(1+ugl/100)
    next_length = length * .75*(1+len/100)
    random_draw_branches(start_point=next_point, angle=next_angle, length=next_length)
    random_draw_branches(start_point=next_point, angle=next_angle2, length=next_length)


root_point = sd.get_point(300, 30)

random_draw_branches(start_point=root_point, angle=90, length=100)
# Пригодятся функции
# sd.random_number()

sd.pause()
