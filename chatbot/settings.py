GROUP_ID = 201143207
TOKEN = 'ff1ffe20c93b89dbde9bc23e3c84409c6b39ab197281056df0147914d414d3dd5063d96a6fe9db4039f2c'

INTENTS = [
    {
        "name": "Дата проведения",
        "tokens": ("когда", "сколько", "дата", "дату"),
        "scenario": None,
        "answer": "Конференция проводится 15го апреля, регистрация начинается в 10 утра",
    },
{
        "name": "Место проведения",
        "tokens": ("где", "место", "локация", "адрес", "метро"),
        "scenario": None,
        "answer": "Конференция пройдет в павильоне 18Г в Экспоцентре",
    },
    {
        "name": "Регистрация",
        "tokens": ("регист", "добав"),
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
                "failure_text": "Имя должно состоять из 3-30 букв и дефиса. Попробуйте еще раз",
                "handler": "handle_name",
                "next_step": "step2"
            },
            "step2":{
                "text": "Введите город назначения",
                "failure_text": "Во введенном адресе ошибка. Попробуйте еще раз",
                "handler": "handle_email",
                "next_step": "step3"
            },
            "step3":{
                "text": "Введите дату отправления в формате ДД-ММ-ГГГГ.",
                "failure_text": None,
                "handler": None,
                "next_step": None
            },
            "step4":{
                "text": "Спасибо за регистрацию, {name}! Мы отправили на {email} билет, распечатайте его.",
                "failure_text": None,
                "handler": None,
                "next_step": None
            },
            "step5":{
                "text": "Спасибо за регистрацию, {name}! Мы отправили на {email} билет, распечатайте его.",
                "failure_text": None,
                "handler": None,
                "next_step": None
            },
            "step6":{
                "text": "Спасибо за регистрацию, {name}! Мы отправили на {email} билет, распечатайте его.",
                "failure_text": None,
                "handler": None,
                "next_step": None
            },
            "step7":{
                "text": "Спасибо за регистрацию, {name}! Мы отправили на {email} билет, распечатайте его.",
                "failure_text": None,
                "handler": None,
                "next_step": None
            }
        }
    }
}

DEFAULT_ANSWER = 'Не знаю как на это ответить. '\
                 'Могу сказать когда и где пройдет конференция, а также зарегистрировать вас'