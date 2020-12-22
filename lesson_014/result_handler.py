from bowling import get_score, Game

def result_hanler():
    names = []
    results = []
    scores = []
    with open('tournament.txt', 'r', encoding='utf8') as file:
        for line in file:
            if line.startswith('###'):
                _, __, tour = line.split(' ')
                continue
            if line.startswith('winner'):
                winner = find_winner(scores)
                print(f'### Tour {tour}')
                for index in range(len(names)):
                    print('{txt:} {txt2:^15} {txt3:}'.format(txt=names[index], txt2=results[index], txt3=scores[index]))
                    # print(names[index], results[index], scores[index])
                print(f'winner {names[winner]}')
                continue
            if line.isspace():
                names = []
                results = []
                scores = []
                continue
            try:
                name, result = line.split('\t')

                score = get_score(game=Game(), game_result=result[:-1])

                names.append(name)
                results.append(result)
                scores.append(score)
            except ValueError as exc:
                raise ValueError('Не хватает данных')





def find_winner(scores):
    int_scores = [int(item) for item in scores]
    max_result = max(int_scores)
    index = int_scores.index(max_result)
    return index

if __name__=='__main__':
    result_hanler()
