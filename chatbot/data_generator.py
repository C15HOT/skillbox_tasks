import json
import datetime
from pprint import pprint
from random import randint
import calendar
from collections import defaultdict


class Generator:
    def __init__(self):
        self.cities = {'Москва': {'Париж': {}, 'Лондон': {}, 'Нью-Йорк': {}},
                       'Париж': {'Москва': {}, 'Лондон': {}, 'Нью-Йорк': {}, 'Токио': {}},
                       'Лондон': {'Москва': {}, 'Париж': {}, 'Нью-Йорк': {}, 'Токио': {}},
                       'Нью-Йорк': {'Москва': {}, 'Париж': {}, 'Лондон': {}, 'Токио': {}},
                       'Токио': {'Париж': {}, 'Лондон': {}, 'Нью-Йорк': {}}
                       }

    def date_generator(self):

        now_date = datetime.datetime.now()
        days = self.count_of_days(now_date.year, now_date.month + 1)
        date = datetime.datetime(year=now_date.year, month=now_date.month + 1, day=randint(1, days), hour=10, minute=14)
        return date.strftime("%d-%m-%Y")

    def dates_generator(self):
        races = defaultdict()
        for count in range(randint(1, 5)):
            races[randint(0, 999)] = [self.date_generator(), randint(1, 5)]
        return races

    def count_of_days(self, year, month):
        calendar_text = calendar.TextCalendar()
        day_iterator = calendar_text.itermonthdays2(year, month)
        month_days = 0

        for data, weekday in day_iterator:
            if data > 0:
                month_days += 1
        return month_days

    def append_races(self):
        for source, destination in self.cities.items():
            for city, races in destination.items():
                any_races = self.dates_generator()
                for number, race in any_races.items():
                    races[number] = race

    def writer(self, file_name):
        with open(file_name, 'w', encoding='utf-8') as write_file:
            json.dump(self.cities, write_file)


if __name__ == '__main__':
    date = Generator()
    date.append_races()
    date.writer(file_name='date.json')
    with open('date.json', 'r') as read_file:
        loaded_json_file = json.load(read_file)
        pprint(loaded_json_file)
