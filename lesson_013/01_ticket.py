# -*- coding: utf-8 -*-
import argparse
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

class TicketFiller:

    def __init__(self, fio, from_, to, date, font=None, ticket=None, save_to=None):
        self.fio = fio
        self.from_ = from_
        self.to = to
        self.date = date
        self.ticket = os.path.join('images', 'ticket_template.png') if ticket is None else ticket
        self.save_to = save_to
        if font is None:
            self.font = os.path.join('fonts', 'AGENCYR.TTF')
        else:
            self.font = font

    def make_ticket(self):
        image = Image.open(self.ticket)
        width, hight = image.size
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('arial.ttf', size=20)
        fio_y = width - 493 - (10 + font.size) * 2
        from_y = width - 423 - (10 + font.size) * 2
        to_y = width - 357 - (10 + font.size) * 2
        date_y = width - 357 - (10 + font.size) * 2
        fio_message = f'{self.fio}'
        from_message = f'{self.from_}'
        to_message = f'{self.to}'
        date_message = f'{self.date}'
        draw.text((45, fio_y), fio_message, font=font, fill=ImageColor.colormap['black'])
        draw.text((45, from_y), from_message, font=font, fill=ImageColor.colormap['black'])
        draw.text((45, to_y), to_message, font=font, fill=ImageColor.colormap['black'])
        draw.text((280, date_y), date_message, font=font, fill=ImageColor.colormap['black'])
        self.save_to = self.save_to if self.save_to else 'ticket.png'
        image.save(self.save_to)
        print(f'Ticket saved to {self.save_to}')


class Parser:
    def parser_func(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('fio', type=str)
        parser.add_argument('from_', type=str)
        parser.add_argument('to', type=str)
        parser.add_argument('date', type=str)
        parser.add_argument('save_to', default=None, type=str, nargs='?')
        args = parser.parse_args()
        return args


if __name__ == '__main__':
    parser = Parser()
    args = parser.parser_func()
    maker = TicketFiller(fio=args.fio, from_=args.from_, to=args.to, date=args.date, save_to=args.save_to)
    maker.make_ticket()

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
