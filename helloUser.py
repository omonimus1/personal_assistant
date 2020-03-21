import pyttsx3
import datetime
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


def  say_hello_in_base_to_hour(user):
    now = datetime.datetime.now()
    hour = now.hour
    print(hour)

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
    