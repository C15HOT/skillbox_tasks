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
    try:
        name, email, age = line.split(' ')
    except ValueError as exc:
        raise ValueError('Не хватает данных')
    #  Такое разделение, да и использование Int на age сами по себе вызывают ошибки
    #  Мы же хотим управлять этим процессом, вызывая их явно
    #  Поэтому попробуйте ошибки ловить условиями и вызывать raise-ом
    #  Такая практика нужна, чтобы научиться отделять наши ошибки (ожидаемые) от чужих
    #  (неожиданных)
    if not name.isalpha():
        raise NotNameError('Некорректное имя')
    if '@' not in email or '.' not in email:
        raise NotEmailError('Некорректный @mail')
    if not age.isdigit():
        raise ValueError('Некорретный возраст')
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
                    bad.write(f'{exc} в строке {line}''\n')
                except Exception as exc:
                    bad.write(f'Непредвиденная ошибка {exc}  в строке {line}''\n')
#зачёт!