# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:
    total_food = 0
    total_money = 0
    total_bowl = 0

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.bowl = 30

    def __str__(self):
        return 'В доме денег - {}, еды - {}, грязи - {}, еды для кота - {}'.format(self.money, self.food, self.dirt,
                                                                                   self.bowl)


class Human:

    def __init__(self, name):
        self.fullness = 30
        self.happiness = 100
        self.house = None
        self.name = name
        self.cats = []

    def __str__(self):
        return 'Я {}, сытость - {}, счастье - {}'.format(self.name, self.fullness, self.happiness)

    def eat(self):
        self.fullness += 30
        self.house.food -= 30
        House.total_food += 30
        cprint('{} поел, еды осталось {}'.format(self.name, self.house.food), color='cyan')

    def go_to_the_house(self, house):
        self.house = house
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер от голода'.format(self.name), color='red')
            return False
        if self.happiness <= 10:
            cprint('{} умер от депрессии'.format(self.name), color='red')
            return False
        else:
            if self.house.dirt > 90:
                self.happiness -= 10
            return True

    def take_cat(self, cat):
        self.cat = cat
        #  чтобы была возможность заводить больше 1 кошки
        #  стоит добавить атрибут-список и в него добавлять кошку
        self.cats.append(cat)
        self.cat.house = self.house
        cprint('{} взял кота {}'.format(self.name, self.cat.name), color='cyan')

    def buy_food_for_cat(self):
        self.house.money -= 50
        self.house.bowl += 50

        cprint('{} Купил еды коту'.format(self.name), color='cyan')
    #  Помимо целых действий вроде eat
    #  Можно выделять схожие части методов и выносить их в родительский класс
    #  Например можно взять общие проверки и действия из act
    # Записать их в act родительского класса, добавив к ним возврат
    #  либо True, либо False
    #  True - если человек жив и способен выполнить какое-нибудь действие
    #  False - если человек мертв или уже выполнил одно из действий
    #  В act наследников тогда нужно будет использовать вызов метода через super()
    #  и проверить то, что вернёт этот вызов (if super().func())
    #Если возвращается True - продолжать выбор действия, если False - завершать функцию


class Husband(Human):

    # def __init__(self, name):
    #     self.name = name

    def __str__(self):
        return super().__str__()

    def act(self):
        # if self.fullness <= 0:
        #     cprint('{} умер от голода'.format(self.name), color='red')
        #     return
        # if self.happiness <= 10:
        #     cprint('{} умер от депрессии'.format(self.name), color='red')
        #     return
        if super().act():

            if self.house.money < 50:
                self.work()
            if self.house.bowl < 50:
                self.buy_food_for_cat()
            dice = randint(1, 6)
            if self.fullness < 20:
                self.eat()
            elif dice == 1:
                self.work()
            elif dice == 2:
                self.gaming()
            else:
                self.eat()

    # def eat(self):
    #     pass

    def work(self):
        self.fullness -= 10
        self.house.money += 150
        House.total_money += 150
        cprint('{} сходил на работу, денег - {}, сытость - {}'.format(self.name,
                                                                      self.house.money, self.fullness), color='cyan')

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        cprint('{} играет в танки, счастье - {}, сытость - {}'.format(self.name,
                                                                      self.happiness, self.fullness), color='cyan')


class Wife(Human):
    total_coat = 0

    # def __init__(self):
    #     pass

    def __str__(self):
        return super().__str__()

    def act(self):
        # if self.fullness <= 0:
        #     cprint('{} умерла от голода'.format(self.name), color='red')
        #     return
        # if self.happiness <= 10:
        #     cprint('{} умерла от депрессии'.format(self.name), color='red')
        #     return
        if super().act():

            if self.house.food < 30:
                self.shopping()
            dice = randint(1, 6)
            if self.fullness < 20:
                self.eat()
            elif self.house.food < 20:
                self.shopping()
            elif dice == 1:
                self.clean_house()
            elif dice == 2:
                if self.house.money > 350:
                    self.buy_fur_coat()
            else:
                self.eat()

    # def eat(self):
    #     pass

    def shopping(self):
        self.fullness -= 10
        self.house.food += 60
        self.house.money -= 60
        cprint('{} купила еды, денег осталось - {}, еды в доме - {}'.format(self.name, self.house.money,
                                                                            self.house.food), color='cyan')

    def buy_fur_coat(self):
        self.fullness -= 10
        self.happiness += 60
        self.house.money -= 350
        Wife.total_coat += 1
        cprint('{} купила шубу, денег осталось - {}, счастье - {}'.format(self.name, self.house.money,
                                                                          self.happiness), color='cyan')

    def clean_house(self):
        self.fullness -= 10
        self.house.dirt -= 100
        if self.house.dirt < 0:
            self.house.dirt = 0
        cprint('{} убралась в доме, сытость - {}, грязи - {}'.format(self.name, self.fullness,
                                                                     self.house.dirt), color='cyan')


class Child(Human):

    def __init__(self,name):
        super().__init__(name=name)
        self.happiness = 100

    def __str__(self):
        return super().__str__()

    def act(self):
        if super().act():
            if self.fullness < 20:
                self.eat()
            else:
                self.sleep()


    def eat(self):
        self.fullness += 10
        self.house.food -= 10
        House.total_food += 10
        cprint('{} поел, еды осталось {}'.format(self.name, self.house.food), color='cyan')

    def sleep(self):
        cprint('{} спит'.format(self.name), color='green')
        self.fullness -= 10


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness,
        )

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
            self.soil()

    def eat(self):
        if self.house.bowl >= 10:
            self.fullness += 20
            self.house.bowl -= 10
            House.total_bowl += 10
            cprint('{} поел'.format(self.name), color='yellow')
        else:
            cprint('{} нет еды для кота'.format(self.name), color='red')

    def sleep(self):
        cprint('{} спит'.format(self.name), color='green')
        self.fullness -= 10

    def soil(self):
        cprint('{} дерет обои'.format(self.name), color='red')
        self.fullness -= 10
        self.house.dirt += 5


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
cat = Cat(name='Мурзик')
son = Child(name='Андрюша')
son.go_to_the_house(house=home)
serge.go_to_the_house(house=home)
masha.go_to_the_house(house=home)
serge.take_cat(cat=cat)
for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    # логику с уменьшением счастья лучше тоже убрать в дейсвтие к человеку
    # if home.dirt > 90:
    #     serge.happiness -= 10
    #     masha.happiness -= 10
    serge.act()
    masha.act()
    son.act()
    cat.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(cat, color='cyan')
    cprint(son, color='cyan')
    cprint(home, color='cyan')
cprint('Всего съедено еды {}'.format(House.total_food), color='yellow')
cprint('Всего заработано денег {}'.format(House.total_money), color='yellow')
cprint('Всего кулено шуб {}'.format(Wife.total_coat), color='yellow')
cprint('Всего съедено еды для кота {}'.format(House.total_bowl), color='yellow')

# после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


# class Cat:
#
#     def __init__(self):
#         pass
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

# class Child:
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass


# после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
#зачёт!