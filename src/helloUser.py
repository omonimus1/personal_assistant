import pyttsx3
import datetime
from datetime import datetime
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


def say_hello(day_fraction, user_name):
    engine.say(day_fraction + " " + user_name)


def hello_to_user(user):
    hour = get_hour()
    if hour >= 5 and hour < 12:
        say_hello('Good morning', user)
    elif hour >= 12 and hour < 18:
        say_hello('Good afternoon', user)
    elif hour >= 18 and hour < 21:
        say_hello('Good evening', user)
    elif hour >= 21:
        say_hello('Good night', user)


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
    engine.say('Today is the: ' + day + 'of' + month + str(year))
