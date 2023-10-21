from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil import parser

start_date = datetime.now()
old_days = 0
numbers = {
    0 : '0️⃣',
    1 : '1️⃣',
    2 : '2️⃣',
    3 : '3️⃣',
    4 : '4️⃣',
    5 : '5️⃣',
    6 : '6️⃣',
    7 : '7️⃣',
    8 : '8️⃣',
    9 : '9️⃣'
}

def get_str_from_number(number):
    strn = str(number)
    for s in strn:
        strn = strn.replace(s, numbers[int(s)])

    return strn

def start_counting(reset=False):
    global start_date
    global old_days

    old_days = get_days()
    start_date = datetime.now()

    start = 'Стартуем!\n'
    if reset:
        start = 'Ни дня без буллинга 😈\n'

    return start + get_print_str(not reset)

def calculate(text):
    days = 0

    return get_print_str()


def manual(text):
    global start_date
    global old_days
    old_days = get_days()

    text = text.replace('/set','').strip()
    start_date = start_date - relativedelta(days=int(text))

    return 'Ну допустим 😑\n' + get_print_str()

def help_message():
    return 'Снова буллят Женю? Скажем этому нет!\n/start - начинаем отсчёт дней\n/jenya - показать текущие количество дней без буллинга'+\
            '\n/zero - обнулить счётчик\n/set - задать вручную кол-во дней\n/help - вывести это сообщение\n\nЗ.ы. при упоминании Жени счётчик сбрасывается.'


def get_print_str(start=False):
    global old_days

    if start:
        return str('Дни без буллинга Жени:\n'  + get_str_from_number(get_days()))


    return str('Дни без буллинга Жени:\n' + get_str_from_number(old_days) + ' ➔ ' + get_str_from_number(get_days()))


def get_days():
    global start_date
    return (datetime.now() - start_date).days