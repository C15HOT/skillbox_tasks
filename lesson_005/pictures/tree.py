import simple_draw as sd

tree_point = sd.get_point(1000, 50)


def draw_branches(start_point, angle, length):
    color = sd.COLOR_YELLOW
    if length < 10:
        return
    if length < 30:
        color = sd.COLOR_GREEN
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)

    v1.draw(color=color)

    next_point = v1.end_point
    next_angle = angle - 30
    next_angle2 = angle + 30
    next_length = length * .75

    draw_branches(start_point=next_point, angle=next_angle, length=next_length)
    draw_branches(start_point=next_point, angle=next_angle2, length=next_length)
