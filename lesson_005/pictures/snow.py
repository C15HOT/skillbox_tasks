# -*- coding: utf-8 -*-

import simple_draw as sd



N = 3


length = []

start_pull_of_y_coordinate = list(range(700, 721, 10))
start_pull_of_x_coordinate = list(range(20, 81, 30))
sun=sd.get_point(100,600)
y_pull = []
y_pull2 = []
for _ in range(N):
    length.append(sd.random_number(a=10, b=30))
def snowfall():
    while True:
        sd.start_drawing()
        for i, x in enumerate(start_pull_of_x_coordinate):
            sdvig = sd.random_number(a=-5, b=5)

            point = sd.get_point(x, start_pull_of_y_coordinate[i])

            sd.snowflake(center=point, length=length[i], color=sd.background_color)
            start_pull_of_y_coordinate[i] -= 10
            start_pull_of_x_coordinate[i] += sdvig


            point = sd.get_point(start_pull_of_x_coordinate[i], start_pull_of_y_coordinate[i])

            if start_pull_of_y_coordinate[i] < 75:

                start_pull_of_y_coordinate[i] += 600



            sd.snowflake(center=point, length=length[i])
        sd.circle(center_position=sun, radius=50, color=sd.COLOR_YELLOW, width=0)
        angle = 0
        for angle in range(0, 360, 20):
            v1 = sd.get_vector(start_point=sun, angle=angle + angle, length=100, width=3)
            v1.draw()
        sd.finish_drawing()
        sd.sleep(0.05)
        if sd.user_want_exit():
            break


