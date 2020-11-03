from random import randint

_number = []
_user_input = []

MAX_NUMBER = 4
INITIAL_NUMBER = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


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


def check(user_number):
    bulls = 0
    cows = 0
    for number_i in user_number:
        for number_j in _number:
            if int(user_number[number_i]) in _number[number_j]:
                if number_i == number_j:
                    bulls += 1
            else:
                cows += 1
    return bulls, cows

think_number()
print(_number)
check('1234')
