# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:
    def __init__(self):
        self.name='Вода'

    def __add__(self, other):
        if getattr(other,'name') == 'Воздух':
            return 'Шторм'
        if getattr(other,'name') == 'Огонь':
            return 'Пар'
        if getattr(other,'name') == 'Земля':
            return 'Грязь'

    def __str__(self):
        return self.name

class Air:
    def __init__(self):
        self.name = 'Воздух'

    def __add__(self, other):
        if getattr(other,'name') == 'Вода':
            return 'Шторм'
        if getattr(other,'name') == 'Огонь':
            return 'Молния'
        if getattr(other,'name') == 'Земля':
            return 'Пыль'

    def __str__(self):
        return self.name

class Earth:
    def __init__(self):
        self.name = 'Земля'

    def __add__(self, other):
        if getattr(other,'name') == 'Вода':
            return 'Грязь'
        if getattr(other,'name') == 'Воздух':
            return 'Пыль'
        if getattr(other,'name') == 'Огонь':
            return 'Лава'

    def __str__(self):
        return self.name

class Fire:
    def __init__(self):
        self.name = 'Огонь'

    def __add__(self, other):
        if getattr(other,'name') == 'Вода':
            return 'Пар'
        if getattr(other,'name') == 'Воздух':
            return 'Молния'
        if getattr(other,'name') == 'Земля':
            return 'Лава'

    def __str__(self):
        return self.name


print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Fire(), '+', Earth(), '=', Fire() + Earth())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
