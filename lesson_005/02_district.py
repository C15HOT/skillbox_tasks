# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

import central_street.house1.room1
import central_street.house1.room2
import central_street.house2.room1
import central_street.house2.room2
import soviet_street.house1.room1
import soviet_street.house1.room2
import soviet_street.house2.room1
import soviet_street.house2.room2
# TODO попробуйте сперва сложить все списки, а затем использовать один join
print('На районе живут: ', ','.join(central_street.house1.room1.folks), '\n',
      ','.join(central_street.house1.room2.folks),
      ','.join(central_street.house2.room1.folks), '\n', ','.join(central_street.house2.room2.folks), ',',
      ','.join(soviet_street.house1.room1.folks), '\n', ','.join(soviet_street.house1.room2.folks), ',',
      ','.join(soviet_street.house2.room1.folks), '\n', ','.join(soviet_street.house2.room2.folks))
# Очень странно что pycharm видит только несколько модулей из общего списка, если не делать папку district источником
# Соответственно, без этой операции программа не работает.
# TODO Путь к модулю надо рассчитывать от рабочей директории - это та директория, в которой лежит запускаемый модуль
# TODO В нашем случае это lesson_005
# TODO значит к путям надо добавить district.central_street.house1.room1
