from abc import ABCMeta, abstractmethod


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

        self.last_result = None

        self.first_throw_result = 0
        self.second_throw_result = 0
        self.third_throw_result = 0

    def throw(self, result):
        self.state.throw(result)


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
        sum = 0
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
        if self.game.last_result is None:
            if result == 'X':
                self.game.first_throw_result = 10
                self.game.frames += 1
                self.game.last_result = 10
                self.game.state = self.game.secondthrow

            elif result == '0':
                raise ValueError(f'Неверно введены данные - {result}')
            else:

                if result.isdigit():
                    self.game.first_throw_result += int(result)
                    self.game.state = self.game.secondthrow
                elif result == '-':
                    self.game.state = self.game.secondthrow
                else:
                    raise ValueError(f'Неверно введены данные - {result}')




class SecondThrowExt(State):

    def __init__(self, game):
        self.game = game

    def throw(self, result):

class ThirdThrowext(State):

    def __init__(self, game):
        self.game = game

    def throw(self, result):



def get_score(game, game_result):
    for result in game_result:
        game.throw(result)
    if game.frames == 10:
        return game.score

    else:
        raise ValueError('Количество фреймов должно быть равно 10')


if __name__ == '__main__':
    game = Game()
    # get_score(game, '3532X332/3/62--XXX')  #  тут 11 фреймов и код работает
    # get_score(game, '5500X332/3/62--XX')  #  сумма очков за один фрейм не должна превышать 9
    #  0 - должен вызывать ошибку (в нашем случае такая информация кодируется через "-")
    # get_score(game, '532X332/3/62--62X')  #  тут 10 и код не работает, почему?
    get_score(game, '5311X332/3/62--XX')
    #  сумма очков за один фрейм не должна превышать 9
    #  0 - должен вызывать ошибку (в нашем случае такая информация кодируется через "-")
    #  55 - фрейм с ошибкой, должен быть 5/ если все 10 кеглей сбиты
    #  если в строке 55 - значит сформирована строка неправильно и мы должны будем об этом сообщить
    # тому, кто строку вводит
