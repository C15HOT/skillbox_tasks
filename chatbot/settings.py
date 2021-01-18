GROUP_ID = 201143207
TOKEN = 'ff1ffe20c93b89dbde9bc23e3c84409c6b39ab197281056df0147914d414d3dd5063d96a6fe9db4039f2c'

INTENTS = [
    {
        "name": "Заказ билетов",
        "tokens": ("/ticket"),
        "scenario": "registration",
        "answer": None,
    },
{
        "name": "Справка",
        "tokens": ("/help"),
        "scenario": None,
        "answer": 'Данный бот позволяет заказать билет на самолет'
        'Для заказа билета введите /ticket',
    },
    {
        "name": "Регистрация",
        "tokens": ("регист", "купи", "заказ"),
        "scenario": "registration",
        "answer": None
    },
]

SCENARIOS = {
    "registration":{
        "first_step": "step1",
        "steps":{
            "step1":{
                "text": "Введите город отправления.",
                "failure_text": "Из данного города нет рейсов",
                "handler": "handle_source",
                "next_step": "step2"
            },
            "step2":{
                "text": "Введите город назначения",
                "failure_text": "В данный город нет рейсов",
                "handler": "handle_destination",
                "next_step": "step3"
            },
            "step3":{
                "text": "Введите дату отправления в формате ДД-ММ-ГГГГ.",
                "failure_text": "В указанный день рейсов нет",
                "handler": "handle_date",
                "next_step": "step4"
            },
            "step4":{
                "text": "Введите номер рейса",
                "failure_text": None,
                "handler": "handle_race_number",
                "next_step": "step5"
            },
            "step5":{
                "text": "Вы можете оставить комментарий к заказу",
                "failure_text": None,
                "handler": "handle_comment",
                "next_step": "step6"
            },
            "step6":{
                "text": "Уточняем введенные данные, введите 'Да' или 'Нет'",
                "failure_text": None,
                "handler": "handle_commit",
                "next_step": "step7"
            },
            "step7":{
                "text": "Введите номер телефона",
                "failure_text": None,
                "handler": "handle_phone",
                "next_step": "step8"
            },
            "step8":{
                "text": "Спасибо за регистрацию! Мы свяжемся с вами по телефону {phone}",
                "failure_text": None,
                "handler": None,
                "next_step": None
            }
        }
    }
}

DEFAULT_ANSWER = 'К сожалению, рейсов с такими параметрами нет '\
                 'Вы можете ознакомиться с расписанием рейсов'

HElP = 'Данный бот позволяет заказать билет на самолет'\
    'Для заказа билета введите /ticket'