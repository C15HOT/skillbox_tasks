# -*- coding: utf-8 -*-

# Подземелье было выкопано ящеро-подобными монстрами рядом с аномальной рекой, постоянно выходящей из берегов.
# Из-за этого подземелье регулярно затапливается, монстры выживают, но не герои, рискнувшие спуститься к ним в поисках
# приключений.
# Почуяв безнаказанность, ящеры начали совершать набеги на ближайшие деревни. На защиту всех деревень не хватило
# солдат и вас, как известного в этих краях героя, наняли для их спасения.
#
# Карта подземелья представляет собой json-файл под названием rpg.json. Каждая локация в лабиринте описывается объектом,
# в котором находится единственный ключ с названием, соответствующем формату "Location_<N>_tm<T>",
# где N - это номер локации (целое число), а T (вещественное число) - это время,
# которое необходимо для перехода в эту локацию. Например, если игрок заходит в локацию "Location_8_tm30000",
# то он тратит на это 30000 секунд.
# По данному ключу находится список, который содержит в себе строки с описанием монстров а также другие локации.
# Описание монстра представляет собой строку в формате "Mob_exp<K>_tm<M>", где K (целое число) - это количество опыта,
# которое получает игрок, уничтожив данного монстра, а M (вещественное число) - это время,
# которое потратит игрок для уничтожения данного монстра.
# Например, уничтожив монстра "Boss_exp10_tm20", игрок потратит 20 секунд и получит 10 единиц опыта.
# Гарантируется, что в начале пути будет две локации и один монстр
# (то есть в коренном json-объекте содержится список, содержащий два json-объекта, одного монстра и ничего больше).
#
# На прохождение игры игроку дается 123456.0987654321 секунд.
# Цель игры: за отведенное время найти выход ("Hatch")
#
# По мере прохождения вглубь подземелья, оно начинает затапливаться, поэтому
# в каждую локацию можно попасть только один раз,
# и выйти из нее нельзя (то есть двигаться можно только вперед).
#
# Чтобы открыть люк ("Hatch") и выбраться через него на поверхность, нужно иметь не менее 280 очков опыта.
# Если до открытия люка время заканчивается - герой задыхается и умирает, воскрешаясь перед входом в подземелье,
# готовый к следующей попытке (игра начинается заново).
#
# Гарантируется, что искомый путь только один, и будьте аккуратны в рассчетах!
# При неправильном использовании библиотеки decimal человек, играющий с вашим скриптом рискует никогда не найти путь.
#
# Также, при каждом ходе игрока ваш скрипт должен запоминать следущую информацию:
# - текущую локацию
# - текущее количество опыта
# - текущие дату и время (для этого используйте библиотеку datetime)
# После успешного или неуспешного завершения игры вам необходимо записать
# всю собранную информацию в csv файл dungeon.csv.
# Названия столбцов для csv файла: current_location, current_experience, current_date
#
#
# Пример взаимодействия с игроком:
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло времени: 00:00
#
# Внутри вы видите:
# — Вход в локацию: Location_1_tm1040
# — Вход в локацию: Location_2_tm123456
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали переход в локацию Location_2_tm1234567890
#
# Вы находитесь в Location_2_tm1234567890
# У вас 0 опыта и осталось 0.0987654321 секунд до наводнения
# Прошло времени: 20:00
#
# Внутри вы видите:
# — Монстра Mob_exp10_tm10
# — Вход в локацию: Location_3_tm55500
# — Вход в локацию: Location_4_tm66600
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали сражаться с монстром
#
# Вы находитесь в Location_2_tm0
# У вас 10 опыта и осталось -9.9012345679 секунд до наводнения
#
# Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!
#
# У вас темнеет в глазах... прощай, принцесса...
# Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)
# Ну, на этот-то раз у вас все получится! Трепещите, монстры!
# Вы осторожно входите в пещеру... (текст умирания/воскрешения можно придумать свой ;)
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло уже 0:00:00
# Внутри вы видите:
#  ...
#  ...
#
# и так далее...
import re
import json
from decimal import Decimal, getcontext
import csv
import datetime

getcontext().prec = 50
remaining_time = '123456.0987654321'
# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date']
status = {'location': 'Location_0_tm0', 'exp': 0, 'timeleft': remaining_time, 'game_time': 0}
location_pattern = r'Location_\d\w|Location_B\d\w|Hatch\w'
monster_pattern = r'Mob_exp\d{2,3}_tm\d|Boss\d{3}_exp\d{2,3}_tm\d|Boss_exp\d{3}_tm\d\w'

time_pattern = r'tm\d{0,10}\w'
exp_pattern = r'exp\d{1,3}\w'
number_pattern = r'\d{1,10}'

with open('rpg.json', 'r') as read_file:
    loaded_json_file = json.load(read_file)

current_location = 'Location_0_tm0'
path_location = loaded_json_file[current_location]

json_data = json.dumps(loaded_json_file)
with open('log.csv', 'a', newline='') as out_csv:
    writer = csv.writer(out_csv)  # <_csv.writer object at 0x03B0AD80>
    writer.writerow(field_names)


def find_location(current_location):
    locations = []
    for item in current_location:
        if isinstance(item, dict):
            for key, _ in item.items():
                location = re.findall(location_pattern, key)
                if location:
                    locations.append(key)
    return locations


def find_monster(current_location):
    monsters = []
    for item in current_location:
        if isinstance(item, str):
            monster = re.findall(monster_pattern, item)
            if monster:
                monsters.append(item)
    return monsters


def attack(monster):
    time = re.findall(time_pattern, monster)
    pure_time = re.findall(number_pattern, str(time))
    exp = re.findall(exp_pattern, monster)
    pure_exp = re.findall(number_pattern, str(exp))
    return pure_time[0], pure_exp[0]


def change_location(location, path):
    for item in path:
        if location in item:
            if location == 'Hatch_tm159.098765432':
                if status['exp'] >= 280:
                    time = re.findall(time_pattern, location)
                    pure_time = re.findall(number_pattern, str(time))
                    index = path.index(item)
                    new_path = path[index][location]
                    status['location'] = location
                    return new_path, pure_time[0]
                else:
                    print('У вас недостаточно опыта для открытия люка, нужно 280 \n')
                    time = re.findall(time_pattern, location)
                    pure_time = re.findall(number_pattern, str(time))
                    return path, pure_time[0]
            else:
                time = re.findall(time_pattern, location)
                pure_time = re.findall(number_pattern, str(time))
                index = path.index(item)
                new_path = path[index][location]
                status['location'] = location
                return new_path, pure_time[0]


def start():
    global current_location, path_location, json_data, remaining_time, status, stat
    while True:

        log(stat=[status['location'], status['exp'], datetime.datetime.now()])
        if status['location'] == 'Hatch_tm159.098765432':
            print('Вы нашли выход, победа')
            log(stat=[status['location'], status['exp'], datetime.datetime.now()])
            stat = field_names
            break
        if Decimal(status['timeleft']) <= Decimal('0'):
            print('Вы не успели открыть люк!!! НАВОДНЕНИЕ!!!')
            print('Игра начинается заново \n')
            log(stat=[status['location'], status['exp'], datetime.datetime.now()])
            stat = field_names
            restart()
        print(f"Вы находитесь в локации {status['location']}")
        print(f"У вас {status['exp']} опыта, {status['timeleft']} секунд до наводнения")
        print(f"Прошло времени {status['game_time']} ")
        locations = find_location(path_location)
        monsters = find_monster(path_location)
        print(f"Внутри вы видите: ")
        for location in locations:
            print(f'Вход в локацию {location}')
        for monster in monsters:
            print(f'Монстра {monster}')

        print('Выберите действие:')
        print('1. Атаковать монстра')
        print('2. Перейти в другую локацию')
        print('3. Сдаться')

        event = input()

        if event == '1':
            print('Выберите монстра')
            select = input()
            if int(select) <= len(monsters):
                time, exp = attack(monsters[int(select) - 1])
                remaining_time = Decimal(remaining_time) - Decimal(time)
                status['timeleft'] = remaining_time
                status['game_time'] += Decimal(time)
                status['exp'] += Decimal(exp)
                index = path_location.index(monsters[int(select) - 1])
                path_location.pop(index)
                monsters.pop(int(select) - 1)
            else:
                print('Вы ввели некорректное число \n')

        elif event == '2':
            print('Введите номер локации')
            change = input()
            if int(change) <= len(locations):

                path_location, time = change_location(locations[int(change) - 1], path_location)
                remaining_time = Decimal(remaining_time) - Decimal(time)
                status['timeleft'] = remaining_time
                status['game_time'] += Decimal(time)
            else:
                print('Вы ввели некорректное число \n')

        elif event == '3':
            log(stat=[status['location'], status['exp'], datetime.datetime.now()])
            stat = field_names
            restart()
        else:
            print('Вы ввели некорректное число \n')


def log(stat):
    with open('log.csv', 'a', newline='') as out_csv:
        writer = csv.writer(out_csv)  # <_csv.writer object at 0x03B0AD80>
        writer.writerow(stat)


def restart():
    global status, remaining_time, path_location, current_location
    with open('rpg.json', 'r') as read_file:
        loaded_json_file = json.load(read_file)
    current_location = 'Location_0_tm0'
    path_location = loaded_json_file[current_location]
    remaining_time = '123456.0987654321'
    status = {'location': 'Location_0_tm0', 'exp': 0, 'timeleft': remaining_time, 'game_time': 0}
    start()


if __name__ == '__main__':
    start()
# Учитывая время и опыт, не забывайте о точности вычислений!
