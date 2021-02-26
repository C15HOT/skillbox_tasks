import peewee
from playhouse.db_url import connect
import datetime


# database = peewee.SqliteDatabase('weather.db')
database = connect('sqlite:///weather.db')

class BaseTable(peewee.Model):

    class Meta:
        database = database


class Weather(BaseTable):

    date = peewee.DateTimeField()
    night = peewee.CharField()
    morning = peewee.CharField()
    afternoon = peewee.CharField()
    evening = peewee.CharField()


database.create_tables([Weather])

# data = Weather.create(
#     date=datetime.date(year=datetime.date.today().year, month=datetime.date.today().month, day=datetime.date.today().day),
#     night='Пасмурно, -10',
#     morning='Ясно, +4',
#     afternoon='Снег, -3',
#     evening='Ясно, +4',
# )

for weather in Weather.select():
    print(f'{weather.date}: '
          f'Ночь: {weather.night}, Утро: {weather.morning}, День: {weather.afternoon}, Вечер: {weather.evening}')