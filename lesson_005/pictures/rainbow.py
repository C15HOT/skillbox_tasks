import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
i = 0

for color in rainbow_colors:
    center = sd.get_point(300, -200)
    sd.circle(center_position=center, radius=500 - i, color=color, width=20)
    i += 20

sd.pause()