import peewee
import datetime


database = peewee.SqliteDatabase('weather.db')


class BaseTable(peewee.Model):

    class Meta:
        database = database


class Weather(BaseTable):

    date = peewee.DateTimeField()
    night = peewee.CharField()
    morning = peewee.CharField()
    afternoon = peewee.CharField()
    evening = peewee.CharField()


database.create_tables(Weather)
