import peewee


database_proxy= peewee.DatabaseProxy()
# TODO не забывайте про стиль кода
class BaseModel(peewee.Model):
    class Meta:
        database = database_proxy

class Weather(BaseModel):

    date = peewee.DateTimeField(unique=True)
    night = peewee.CharField()
    morning = peewee.CharField()
    afternoon = peewee.CharField()
    evening = peewee.CharField()

