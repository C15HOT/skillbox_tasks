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


def triangle(point, length, color, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
    v3.draw(color=color)


point_0 = sd.get_point(300, 300)


def square(point, length, color, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
    v3.draw(color=color)

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=3)
    v4.draw(color=color)


point_1 = sd.get_point(100, 100)


def pentagon(point, length, color, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 72 * 2, length=length, width=3)
    v3.draw(color=color)

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 72 * 3, length=length, width=3)
    v4.draw(color=color)

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 72 * 4, length=length, width=3)
    v5.draw(color=color)


point_2 = sd.get_point(400, 500)


def hexagon(point, length, color, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
    v3.draw(color=color)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
    v4.draw(color=color)

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=3)
    v5.draw(color=color)

    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length, width=3)
    v6.draw(color=color)


point_3 = sd.get_point(700, 200)

list = ['1: Красный',
        '2: Оранжевый',
        '3: Желтый',
        '4: Зеленый',
        '5: Циановый',
        '6: Синий',
        '7: Фиолетовый']

colors = {1: sd.COLOR_RED, 2: sd.COLOR_ORANGE, 3: sd.COLOR_YELLOW, 4: sd.COLOR_GREEN, 5: sd.COLOR_CYAN,
          6: sd.COLOR_BLUE, 7: sd.COLOR_PURPLE}
# TODO В этом случае удобнее создать словарь следующей структуры
# TODO словарь = {'0': {'color_name': 'red', 'sd_name': sd.COLOR_RED},...}
# TODO Таким образом для каждого цвета у нас будет свой словарь. И у каждого словаря будут одинаковые ключи
# TODO 'color_name' и 'sd_name'
# TODO Тогда можно будет легко проверить ввод (user_input in словарь)
# TODO А если среди ключей есть выбор пользователя - по этому ключу мы получим нужный вложенный словарь
# TODO А там все ключи одинаковые, можем получить как название цвета, так и sd_цвет
print('Возможные цвета:', '\n', '\n'.join(list), '\n', 'Введите цвет фигур')
# TODO Я бы вообще предложил отказаться от связки int+input
# TODO В словаре можно использовать числа-строки, '1' например
# TODO И тогда единственное условие, которое нужно будет - есть ли строка user_input среди ключей словаря.
# TODO И пока её там нет - надо повторять инпут
number = int(input())
# TODO Тут хорошо бы реализовать следующие шаги
# TODO 1) Цикл, который распечатает номера и названия цветов из словаря выше
# TODO 2) ввод пользователя (без int, тк ключи в словаре у нас строки, а не числа)
# TODO 3) проверка(лучше в цикле) "если ввод среди ключей словаря" --> то выбранный_цвет = словарь[ввод]['sd_name']
if number in colors:
    color = colors.get(number)
    triangle(point=point_0, color=color, angle=0, length=200)
    square(point=point_1, color=color, angle=0, length=200)
    pentagon(point=point_2, color=color, angle=0, length=100)
    hexagon(point=point_3, color=color, angle=0, length=100)
else:
    print('Вы ввели неверный номер')

sd.pause()
