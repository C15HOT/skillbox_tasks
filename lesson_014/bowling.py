from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    @abstractmethod
    def throw(self, result):
        pass


class Game:

    def __init__(self):
        self.score = 0
        self.firstthrow = FirstThrow(self)
        self.secondthrow = SecondThrow(self)
        self.state = self.firstthrow
        self.frames = 0
        self.firstthrow_score = 0  # запоминание результата первого броска

    def throw(self, result):
        self.state.throw(result)


class FirstThrow(State):

    def __init__(self, game):
        self.game = game

    def throw(self, result):
        if result == 'X':
            self.game.score += 20
            self.game.frames += 1
        else:
            if result.isdigit():
                self.game.firstthrow_score += int(result)
                self.game.state = self.game.secondthrow
            elif result == '-':
                self.game.state = self.game.secondthrow
            else:
                raise ValueError('Неверно введены данные')


class SecondThrow(State):

    def __init__(self, game):
        self.game = game

    def throw(self, result):
        if result == '/':
            self.game.score += 15
            self.game.frames += 1
        elif result == '-':
            if self.game.firstthrow_score != 0:
                self.game.score += self.game.firstthrow_score
                self.game.frames += 1
        elif result.isdigit():
            self.game.score += int(result) + self.game.firstthrow_score
            self.game.frames += 1
        self.game.firstthrow_score = 0
        self.game.state = self.game.firstthrow


def get_score(game, game_result):
    for result in game_result:
        game.throw(result)
    if game.frames == 10:
        print(f'Количество очков для результатов {game_result} - {game.score}')
    else:
        raise ValueError('Количество фреймов должно быть равно 10')


if __name__ == '__main__':
    game = Game()
    get_score(game, 'X4/34-4')
