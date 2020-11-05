import simple_draw as sd

N = 5
start_pull_of_y_coordinate = [300] * N
start_pull_of_x_coordinate = list(range(1, N * 100, 100))
pure_points = []
points = []
step = 10
del_list=[]

def make_snawflake():
    for i in range(N):
        pure_points.append([start_pull_of_x_coordinate[i], start_pull_of_y_coordinate[i]])

        point = sd.get_point(pure_points[i][0], pure_points[i][1])

        points.append(point)


def draw_snowflake(color=sd.COLOR_WHITE):
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
            return num


def del_snowflake():
    if len(del_list)!=0:
        for i in del_list:
            pure_points.pop(i)

