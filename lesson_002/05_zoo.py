#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.insert(1, 'beer')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark']
#  и выведите список на консоль
# zoo.extend([birds[0],birds[1],birds[2]])
zoo.extend(birds)
print(zoo)

# уберите слона
#  и выведите список на консоль
zoo.remove('elephant')

print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
print('лев сидит в клетке с номером ', zoo.index('lion') + 1)
print('жаворонок сидит в клетке с номером ', zoo.index('lark') + 1)

#зачёт!