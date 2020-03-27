import pyttsx3
import datetime
from datetime import datetime
import speech_recognition as sr

engine = pyttsx3.init()
r = sr.Recognizer()

def say_good_morning(user_name):
    engine.say("Good morning " + user_name)
        

def say_good_afternoon(user_name):
	engine.say("Good afternoon"+ user_name)
    

def say_good_evening(user_name):
	engine.say("Good evening" + user_name)

def say_good_night(user_name):
	engine.say("Good night" + user_name)


def say_hello_to_user(user):
    now = datetime.now()
    hour = now.hour
    if hour >= 6 and hour < 12:
        say_good_morning(user)
    elif hour >= 12 and hour < 18:
        say_good_afternoon(user)
    elif hour >= 18 and hour < 21:
        say_good_evening(user)
    elif hour >=21 and hour <=23 :
        say_good_night(user)
    else:
        say_good_night(user)
    

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
    elif month_number == '12':
        return 'December'
    else:   
        return 'Month is not correct'

def say_today_date():
    now = datetime.now()
    # Get information about current date 
    number_of_the_month = now.strftime("%m")
    day = now.strftime("%d")
    # Convert number of the month in it's name 
    month = get_name_of_the_month(number_of_the_month)

    engine.say('Today is the: ' + day + 'of' + month)
