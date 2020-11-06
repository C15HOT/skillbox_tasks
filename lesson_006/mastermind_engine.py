from random import randint

_number = []
_user_input = []

MAX_NUMBER = 4
INITIAL_NUMBER = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

bulls = 0
cows = 0
result = {'Быки': bulls, 'Коровы': cows}


def think_number():
    global _number
    _number = []
    _number.append(INITIAL_NUMBER[randint(1, 9)])
    for i in range(MAX_NUMBER - 1):
        num = INITIAL_NUMBER[randint(0, 9)]
        while num in _number:
            num = INITIAL_NUMBER[randint(0, 9)]
        _number.append(num)
    #  ещё можно было бы упростить сам цикл - превратить его в while с условием (пока длина списка меньше 4)
    #  и в нём тогда не нужно будет вызывать вложенный цикл
    # Вложенный цикл нужен для проверки условия неповторяемости знаков,
    # пока не вижу как это сделать внутри одного цикла
    # TODO структура примерно такая:
    # TODO while длина списка меньше нужной
    # TODO     создаем случайное число от 0 до 9
    # TODO         если его нет в списке -> добавляем в список
    print(_number)


def check(user_input):
    global bulls, cows, result
    bulls, cows = 0, 0
    result = {'Быки': bulls, 'Коровы': cows}
    for user_number, user_char in enumerate(user_input):
        #  всё верно, только условия надо немного подправить
        if int(user_char) == _number[user_number]:  # - это уже условие, достаточное для быка
            result['Быки'] += 1
            continue  # TODO continue пропускает код, который должен выполниться внутри цикла после if/else блока
        else:
            if int(user_char) in _number:  # TODO else if можно заменить на elif
                result['Коровы'] += 1
        # TODO но тут кода нету, чтобы его пропускать, поэтому continue можно убрать
    # Т.е. для быка мы проверяем равно ли текущее число - другому числу с текущим индексом
    # Для коровы - есть ли это число вообще в другом наборе числе (if число in _number)
    # for user_number, user_char in enumerate(user_input):
    #     for comp_number, comp_char in enumerate(_number):
    #         if int(user_char) == comp_char:
    #             if user_number == comp_number:
    #                 result['Быки'] += 1
    #                 continue
    #             result['Коровы'] += 1
    return result
    #  результат не нужно печатать - его надо возвращать
    #  а его форматирование и печать нужно прописать в том модуле


def is_gameover():
    return result['Быки'] == 4
