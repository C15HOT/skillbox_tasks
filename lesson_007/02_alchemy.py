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
class Storm:
    def __init__(self):
        self.name = 'Шторм'


class Steam:
    def __init__(self):
        self.name = 'Пар'


class Dirt:
    def __init__(self):
        self.name = 'Грязь'


class Lightning:
    def __init__(self):
        self.name = 'Молния'


class Dust:
    def __init__(self):
        self.name = 'Пыль'


class Lava:
    def __init__(self):
        self.name = 'Лава'


class Water:
    def __init__(self):
        self.name = 'Вода'

    def __add__(self, other):
        # Такая проверка - антипаттерн,
        #  В таких случаях стоит использовать проверку isinstance(other, Class)
        if isinstance(other, Air):
            obj = Storm()
            return obj.name
        elif isinstance(other, Fire):
            obj = Steam()
            return obj.name
        elif isinstance(other, Earth):
            obj = Dirt()
            return obj.name

    def __str__(self):
        return self.name


class Air:
    def __init__(self):
        self.name = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            obj = Storm()
            return obj.name
        elif isinstance(other, Fire):
            obj = Lightning()
            return obj.name
        elif isinstance(other, Earth):
            obj = Dust()
            return obj.name

    def __str__(self):
        return self.name


class Earth:
    def __init__(self):
        self.name = 'Земля'

    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()

        elif isinstance(other, Fire):
            obj = Lava()
            return obj.name

        elif isinstance(other, Water):
            obj = Dirt()
            return obj.name

    def __str__(self):
        return self.name


class Fire:
    def __init__(self):
        self.name = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Air):
            obj = Lightning()
            return obj.name
        elif isinstance(other, Water):
            obj = Steam()
            return obj.name
        elif isinstance(other, Earth):
            obj = Lava()
            return obj.name

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
#зачёт!