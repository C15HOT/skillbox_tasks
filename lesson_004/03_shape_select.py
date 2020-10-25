# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

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


figs = {'1': {'fig_name': 'Треугольник', 'func': triangle}, '2': {'fig_name': 'Квардрат', 'func': square},
        '3': {'fig_name': 'Пятиугольник', 'func': pentagon}, '4': {'fig_name': 'Шестиугольник', 'func': hexagon}}
#  Нам надо реализовать выбор функции пользователем
#  Для этого мы выбираем тот же путь, что в 02 с выбором цвета.
#  Берем ту же структуру данных. Чтобы хранить функции в словаре - надо указать их без скобок, только имя
#  Запустить её можно будет следующим образом:
#  функция = словарь[юзер_выбор]['func']
#  функция(параметры)
point = sd.get_point(300, 300)

print('Возможные фигуры:')
for number, _ in figs.items():
    print(number, ':', figs[number]['fig_name'])

print('Введите название фигуры')
user_input = input()
while user_input not in figs:
    print('Вы ввели неверный номер')
    user_input = input()
if user_input in figs:
    func = figs[user_input]['func']
    func(point=point, angle=0, length=100)

sd.pause()
#зачёт!