# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
# length = []
#
# start_pull_of_y_coordinate = list(range(500, 700, 10))
# start_pull_of_x_coordinate = list(range(0, 1200, 60))
# for _ in range(N):
#     length.append(sd.random_number(a=10, b=101))
#
# while True:
#     sd.clear_screen()
#     for i, x in enumerate(start_pull_of_x_coordinate):
#
#         point = sd.get_point(x, start_pull_of_y_coordinate[i])
#
#         sd.snowflake(center=point, length=length[i])
#         start_pull_of_y_coordinate[i] -= 10
#
#         if start_pull_of_y_coordinate[i] < 10:
#
#             break  # подумайте, что ещё можно сделать с упавшими снежинками - оставить лежать на земле, пока не представляю как
#
#     sd.sleep(0.05)
#     if sd.user_want_exit():
#         break
# sd.pause()

# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       изменить координата_у и запомнить её в списке по индексу
#       создать точку отрисовки снежинки по координатам
#       нарисовать снежинку белым цветом в этой точке
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла: полная очистка всего экрана - долгая операция.
# - использовать хак для стирания старого положения снежинки:
#       отрисуем её заново на старом месте, но цветом фона (sd.background_color) и она исчезнет!
# - использовать функции sd.start_drawing() и sd.finish_drawing()
#       для начала/окончания отрисовки кадра анимации
# - между start_drawing и finish_drawing библиотека sd ничего не выводит на экран,
#       а сохраняет нарисованное в промежуточном буфере, за счет чего достигается ускорение анимации
# - в момент вызова finish_drawing все нарисованное в буфере разом покажется на экране
#
# Примерный алгоритм ускоренной отрисовки снежинок
#   навсегда
#     начать рисование кадра
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     закончить рисование кадра
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл
length = []

start_pull_of_y_coordinate = list(range(500, 700, 10))
start_pull_of_x_coordinate = list(range(30, 1230, 60))

y_pull = []
for _ in range(N):
    length.append(sd.random_number(a=10, b=101))


while True:
    sd.start_drawing()
    for i, x in enumerate(start_pull_of_x_coordinate):

        point = sd.get_point(x, start_pull_of_y_coordinate[i])
        # start и finish нужно до и после цикла расставлять
        #  чтобы между этими операциями вызывались все функции рисования,
        #  тогда это поможет оптимизировать код

        sd.snowflake(center=point, length=length[i], color=sd.background_color)
        start_pull_of_y_coordinate[i] -= 10

        point = sd.get_point(x, start_pull_of_y_coordinate[i])


        if start_pull_of_y_coordinate[i] < 50:
            y_pull.append(start_pull_of_y_coordinate[i])
            point2 = sd.get_point(x, y_pull[i])
            sd.snowflake(center=point2,length=length[i])
            continue
        sd.snowflake(center=point, length=length[i])
            #  проблема тут в этом условии
            #  из-за него цикл останавливается и следующие снежинки уже не падают
            # чем можно заменить break?
    # Еще не могу разобраться как сделать чтобы каждая снежинка долетала до низа,
    # программа останавливаетяс при попадании
    # вниз первой снежинки, причем сама первая снежинка куда-то проваливается под экран, а остальные останавливаются
    sd.finish_drawing()
    sd.sleep(0.05)
    if sd.user_want_exit():
        break
sd.pause()

# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
