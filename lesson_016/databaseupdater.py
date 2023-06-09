import peewee
from playhouse.db_url import connect
import models
from image_maker import day_handler


#  используйте относительный путь (относительно рабочей директории, без lesson_016)

class DatabaseUpdater:
    def __init__(self):
        self.database = connect('sqlite:///weather.db')
        models.database_proxy.initialize(self.database)

        self.database.create_tables([models.Weather])

    def set_info(self, data):
        #  кстати, если у вас есть столбец уникальных записей (в нашем случае дата)
        #  можно использовать более высокоуровневый метод
        #  https://stackoverflow.com/questions/33485312/insert-or-update-a-peewee-record-in-python
        #  можно даже сочетать http://docs.peewee-orm.com/en/latest/peewee/api.html#Model.insert_many
        #  с методом http://docs.peewee-orm.com/en/latest/peewee/api.html?highlight=on%20conflict#Insert.on_conflict
        for day, values in data.items():
            date = day_handler(day).strftime("%Y-%m-%d")

            #  При добавлении новых данных в базу попробуйте использовать метод get_or_create
            #  Он либо создаст новую запись, либо укажет на то, что запись уже существует
            #  По возвращенному айди можно будет обновить старую запись, вместо создания новой.
            #  Обратите внимание на описание этого метода и на то, что он возвращает при использовании
            # http://docs.peewee-orm.com/en/latest/peewee/api.html#Model.get_or_create
            #  Returns:
            #  Tuple of Model instance and boolean indicating if a new object was created.
            #  Т.е. возвращается кортеж с ID элемента, который был найден или был создан
            #  И возвращается True/False объект, который говорит о том, был ли объект создан
            #  Если объект не был создан - его хорошо было бы обновить по вернувшемуся ID
            #  Принцип примерно следующий:
            # for data in data_to_save:
            # Сперва получаем данные из get_or_create по одному из полей(в данном случае по дате)
            #     weather, created = Weather.get_or_create(
            #         date=data['date'],
            #  В defaults указываются остальные данные, которые будут использованы при создании записи
            #         defaults={'temperature': data['temperature'], 'pressure': data['pressure'],
            #                   'conditions': data['conditions'], 'wind': data['wind']})
            #     if not created:
            #  Если запись не создана - обновляем её
            #         query = Weather.update(temperature=data['temperature'], pressure=data['pressure'],
            #                                conditions=data['conditions'], wind=data['wind']).where(Weather.id == weather.id)
            #         query.execute()
            # weather, created = models.Weather.get_or_create(
            #     date=date,
            #     defaults={
            #         'night': f"{values['Ночь'][0][0]}, Температура: {values['Ночь'][1].replace('−', '-')}",
            #         'morning': f"{values['Утро'][0][0]}, Температура: {values['Утро'][1].replace('−', '-')}",
            #         'afternoon': f"{values['День'][0][0]}, Температура: {values['День'][1].replace('−', '-')}",
            #         'evening': f"{values['Вечер'][0][0]}, Температура: {values['Вечер'][1].replace('−', '-')}"
            #     })
            # if not created:
            #     query = models.Weather.update(
            #         date=date,
            #         night=f"{values['Ночь'][0][0]}, Температура: {values['Ночь'][1].replace('−', '-')}",
            #         morning=f"{values['Утро'][0][0]}, Температура: {values['Утро'][1].replace('−', '-')}",
            #         afternoon=f"{values['День'][0][0]}, Температура: {values['День'][1].replace('−', '-')}",
            #         evening=f"{values['Вечер'][0][0]}, Температура: {values['Вечер'][1].replace('−', '-')}"
            #     )
            #     query.execute()

            result = (models.Weather
                      .insert(date=date,
                              night=f"{values['Ночь'][0][0]}, Температура: {values['Ночь'][1].replace('−', '-')}",
                              morning=f"{values['Утро'][0][0]}, Температура: {values['Утро'][1].replace('−', '-')}",
                              afternoon=f"{values['День'][0][0]}, Температура: {values['День'][1].replace('−', '-')}",
                              evening=f"{values['Вечер'][0][0]}, Температура: {values['Вечер'][1].replace('−', '-')}")
                      .on_conflict('replace')
                      .execute())

    def get_info(self, date_low=None, date_high=None):
        # нужно убрать дублирование кода
        #  + этот метод должен формировать список прогнозов и возвращать его
        #  печатью пусть занимается менеджер
        list = []
        if (date_low is not None) and (date_high is not None):
            range_low = date_low
            range_high = date_high

        else:
            range_low = peewee.fn.MIN(models.Weather).alias('date')
            range_high = peewee.fn.Max(models.Weather).alias('date')

        for weather in models.Weather.select().where((models.Weather.date >= range_low) &
                                                     (models.Weather.date <= range_high)):
            list.append(f'{weather.date}: '
                        f'Ночь: {weather.night},'
                        f' Утро: {weather.morning}, '
                        f'День: {weather.afternoon}, '
                        f'Вечер: {weather.evening}')

        return list
