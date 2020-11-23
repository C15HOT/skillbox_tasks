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
    # TODO Такое разделение, да и использование Int на age сами по себе вызывают ошибки
    # TODO Мы же хотим управлять этим процессом, вызывая их явно
    # TODO Поэтому попробуйте ошибки ловить условиями и вызывать raise-ом
    # TODO Такая практика нужна, чтобы научиться отделять наши ошибки (ожидаемые) от чужих
    # TODO (неожиданных)
    if not name.isalpha():
        raise NotNameError('Некорректное имя')
    if not ('@' or '.') in email:
        # TODO такое условие не сработает
        # TODO важно понимать порядок действий, с которым пайтон выполняет его
        # TODO 1) ('@' or '.') -- результатом этого сравнения будет "@"
        # TODO 2) результат 1 он подставит в проверку - "@" in email
        # TODO 3) и к результату 2 он добавит not
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
                except ValueError as exc:  # TODO а почему ловите только ValueError?
                    if 'unpack' in exc.args[0]:  # TODO стоит ли тут доп проверку выполнять
                        # TODO если вызывается ValueError с разными сообщениями?
                        bad.write(f'Не хватает данных {exc} в строке {line}''\n')
                    else:
                        bad.write(f'{exc} в строке {line}''\n')