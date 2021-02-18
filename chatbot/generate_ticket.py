from io import BytesIO

import requests
from PIL import Image, ImageFont, ImageDraw, ImageColor


AVATAR_OFFSET = (400, 80)

def generate_ticket(source, destination, date, race, phone):
    base = Image.open('files/ticket_template.png').convert('RGBA')
    font = ImageFont.truetype('arial.ttf', size=20)
    draw = ImageDraw.Draw(base)
    width, hight = base.size
    phone_y = width - 493 - (10 + font.size) * 2
    from_y = width - 423 - (10 + font.size) * 2
    to_y = width - 357 - (10 + font.size) * 2
    date_y = width - 357 - (10 + font.size) * 2
    draw.text((45, from_y), source, font=font, fill=ImageColor.colormap['black'])
    draw.text((45, to_y), destination, font=font, fill=ImageColor.colormap['black'])
    draw.text((280, date_y), date, font=font, fill=ImageColor.colormap['black'])
    draw.text((45, 328), race, font=font, fill=ImageColor.colormap['black'])
    draw.text((45, phone_y), phone, font=font, fill=ImageColor.colormap['black'])



    responce = requests.get(url=f'https://i.pravatar.cc/100?u={phone}')
    avatar_file_like = BytesIO(responce.content)

    avatar = Image.open(avatar_file_like)


    base.paste(avatar, AVATAR_OFFSET)
    temp_file = BytesIO()
    base.save(temp_file, 'png')
    temp_file.seek(0)

    return temp_file




generate_ticket('Москва', 'Лондон', '09-02-2021', '843', '89992223311')