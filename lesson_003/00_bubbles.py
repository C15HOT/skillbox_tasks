# -*- coding: utf-8 -*-
import random
import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(200,200)
radius = 100
for _ in range(3):
    sd.circle(center_position=point, radius=radius)
    radius += 5
# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет

def print_buble(point,step,color,amount):
    radius = 10
    for _ in range(amount):
        sd.circle(center_position=point, radius=radius, color=color)
        radius = radius + step
step = 10
amount = 10
point = sd.get_point(300,300)
color = (255,0,0)
print_buble(point,step,color,amount)

# Нарисовать 10 пузырьков в ряд

y = 150
for x in range(100,1001,100):
    point=sd.get_point(x,y)
    sd.circle(center_position=point,radius=radius,color=(0,255,0))



# Нарисовать три ряда по 10 пузырьков


for x in range(200,1101,100):
    for y in range(300,501,100):
        point=sd.get_point(x,y)
        sd.circle(center_position=point,radius=10,color=(255,255,0))

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(100):
    point=sd.random_point()
    step = random.randint(1,10)
    color = sd.random_color()
    print_buble(point,step,color,1)


sd.pause()
