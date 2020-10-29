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
#  В модулях должны быть только необходимые импорты и функции
#  Код, который лежит вне функций - надо убрать, особенно sd.pause
#  При импорте модуля - весь код из него будет выполняться
#  Ещё до того, как мы начнём вызывать эти функции тут.
#  А пауза так вообще не даст выполняться коду дальше.
from lesson_005.pictures import wall
import simple_draw as sd
from lesson_005.pictures import tree
from lesson_005.pictures.tree import tree_point
from lesson_005.pictures.wall import window_bottom, window_top,start_point_x,start_point_y,right_top,left_bottom,top_y,top_x

from lesson_005.pictures import rainbow
from lesson_005.pictures import smile
from lesson_005.pictures import snow
#  Тут должны остаться только вызовы функций рисования элементов картины,
#  без лишних вспомогательных команд вроде создания точек и циклов

sd.resolution=(1200,700)

wall.wall(start_point_x=start_point_x, start_point_y=start_point_y, top_x=top_x, top_y=top_y)
sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_DARK_ORANGE, width=0)
sd.rectangle(left_bottom=window_bottom, right_top=window_top, color=sd.background_color, width=0)
sd.rectangle(left_bottom=window_bottom, right_top=window_top, color=sd.COLOR_YELLOW, width=2)



tree.draw_branches(start_point=tree_point,angle=90,length=80)

rainbow.rainbow_print()

smile.smile(500,150,color=sd.COLOR_PURPLE)
wall.roof()
snow.snowfall()

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
sd.pause()