# -*- coding: utf-8 -*-

# В очередной спешке, проверив приложение с прогнозом погоды, вы выбежали
# навстречу ревью вашего кода, которое ожидало вас в офисе.
# И тут же день стал хуже - вместо обещанной облачности вас встретил ливень.

# Вы промокли, настроение было испорчено, и на ревью вы уже пришли не в духе.
# В итоге такого сокрушительного дня вы решили написать свою программу для прогноза погоды
# из источника, которому вы доверяете.

# Для этого вам нужно:

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}

# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю, должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.

# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database
import argparse

#  каждый класс стоит выделить в отдельный модуль
#  и добавить в конце модуля проверку работы текущего класса
#  (чтобы убедиться, что каждый класс может выполнять свои функции независимо от других)

#  просто открытый код оставлять нельзя, надо предполагать, что нашу программу захотят импортировать
#  и использовать в своих программах
#  значит весь код должен быть внутри классов и функций
#  тут например стоит сформировать класс-менеджер, который будет получать какой-то запрос от пользователя
# и, управляя другими классами-рабочими, будет выполнять этот запрос.
# И выводить информацию о том, какие действия он смог выполнить, а какие нет.

from image_maker import ImageMaker
from lesson_016.databaseupdater import DatabaseUpdater
from weather_maker import WeatherMaker


class Parser:  # этот класс стоит расширить до менеджера
    #  чтобы он полностью выполнял организационную часть работы
    # 1) получал ввод пользователя
    #  2) обрабатывал его
    #  3) выполнял запросы через классы-работники
    #  4) формировал результат
    def parser_func(self):
        parser = argparse.ArgumentParser()

        parser.add_argument('--days_count', default=1, type=int)
        parser.add_argument('--date_low', type=str)
        parser.add_argument('--date_high', type=str)
        parser.add_argument('--create_ticket', default=False, type=bool)

        args = parser.parse_args()
        return args

    def handler(self):
        args = self.parser_func()

        parse = WeatherMaker()
        parse.parse(days=args.days_count)

        data = parse.data
        img = ImageMaker()
        if args.create_ticket:
            img.put_data(data=data)
        db = DatabaseUpdater()
        db.set_info(data=parse.data)
        db.get_info(date_low=args.date_low, date_high=args.date_high)

        self.dialog(parse=parse, img=img, db=db)

    def dialog(self, parse, img, db):
        x = True
        while x:
            print('Вам доступны следующие действия: \n'
                  '1. Обновить данные о погоде \n'
                  '2. Создать открытки \n'
                  '3. Узнать погоду \n'
                  '4. Выход \n'
                  'Введите номер действия \n')
            user_input = input()
            if user_input == '1':
                print('Введите количество дней: \n')
                days = input()
                if int(days) >= 10:
                    days = 10
                data = parse.parse(int(days))
                db.set_info(data)
            elif user_input == '2':
                print('Введите количество дней: \n')
                days = input()
                if int(days) >= 10:
                    days = 10
                data = parse.parse(int(days))
                img.put_data(data)
            elif user_input == '3':
                print('Вывести все доступные данные? Введите "Да" или "Нет"\n')
                answer = input()
                if answer.lower() == 'да':
                    self.data_print(db.get_info())
                else:

                    print('Введите дату начала: \n')
                    date_low = input()
                    print('Введите дату конца: \n')
                    date_high = input()
                    self.data_print(db.get_info(date_low=date_low, date_high=date_high))
            else:
                x = False

    def data_print(self, list):
        for data in list:
            print(data)


if __name__ == '__main__':
    parser = Parser()
    parser.handler()
#зачёт!