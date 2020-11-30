# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'


def log_errors(file_name):
    def file(func):
        def surrogate(*args,**kwargs):
            with open(file=file_name, mode='a', encoding='utf8') as file:
                try:
                    result = func(*args,**kwargs)
                    # TODO результат выполнения функции надо возвращать return-ом
                except Exception as exc:
                    file.write(f'{exc}''\n')
                    # TODO записать надо больше данных <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
                    # TODO после обработки надо выкинуть это же исключение дальше
                    # TODO сделать raise или raise exc

        return surrogate
    return file



# Проверить работу на следующих функциях
@log_errors(file_name='123.txt')
def perky(param):
    return param / 0


@log_errors(file_name='asdas.txt')
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')
perky(param=42)


# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass
