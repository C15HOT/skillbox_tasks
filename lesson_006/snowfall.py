import simple_draw as sd

N = 5
# TODO список с 300 можно по сути убрать и добавлять в pure_points просто число 300
start_pull_of_y_coordinate = [300] * N
# TODO так же и тут, можно убрать этот список, и вместо икса добавлять i*100
start_pull_of_x_coordinate = list(range(1, N * 100, 100))
pure_points = []
points = []
step = 10
del_list=[]

def make_snawflake():  # TODO N сюда хорошо было бы передавать параметром
    for i in range(N):
        pure_points.append([start_pull_of_x_coordinate[i], start_pull_of_y_coordinate[i]])
        point = sd.get_point(pure_points[i][0], pure_points[i][1])

        points.append(point)


def draw_snowflake(color=sd.COLOR_WHITE):
    # TODO Тут и далее лучше использовать for index, y in enumerate(coordinate_y)
    for i in range(N):
        sd.snowflake(center=points[i], length=50, color=color)


def shift_snowflake():
    for i in range(N):
        pure_points[i][1] -= step
        points[i] = sd.get_point(pure_points[i][0], pure_points[i][1])


def number_of_snowflake():
    for num, coord_y in enumerate(pure_points):
        if coord_y[1] < 50:
            del_list.append(num)
            return num  # TODO ретурн здесь прервёт выполнение цикла и функции
    # TODO нужно вынести его из цикла


def del_snowflake():
    if len(del_list)!=0:  # TODO эту проверку можно убрать
        for i in del_list:  # TODO цикл по пустому списку просто не начнётся
            pure_points.pop(i)
    # TODO Полученные индексы сперва стоит развернуть - чтобы удалять снежинки, начиная с конца.
    # TODO Иначе сдвиг списка будет изменять индексы и мы удалим что-нибудь не то
