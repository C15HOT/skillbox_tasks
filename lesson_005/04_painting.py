# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)
# TODO В модулях должны быть только необходимые импорты и функции
# TODO Код, который лежит вне функций - надо убрать, особенно sd.pause
# TODO При импорте модуля - весь код из него будет выполняться
# TODO Ещё до того, как мы начнём вызывать эти функции тут.
# TODO А пауза так вообще не даст выполняться коду дальше.
from pictures import wall
import simple_draw as sd
#from pictures import tree

# TODO Тут должны остаться только вызовы функций рисования элементов картины,
# TODO без лишних вспомогательных команд вроде создания точек и циклов

sd.resolution=(1200,700)
start_point_x=300
start_point_y=50
top_x=750
top_y=400
right_top=sd.get_point(1200,start_point_y)
left_bottom=sd.get_point(0,0)
wall.wall(start_point_x=start_point_x,start_point_y=start_point_y,top_x=top_x,top_y=top_y)
sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_DARK_ORANGE, width=0)
window_bottom=sd.get_point(start_point_x+100,start_point_y+50)
window_top=sd.get_point(top_x-100,top_y-50)
sd.rectangle(left_bottom=window_bottom, right_top=window_top, color=sd.background_color, width=0)
sd.rectangle(left_bottom=window_bottom, right_top=window_top, color=sd.COLOR_YELLOW, width=2)

sun=sd.get_point(100,600)
sd.circle(center_position=sun, radius=50, color=sd.COLOR_YELLOW, width=0)
angle=0
for angle in range(0,360,20):
    v1 = sd.get_vector(start_point=sun, angle=angle+angle, length=100, width=3)
    v1.draw()
#tree_point=sd.get_point(700,0)
#tree.draw_branches(start_point=tree,angle=0,length=100)

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
sd.pause()