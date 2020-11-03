import simple_draw as sd
N=5
start_pull_of_y_coordinate = [300]*N
start_pull_of_x_coordinate = list(range(1,N*100,100))


def make_snawflake():
    for i in range(N):
        point = sd.get_point(start_pull_of_x_coordinate[i], start_pull_of_y_coordinate[i])
        sd.snowflake(center=point, length=50)

def draw_snowflake():


def shift_snowflake():
    pass

def number_of_snowflake():
    pass

def del_snowflake():
    pass
make_snawflake()
sd.pause()