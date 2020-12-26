from abc import ABCMeta, abstractmethod
from collections import defaultdict


class State(metaclass=ABCMeta):
    @abstractmethod
    def throw(self, result):
        pass


class Game():

    def __init__(self, rules='internal'):
        self.score = 0
        self.rules = rules
        if self.rules == 'internal':
            self.firstthrow = FirstThrow(self)
            self.secondthrow = SecondThrow(self)
        else:
            self.firstthrow = FirstThrowExt(self)
            self.secondthrow = SecondThrowExt(self)

        self.state = self.firstthrow
        self.frames = 0
        self.firstthrow_score = 0  # запоминание результата первого броска
        self.frame_result = 0

        self.frames_dict = defaultdict()
        self.frames_dict_result = defaultdict()

        self.is_strike = False
        self.is_spare = False
        self.ext_result = 0

    def throw(self, result):
        self.state.throw(result)

    def get_ext_score(self):
        for key in range(1, 11):
            if self.frames_dict[key][1] == 'X':
                if key == 10:
                    self.frames_dict_result[key] = 10

                else:
                    if self.frames_dict[key + 1][1] == 'X':
                        if key == 9:
                            self.frames_dict_result[key] = 20
                        else:
                            if self.frames_dict[key + 2][1] == 'X':
                                self.frames_dict_result[key] = 30
                            else:
                                self.frames_dict_result[key] = 20 + self.frames_dict[key + 2][1]

                    elif self.frames_dict[key + 1][2] == 'spare':
                        self.frames_dict_result[key] = 20
                    else:
                        self.frames_dict_result[key] = 10 + self.frames_dict[key+1][1] + self.frames_dict[key+1][2]

            elif self.frames_dict[key][2] == 'spare':
                if key == 10:
                    self.frames_dict_result[key] = 10
                else:
                    if self.frames_dict[key + 1][1] == 'X':
                        self.frames_dict_result[key] = 20
                    else:
                        self.frames_dict_result[key] = 10 + self.frames_dict[key + 1][1]
            else:
                self.frames_dict_result[key] = self.frames_dict[key][1] + self.frames_dict[key][2]

        self.ext_result = sum(self.frames_dict_result.values())

class FirstThrow(State):

    def __init__(self, game):
        self.game = game

    def throw(self, result):
        if result == 'X':
            self.game.score += 20
            self.game.frames += 1
        elif result == '0':
            raise ValueError(f'Неверно введены данные - {result}')
        else:
            if result.isdigit():

                self.game.firstthrow_score += int(result)
                # self.game.frame_result += int(result)
                self.game.state = self.game.secondthrow
            elif result == '-':
                self.game.state = self.game.secondthrow

            else:
                raise ValueError(f'Неверно введены данные - {result}')


class SecondThrow(State):

    def __init__(self, game):
        self.game = game

    def throw(self, result):

        if result == '/':
            self.game.score += 15
            self.game.frames += 1
        elif result == '0':
            raise ValueError(f'Неверно введены данные - {result}')

        elif result == '-':
            if self.game.firstthrow_score != 0:
                self.game.score += self.game.firstthrow_score
            self.game.frames += 1
        elif result.isdigit():
            sum = self.game.firstthrow_score + int(result)
            if sum >= 10:
                raise ValueError(f'Неверно введены данные, ожидалось spare, получили результат {sum}')
            else:
                self.game.score += sum

                self.game.frames += 1
                self.game.frame_result += int(result)
        elif result == 'X':
            raise ValueError(f'Неверно введены данные во втором броске - {result}')
        #  а тут могут быть неверные данные? X например?
        self.game.firstthrow_score = 0
        self.game.state = self.game.firstthrow
        if self.game.frame_result > 10:
            raise ValueError(f'Неверно введены данные - счет во фрейме {self.game.frame_result}')
        self.game.frame_result = 0


class FirstThrowExt(State):

    def __init__(self, game):
        self.game = game

    def throw(self, result):
        if result == 'X':
            # self.game.score += 20
            self.game.frames += 1
            self.game.frames_dict[self.game.frames] = {1: 'X', 2: None}
        elif result == '0':
            raise ValueError(f'Неверно введены данные - {result}')
        else:
            if result.isdigit():

                self.game.firstthrow_score += int(result)
                self.game.frame_result += int(result)
                self.game.state = self.game.secondthrow
            elif result == '-':
                self.game.state = self.game.secondthrow

            else:
                raise ValueError(f'Неверно введены данные - {result}')


class SecondThrowExt(State):

    def __init__(self, game):
        self.game = game

    def throw(self, result):

        if result == '/':
            # self.game.score += 15
            self.game.frames += 1
            self.game.frames_dict[self.game.frames] = {1: self.game.firstthrow_score, 2: 'spare'}
        elif result == '0':
            raise ValueError(f'Неверно введены данные - {result}')

        elif result == '-':
            if self.game.firstthrow_score != 0:
                # self.game.score += self.game.firstthrow_score
                self.game.frames += 1
                self.game.frames_dict[self.game.frames] = {1: self.game.firstthrow_score, 2: 0}
            self.game.frames += 1
            self.game.frames_dict[self.game.frames] = {1: 0, 2: 0}

        elif result.isdigit():
            sum = self.game.firstthrow_score + int(result)
            if sum >= 10:
                raise ValueError(f'Неверно введены данные, ожидалось spare, получили результат {sum}')
            else:
                # self.game.score += sum

                self.game.frames += 1
                self.game.frames_dict[self.game.frames] = {1: self.game.firstthrow_score, 2: int(result)}
                self.game.frame_result += int(result)
        elif result == 'X':
            raise ValueError(f'Неверно введены данные во втором броске - {result}')
        #  а тут могут быть неверные данные? X например?
        self.game.firstthrow_score = 0
        self.game.state = self.game.firstthrow
        if self.game.frame_result > 10:
            raise ValueError(f'Неверно введены данные - счет во фрейме {self.game.frame_result}')
        self.game.frame_result = 0


def get_score(game, game_result):
    for result in game_result:
        game.throw(result)
    if game.frames == 10:
        if game.rules == 'internal':
            return game.score
        else:
            game.get_ext_score()
            return game.ext_result

    else:
        raise ValueError('Количество фреймов должно быть равно 10')


if __name__ == '__main__':
    game = Game(rules='ext')
    # get_score(game, '3532X332/3/62--XXX')  #  тут 11 фреймов и код работает
    # get_score(game, '5500X332/3/62--XX')  #  сумма очков за один фрейм не должна превышать 9
    #  0 - должен вызывать ошибку (в нашем случае такая информация кодируется через "-")
    # get_score(game, '532X332/3/62--62X')  #  тут 10 и код не работает, почему?
    print(get_score(game, '5311X332/3/62--XX'))
    #  сумма очков за один фрейм не должна превышать 9
    #  0 - должен вызывать ошибку (в нашем случае такая информация кодируется через "-")
    #  55 - фрейм с ошибкой, должен быть 5/ если все 10 кеглей сбиты
    #  если в строке 55 - значит сформирована строка неправильно и мы должны будем об этом сообщить
    # тому, кто строку вводит
