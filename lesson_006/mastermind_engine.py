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
        if i == 0:
            _number.append(INITIAL_NUMBER[randint(1, 9)])
        else:
            num = INITIAL_NUMBER[randint(0, 9)]
            while num in _number:
                num = INITIAL_NUMBER[randint(0, 9)]
            _number.append(num)
    #print(_number)


def check(user_input):
    global bulls, cows, result
    bulls, cows = 0, 0
    result = {'Быки': bulls, 'Коровы': cows}
    # TODO Попробуйте эту проверку реализовать в один цикл
    for user_number, user_char in enumerate(user_input):
        for copm_number, comp_char in enumerate(_number):
            if int(user_char) == comp_char:
                if user_number == copm_number:
                    result['Быки'] += 1
                    continue
                result['Коровы'] += 1
    print(result)


def is_gameover():
    return result['Быки'] == 4
