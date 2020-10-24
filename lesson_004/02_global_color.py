# -*- coding: utf-8 -*-
import simple_draw as sd

sd.set_screen_size(1200, 800)

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

point_0 = sd.get_point(300, 300)
point_1 = sd.get_point(100, 100)
point_2 = sd.get_point(400, 500)
point_3 = sd.get_point(700, 200)


def triangle(point, length, color, angle=0):
    step = 120
    end = point
    for cur_angle in range(0, 360 - step, step):
        v1 = sd.get_vector(start_point=point, angle=angle + cur_angle, length=length, width=3)
        v1.draw(color=color)
        point = v1.end_point

    sd.line(start_point=point, end_point=end, color=color, width=3)


def square(point, length, color, angle=0):
    step = 90
    end = point
    for cur_angle in range(0, 360 - step, step):
        v1 = sd.get_vector(start_point=point, angle=angle + cur_angle, length=length, width=3)
        v1.draw(color=color)
        point = v1.end_point

    sd.line(start_point=point, end_point=end, color=color, width=3)


def pentagon(point, length, color, angle=0):
    step = 72
    end = point
    for cur_angle in range(0, 360 - step, step):
        v1 = sd.get_vector(start_point=point, angle=angle + cur_angle, length=length, width=3)
        v1.draw(color=color)
        point = v1.end_point

    sd.line(start_point=point, end_point=end, color=color, width=3)


def hexagon(point, length, color, angle=0):
    step = 60
    end = point
    for cur_angle in range(0, 360 - step, step):
        v1 = sd.get_vector(start_point=point, angle=angle + cur_angle, length=length, width=3)
        v1.draw(color=color)
        point = v1.end_point

    sd.line(start_point=point, end_point=end, color=color, width=3)


colors = {'1': {'color_name': 'Красный', 'sd_name': sd.COLOR_RED},
          '2': {'color_name': 'Оранжевый', 'sd_name': sd.COLOR_ORANGE},
          '3': {'color_name': 'Желтый', 'sd_name': sd.COLOR_YELLOW},
          '4': {'color_name': 'Зеленый', 'sd_name': sd.COLOR_GREEN},
          '5': {'color_name': 'Циановый', 'sd_name': sd.COLOR_CYAN},
          '6': {'color_name': 'Синий', 'sd_name': sd.COLOR_BLUE},
          '7': {'color_name': 'Фиолетовый', 'sd_name': sd.COLOR_PURPLE}}

#  В этом случае удобнее создать словарь следующей структуры
#  словарь = {'0': {'color_name': 'red', 'sd_name': sd.COLOR_RED},...}
#  Таким образом для каждого цвета у нас будет свой словарь. И у каждого словаря будут одинаковые ключи
#  'color_name' и 'sd_name'
#  Тогда можно будет легко проверить ввод (user_input in словарь)
#  А если среди ключей есть выбор пользователя - по этому ключу мы получим нужный вложенный словарь
#  А там все ключи одинаковые, можем получить как название цвета, так и sd_цвет
print('Возможные цвета:')
for number, _ in colors.items():
    print(number, ':', colors[number]['color_name'])

print('Введите цвет фигур')
#  Я бы вообще предложил отказаться от связки int+input
#  В словаре можно использовать числа-строки, '1' например
#  И тогда единственное условие, которое нужно будет - есть ли строка user_input среди ключей словаря.
#  И пока её там нет - надо повторять инпут
user_input = input()
#  Тут хорошо бы реализовать следующие шаги
#  1) Цикл, который распечатает номера и названия цветов из словаря выше
#  2) ввод пользователя (без int, тк ключи в словаре у нас строки, а не числа)
#  3) проверка(лучше в цикле) "если ввод среди ключей словаря" --> то выбранный_цвет = словарь[ввод]['sd_name']
while user_input not in colors:
    print('Вы ввели неверный номер')
    user_input = input()
if user_input in colors:
    color = colors[user_input]['sd_name']
    triangle(point=point_0, color=color, angle=0, length=200)
    square(point=point_1, color=color, angle=0, length=200)
    pentagon(point=point_2, color=color, angle=0, length=100)
    hexagon(point=point_3, color=color, angle=0, length=100)

sd.pause()
