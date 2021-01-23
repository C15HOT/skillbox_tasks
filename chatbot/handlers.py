import re
import json

re_name = re.compile(r'^[\w\-\s]{3,40}$')
re_email = re.compile(r"\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b")
re_telephone = re.compile(r'\b\+?[7,8](\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2})\b')
re_date = re.compile(r'\d\d-\d\d-\d{4}')
re_race_number = re.compile(r'\d{3}')

cities = {"москв": "Москва", "лондон": "Лондон", "париж": "Париж", "нью-йорк": "Нью-Йорк", "токио": "Токио"}


def handle_name(text, context):
    match = re.match(re_name, text)
    if match:
        context['name'] = text
        return True
    else:
        return False


def handle_email(text, context):
    matches = re.findall(re_email, text)
    if len(matches) > 0:
        context['email'] = matches[0]
        return True
    else:
        return False


def handle_source(text, context):
    #if any(token in text.lower() for token in cities):
    for token in cities:
        if token in text.lower():
            context['source'] = cities[token]

        # context['source'] = text

            return True
    else:
        return False


def handle_destination(text, context):
    races = []
    # if any(token in text.lower() for token in cities):
    #     context['destination'] = text
    for token in cities:
        if token in text.lower():
            context['destination'] = cities[token]

            # context['source'] = text
            with open('date.json', 'r') as read_file:
                loaded_json_file = json.load(read_file)
                if loaded_json_file[context['source']][context['destination']]:
                    for race in loaded_json_file[context['source']][context['destination']]:
                        races.append(race)
            return races

    else:
        return False




def handle_date(text, context):
    match = re.match(re_date, text)
    races = []
    if match:
        context['date'] = text
        with open('date.json', 'r') as read_file:
            loaded_json_file = json.load(read_file)
            for number in context['races']:
                race = loaded_json_file[context['source']][context['destination']][number]
                if race[0] == context['date']:
                    races.append((number, race[0], race[1]))
        return races
    else:
        return False


def handle_race_number(text, context):
    match = re.match(re_race_number, text)
    if match:
        context['race_number'] = text
        return True
    else:
        return False


def handle_comment(text, context):
    context['comment'] = text
    return True


def handle_commit(text):
    if text == 'Да' or 'да':
        return True
    else:
        return False


def handle_phone(text, context):
    match = re.match(re_telephone, text)
    if match:
        context['phone'] = text
        return True
    else:
        return False
