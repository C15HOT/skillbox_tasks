
import simple_draw as sd
def draw_branches(start_point, angle, length):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
    v1.draw()

    next_point = v1.end_point
    next_angle = angle - 30
    next_angle2 = angle +30
    next_length = length * .75
    draw_branches(start_point=next_point, angle=next_angle, length=next_length)
    draw_branches(start_point=next_point, angle=next_angle2, length=next_length)



sd.pause()