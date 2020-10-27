# -*- coding: utf-8 -*-

import simple_draw as sd



N = 20


length = []

start_pull_of_y_coordinate = list(range(700, 500, -10))
start_pull_of_x_coordinate = list(range(30, 1230, 60))

y_pull = []
y_pull2 = []
for _ in range(N):
    length.append(sd.random_number(a=10, b=50))

while True:
    sd.start_drawing()
    for i, x in enumerate(start_pull_of_x_coordinate):
        sdvig = sd.random_number(a=-20, b=20)

        point = sd.get_point(x, start_pull_of_y_coordinate[i])

        sd.snowflake(center=point, length=length[i], color=sd.background_color)
        start_pull_of_y_coordinate[i] -= 10
        start_pull_of_x_coordinate[i] += sdvig


        point = sd.get_point(start_pull_of_x_coordinate[i], start_pull_of_y_coordinate[i])

        if start_pull_of_y_coordinate[i] < 50:

            start_pull_of_y_coordinate[i] += 600



        sd.snowflake(center=point, length=length[i])

    sd.finish_drawing()
    sd.sleep(0.05)
    if sd.user_want_exit():
        break
sd.pause()

