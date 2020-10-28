# -*- coding: utf-8 -*-


import simple_draw as sd

def wall(start_point_x,start_point_y,top_y,top_x):
    COLOR_YELLOW = (255, 255, 0)

    sd.resolution=(1200,700)
    start_point=sd.get_point(start_point_x-50,start_point_y)
    finish_point=sd.get_point(top_x+50,top_y)
    point_x, point_y = 100, 50
    for row, y in enumerate(range(start_point_y, top_y, 50)):
        x0 = -50 if row % 2 == 0 else 0
        for x in range(x0+start_point_x, top_x, 100):
            left = sd.get_point(0 + x, 0 + y)
            right = sd.get_point(point_x + x, point_y + y)
            sd.rectangle(left_bottom=left, right_top=right, color=COLOR_YELLOW, width=1)
    sd.rectangle(left_bottom=start_point, right_top=finish_point, color=COLOR_YELLOW, width=1)




