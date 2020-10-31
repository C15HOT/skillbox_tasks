# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

import district.central_street.house1.room1
import district.central_street.house1.room2
import district.central_street.house2.room1
import district.central_street.house2.room2
import district.soviet_street.house1.room1
import district.soviet_street.house1.room2
import district.soviet_street.house2.room1
import district.soviet_street.house2.room2

#  попробуйте сперва сложить все списки, а затем использовать один join
humans = (district.central_street.house1.room1.folks + district.central_street.house1.room2.folks + ['\n'] +
          district.central_street.house2.room1.folks + district.central_street.house2.room2.folks + ['\n'] +
          district.soviet_street.house1.room1.folks + district.soviet_street.house1.room2.folks + ['\n'] +
          district.soviet_street.house2.room1.folks + district.soviet_street.house2.room2.folks)

print('На районе живут: ', ','.join(humans))
# Очень странно что pycharm видит только несколько модулей из общего списка, если не делать папку district источником
# Соответственно, без этой операции программа не работает.
#  Путь к модулю надо рассчитывать от рабочей директории - это та директория, в которой лежит запускаемый модуль
#  В нашем случае это lesson_005
#  значит к путям надо добавить district.central_street.house1.room1
# В этом случае все выводится в одну строку
# при добавлении district к пути все закрашивается серым все равно(
#зачёт!