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
    for i in range(MAX_NUMBER):
        if i == 0:  # TODO от этой проверки можно вовсе избавиться, если добавить
            _number.append(INITIAL_NUMBER[randint(1, 9)])  # TODO эту операцию до цикла
        else:
            num = INITIAL_NUMBER[randint(0, 9)]
            while num in _number:
                num = INITIAL_NUMBER[randint(0, 9)]
            _number.append(num)
    # TODO ещё можно было бы упростить сам цикл - превратить его в while с условием (пока длина списка меньше 4)
    # TODO и в нём тогда не нужно будет вызывать вложенный цикл
    print(_number)


def check(user_input):
    global bulls, cows, result
    bulls, cows = 0, 0
    result = {'Быки': bulls, 'Коровы': cows}
    # for user_number, user_char in enumerate(user_input):
    # TODO всё верно, только условия надо немного подправить
    #     if int(user_char)== _number[int(user_char)]:  - это уже условие, достаточное для быка
    #         if user_number==_number.index(user_char):  - а это уже получается лишним
    #             result['Быки'] += 1
    #             continue
    #         result['Коровы'] += 1
    # TODO Т.е. для быка мы проверяем равно ли текущее число - другому числу с текущим индексом
    # TODO Для коровы - есть ли это число вообще в другом наборе числе (if число in _number)
    for user_number, user_char in enumerate(user_input):
        for comp_number, comp_char in enumerate(_number):
            if int(user_char) == comp_char:
                if user_number == comp_number:
                    result['Быки'] += 1
                    continue
                result['Коровы'] += 1
    print(result)
    # TODO результат не нужно печатать - его надо возвращать
    # TODO а его форматирование и печать нужно прописать в том модуле


def is_gameover():
    return result['Быки'] == 4
