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
    },{
        "name": "Регистрация",
        "tokens": ("регист", "добав"),
        "scenario": "registration",
        "answer": None
    },
]

SCENARIOS = {

}