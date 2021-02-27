import datetime

import cv2


def day_handler(day):
    _, number, month = day.split(' ')

    equal = {'янв': 1, 'фев': 2,
             'мар': 3, 'апр': 4,
             'май': 5, 'июн': 6,
             'июл': 7, 'авг': 8,
             'сен': 9, 'окт': 10,
             'ноя': 11, 'дек': 12,
             }
    date = datetime.date(year=datetime.date.today().year, month=equal[month], day=int(number))
    return date


class ImageMaker:
    PATTERN = 'python_snippets/external_data/probe.jpg'
    LINKS = {
        'Пасмурно': 'python_snippets/external_data/weather_img/cloud.jpg',
        'Ясно': 'python_snippets/external_data/weather_img/sun.jpg',
        'снег': 'python_snippets/external_data/weather_img/snow.jpg',
        'Облачно': 'python_snippets/external_data/weather_img/cloud.jpg',
        'Мокрый снег': 'python_snippets/external_data/weather_img/snow.jpg',
        'Дождь с грозой': 'python_snippets/external_data/weather_img/rain.jpg',
        'Малооблачно': 'python_snippets/external_data/weather_img/cloud.jpg',
        'Небольшой снег': 'python_snippets/external_data/weather_img/snow.jpg',
        'дождь': 'python_snippets/external_data/weather_img/rain.jpg',
        'осадки': 'python_snippets/external_data/weather_img/rain.jpg'
    }

    def put_data(self, data):

        y = 50

        img_x = 900
        for day, values in data.items():
            image = cv2.imread(self.PATTERN)
            image = self.gradient(image=image, state=data[day]['День'][0][0])

            cv2.putText(image, day_handler(day).strftime("%Y-%m-%d"), (50, y), cv2.FONT_HERSHEY_COMPLEX, 1,
                        (0, 0, 0), 2)
            for states, items in values.items():
                y += 100

                temp = items[1].replace('−', '-')

                text = f"{states}: {items[0][0]}, Температура: {temp}"

                if len(items[0]) > 1:
                    #  можно упростить проверку при помощи оператора in и кортежа из вариантов
                    if items[0][1] in ('небольшой', 'мокрый', 'небольшие', 'сильный'):
                        if items[0][2] == 'мокрый':
                            state = items[0][3]
                        else:
                            state = items[0][2]
                    else:
                        state = items[0][1]

                else:
                    state = items[0][0]

                image = self.put_image(background=image, state=state, x=img_x, y=y)

                # print(text)
                cv2.putText(image, text, (50, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            y = 50

            # self.viewImage(image, 'Line')

            cv2.imwrite(f'images/image_{day_handler(day).strftime("%Y-%m-%d")}.jpg', image)

    def put_image(self, background, state, x, y):
        img1 = background

        img2 = cv2.imread(self.LINKS[state])

        scale_percent = 100  # Процент от изначального размера
        width = int(img2.shape[1] * scale_percent / 100)
        height = int(img2.shape[0] * scale_percent / 100)
        dim = (width, height)
        img2 = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)

        rows, cols, channels = img2.shape
        roi = img1[0:rows, 0:cols]

        img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)

        img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

        img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

        dst = cv2.add(img1_bg, img2_fg)
        img1[0 + y - 50:rows + y - 50, 0 + x:cols + x] = dst

        return img1

    def gradient(self, image, state):
        y = image.shape[0]
        x = image.shape[1]
        if state == 'Ясно':

            g = 0
            r = 0
            b = 255
        elif state == 'Дождь':

            g = 255
            r = 255
            b = 0
        elif state == 'cнег':

            g = 0
            r = 255
            b = 0
        elif state in ('Пасмурно', 'Малооблачно', 'Облачно'):

            g = 100
            r = 100
            b = 100

        else:
            g = 1
            r = 1
            b = 1

        for i in range(y):
            #  градиент можно упростить
            # 1) вложенный цикл убрать и использовать cv2.line
            # 2) определить начальный цвет ДО вызова функции градиента
            #  передавать в функцию начальный цвет и к нему прибавлять +1 по каждому каналу, если он меньше 255

            cv2.line(img=image, pt1=(i, 0), pt2=(i, x), color=(b + i, g + i, r + i))

        return image


if __name__ == '__main__':
    img = ImageMaker()
    img.put_data(data={'Сб, 27 фев': {'Ночь': [['Пасмурно', 'небольшие', 'осадки'], '+3'],
                                      'Утро': [['Пасмурно', 'небольшие', 'осадки'], '+2'],
                                      'День': [['Малооблачно', 'небольшой', 'снег'], '0'],
                                      'Вечер': [['Облачно'], '−3']}})
