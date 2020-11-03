from random import randint

_number=[]

MAX_NUMBER=4
INITIAL_NUMBER=[0,1,2,3,4,5,6,7,8,9]

def think_number():
    global _number
    _number=[]
    for i in range(MAX_NUMBER):
        if i==0:
            _number.append(INITIAL_NUMBER[randint(1,9)])
        else:
            num=INITIAL_NUMBER[randint(0,9)]
            while num in _number:
                num = INITIAL_NUMBER[randint(0, 9)]
            _number.append(num)

think_number()
print(_number)