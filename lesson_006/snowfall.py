import simple_draw as sd
N=5
start_pull_of_y_coordinate = [300]*N
start_pull_of_x_coordinate = list(range(1,N*100,100))
points=[]
step=10
def make_snawflake():
    for i in range(N):
        point=sd.get_point(start_pull_of_x_coordinate[i], start_pull_of_y_coordinate[i])
        points.append(point)


def draw_snowflake():
    for i in range(N):
        sd.snowflake(center=points[i], length=50)

def shift_snowflake():
    for i in range(N):
        points[i]=sd.get_point(start_pull_of_x_coordinate[i],start_pull_of_y_coordinate[i]-step)

def number_of_snowflake():
    pass

def del_snowflake():
    pass
make_snawflake()
draw_snowflake()
shift_snowflake()
draw_snowflake()

sd.pause()