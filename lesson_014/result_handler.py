from bowling import get_score, Game


def result_hanler(input, output, rules):
    names = []
    results = []
    scores = []
    with open(input, 'r', encoding='utf8') as file:
        with open(output, 'a', encoding='utf8') as ff:
            for line in file:
                if line.startswith('###'):
                    _, __, tour = line.split(' ')
                    ff.write(f'### Tour {tour}')
                    continue
                if line.startswith('winner'):
                    winner = find_winner(scores)
                    if winner is not None:
                        for index in range(len(names)):
                            ff.write('{txt:} {txt2:^15} {txt3:^5}''\n'.format(txt=names[index], txt2=results[index],
                                                                              txt3=scores[index]))
                            # print(names[index], results[index], scores[index])
                        ff.write(f'winner is {names[winner]}\n''\n')
                    else:
                        for index in range(len(names)):
                            ff.write('{txt:} {txt2:^15} {txt3:^5}''\n'.format(txt=names[index], txt2=results[index],
                                                                              txt3=scores[index]))
                        ff.write(f'winner is not defined \n''\n')
                    continue
                if line.isspace():
                    names = []
                    results = []
                    scores = []
                    continue
                try:
                    name, result = line.split('\t')

                    score = get_score(game=Game(rules=rules), game_result=result[:-1])

                    names.append(name)
                    results.append(result[:-1])
                    scores.append(score)
                except ValueError as exc:
                    scores.append(f'Недопустимая комбинация фрейма {exc}')
                    names.append(name)
                    results.append(result[:-1])


def find_winner(scores):
    int_scores = []
    for item in scores:
        if isinstance(item, int):
            int_scores.append(int(item))
    # int_scores = [int(item) for item in scores]
    try:
        max_result = max(int_scores)
        index = scores.index(max_result)
        # index = int_scores.index(max_result)
        return index
    except:
        return None


if __name__ == '__main__':
    result_hanler(input='tournament.txt', output='tournament_result.txt', rules='internal')
