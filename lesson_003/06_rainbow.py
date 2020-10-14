# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
i = 0

for color in rainbow_colors:
    start = sd.get_point(50 + i, 50)
    end = sd.get_point(350 + i, 450)
    sd.line(start_point=start, end_point=end, color=color, width=4)
    i += 5

# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
i = 0
for color in rainbow_colors:
    center = sd.get_point(300, -200)
    sd.circle(center_position=center, radius=500 - i, color=color, width=20)
    i += 20

sd.pause()
#зачёт!