import pyttsx3
import datetime
from datetime import datetime, date
import speech_recognition as sr

engine = pyttsx3.init()
r = sr.Recognizer()

now = datetime.now()


def get_minute():
    return now.minute


def get_hour():
    return now.hour


def get_month_id():
    return now.strftime("%m")


def get_day_of_the_week():
    return now.strftime("%d")


def get_year():
    return now.year


def current_time():
    hour = get_hour()
    minute = get_minute()
    engine.say('Current time is: ' + str(hour) + 'and' + str(minute))


def say_hello():
    hello = 'Hello!'
    print(hello)
    engine.say(hello)


def hello_to_user():
    hour = get_hour()
    intro = 'Hi, I hope you are having a'
    if hour >= 5 and hour < 12:
        say_hello(intro + ' good morning')
    elif hour >= 12 and hour < 18:
        say_hello(intro + ' good afternoon')
    elif hour >= 18 and hour < 21:
        say_hello(intro + ' good evening')
    elif hour >= 21:
        say_hello(intro + ' good night')


def get_name_of_the_month(month_number):
    if month_number == '01':
        return 'Jenuary'
    elif month_number == '02':
        return 'February'
    elif month_number == '03':
        return 'March'
    elif month_number == '04':
        return 'April'
    elif month_number == '05':
        return 'May'
    elif month_number == '06':
        return 'June'
    elif month_number == '07':
        return 'July'
    elif month_number == '08':
        return 'August'
    elif month_number == '09':
        return 'Septmber'
    elif month_number == '10':
        return 'October'
    elif month_number == '11':
        return 'November'
    return 'December'


def say_today_date():
    day = get_day_of_the_week()
    month_id = get_month_id()
    month = get_name_of_the_month(month_id)
    year = get_year()
    today_date = 'Today is ' + day + ' of ' + month + ' ' + str(year)
    print(today_date)
    engine.say(today_date)


def get_day_name_having_its_day_id(day_id):
    if day_id == 0:
        return 'Monday'
    elif day_id == 1:
        return 'Tuesday'
    elif day_id == 2:
        return 'Wednesday' 
    elif day_id == 3:
        return 'Thursday' 
    elif day_id == 4:
        return 'Friday' 
    elif day_id == 5:
        return 'Saturday' 
    else:
        return 'Sunday'


