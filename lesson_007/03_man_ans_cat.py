# -*- coding: utf-8 -*-

from random import randint

from termcolor import cprint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class Human:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.cat = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness,
        )

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
            self.house.bowl += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def take_cat(self, cat):
        self.cat = cat  # TODO чтобы была возможность заводить больше 1 кошки
        # TODO стоит добавить атрибут-список и в него добавлять кошку
        self.cat.house = self.house
        cprint('{} взял кота {}'.format(self.name, self.cat.name), color='cyan')

    # def buy_food_for_cat(self):
    #     self.house.money -= 50
    #     self.house.bowl += 50
    #     cprint('{} Купил еды коту'.format(self.name), color='cyan')
    def clean_house(self):
        self.house.dirt -= 100
        self.fullness -= 20
        if self.house.dirt < 0:
            self.house.dirt = 0
        cprint('{} убрался в доме'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()

        elif self.house.dirt > 40:
            self.clean_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.dirt = 0
        self.bowl = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, еды для кота осталось {}, грязи дома {}'.format(
            self.food, self.money, self.bowl, self.dirt
        )


class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness,
        )

    def sleep(self):
        cprint('{} спит'.format(self.name), color='green')
        self.fullness -= 10

    def eat(self):
        if self.house.bowl >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.bowl -= 10
        else:
            cprint('{} нет еды для кота'.format(self.name), color='red')

    def cut_wallpaper(self):
        cprint('{} дерет обои'.format(self.name), color='red')
        self.fullness -= 10
        self.house.dirt += 5

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        else:
            self.cut_wallpaper()


man = Human(name='Дима')
cat = Cat(name='Мурзик')

my_sweet_home = House()

man.go_to_the_house(house=my_sweet_home)
man.take_cat(cat=cat)
for day in range(1, 366):
    print('================ день {} =================='.format(day))
    man.act()
    cat.act()
    print('--- в конце дня ---')

    print(man)
    print(cat)
    print(my_sweet_home)
# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
