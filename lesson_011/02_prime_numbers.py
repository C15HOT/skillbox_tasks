# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n):
        self.prime_numbers = []
        self.n = n
        self.i = 0
        self.start_number = 2

    def __iter__(self):
        self.i = 2
        self.prime_numbers = []
        return self

    def __next__(self):
        # self.i += 1  #  это можно убрать
        # if self.i > self.n:
        #     raise StopIteration()
        #  нужно поправить стиль кода
        for number in range(self.i, self.n):

            # не стоит каждый раз начинать с 2,
            # попробуйте начинать с прошлого простого
            # проверку со stopiteration стоит реализовать тут
            #  хотя по сути её вовсе можно вынести из цикла
            #  т.к. цикл будет работать от i до n
            #  т.е. условие self.i == self.n: не сработает
            for prime in self.prime_numbers:
                if number % prime == 0:  # проверяйте тут number
                    #  если вы используете цикл for, то self.i вручную увеличивать не нужно

                    break
            else:
                self.prime_numbers.append(self.i)
                self.i = number

                #  а вот здесь заменяйте self.i = number
                return number
        raise StopIteration()  # понимаете почему это работает?


prime_number_iterator = PrimeNumbers(n=10000)


# for number in prime_number_iterator:
#     print(number)

#  если да - можете приступать ко второй части, если нет - напишите в лмс
# после подтверждения части 1 преподователем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            yield number
            prime_numbers.append(number)


for number_g, number_i in zip(prime_numbers_generator(n=10000), prime_number_iterator):
    print(number_g, number_i, number_g == number_i)

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
