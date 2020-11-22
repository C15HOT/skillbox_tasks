# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NotNameError(ValueError):
    pass


class NotEmailError(ValueError):
    pass


def analysis(line):
    name, email, age = line.split(' ')

    if not name.isalpha():
        raise NotNameError('Некорректное имя')
    if not ('@' or '.') in email:
        raise NotEmailError('Некорректный @mail')
    if (int(age) > 99 or int(age)) < 10:
        raise ValueError('Некорретный возраст')

with open('registrations.txt', 'r', encoding='utf8') as ff:
    with open('registrations_good.txt', 'w+', encoding='utf8') as good:
        with open('registrations_bad.txt', 'w+', encoding='utf8') as bad:
            for line in ff:
                line = line[:-1]
                try:
                    analysis(line=line)
                    good.write(f'{line}''\n')
                except ValueError as exc:
                    if 'unpack' in exc.args[0]:
                        bad.write(f'Не хватает данных {exc} в строке {line}''\n')
                    else:
                        bad.write(f'{exc} в строке {line}''\n')