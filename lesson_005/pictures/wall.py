# -*- coding: utf-8 -*-


import simple_draw as sd
start_point_x = 300
start_point_y = 50
top_x = 750
top_y = 400
right_top = sd.get_point(1200, start_point_y)
left_bottom = sd.get_point(0, 0)
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

point=sd.get_point(start_point_x-100,top_y)
def roof(point=point, angle=0):
    end = point

    v1 = sd.get_vector(start_point=point, angle=angle, length=650, width=3)
    v1.draw(color=sd.COLOR_RED)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle +145, length=400, width=3)
    v2.draw(color=sd.COLOR_RED)

    point = v2.end_point

    sd.line(start_point=point, end_point=end, width=3,color=sd.COLOR_RED)





window_bottom = sd.get_point(start_point_x + 100, start_point_y + 50)
window_top = sd.get_point(top_x - 100, top_y - 50)



