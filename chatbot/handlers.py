import re
import json
import datetime

from chatbot.generate_ticket import generate_ticket

re_name = re.compile(r'^[\w\-\s]{3,40}$')
re_email = re.compile(r"\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b")
re_telephone = re.compile(r'\b\+?[7,8](\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2})\b')
re_date = re.compile(r'\d\d-\d\d-\d{4}')
re_race_number = re.compile(r'\d{3}')

cities = {"москв": "Москва", "лондон": "Лондон", "париж": "Париж", "нью-йорк": "Нью-Йорк", "токио": "Токио"}


def handle_name(text, context, step):
    match = re.match(re_name, text)
    if match:
        context['name'] = text
        return True
    else:
        return False


def handle_email(text, context, step):
    matches = re.findall(re_email, text)
    if len(matches) > 0:
        context['email'] = matches[0]
        return True
    else:
        return False


def handle_source(text, context, step):
    # if any(token in text.lower() for token in cities):
    for token in cities:
        if token in text.lower():
            context['source'] = cities[token]

            # context['source'] = text

            return True
    else:
        return False


def handle_destination(text, context, step):
    races = []
    # if any(token in text.lower() for token in cities):
    #     context['destination'] = text
    for token in cities:
        if token in text.lower():

            context['destination'] = cities[token]

            # context['source'] = text
            with open('date.json', 'r') as read_file:
                loaded_json_file = json.load(read_file)
                if any(context['destination'] in city for city in loaded_json_file[context['source']]):
                    if loaded_json_file[context['source']][context['destination']]:
                        for race in loaded_json_file[context['source']][context['destination']]:
                            races.append(race)
                    context['allraces'] = races
                    return True

    else:
        return False


def handle_date(text, context, step):
    dates = []
    match = re.match(re_date, text)
    races = []
    if match:
        context['date'] = text
        user_date = datetime.datetime.strptime(text, '%d-%m-%Y')
        for day in range(5):
            last_date = user_date + datetime.timedelta(days=day)
            text_date = last_date.strftime("%d-%m-%Y")
            dates.append(text_date)
        with open('date.json', 'r') as read_file:
            loaded_json_file = json.load(read_file)
            for number in context['allraces']:
                race = loaded_json_file[context['source']][context['destination']][number]
                for day in dates:
                    if race[0] == day:
                        races.append((number, race[0], race[1]))
        context['races'] = races
        if len(races) != 0:
            return True
        else:
            return False
    else:
        return False


def handle_race_number(text, context, step):
    match = re.match(re_race_number, text)
    if match:
        for race in context['races']:
            if race[0] == text:
                context['race_number'] = text
                context['selected_race'] = race
                return True
    else:
        return False


def handle_comment(text, context, step):
    context['comment'] = text
    return True


def handle_commit(text, context, step):
    if text.lower() == 'да':
        return True
    else:
        step.step_name = "step1"
        return False


def handle_phone(text, context, step):
    match = re.match(re_telephone, text)
    if match:
        context['phone'] = text
        return True
    else:
        return False


def generate_ticket_handler(text, context, step):
    return generate_ticket(source=context['source'],
                           destination=context['destination'],
                           date=context['selected_race'][1],
                           race=context['selected_race'][0],
                           phone=context['phone'],
                           )
