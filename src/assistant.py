#!/usr/bin/env python

# Author: Davide Pollicino
# Date: 26/03/2020

import pyttsx3
from gtts import gTTS
import psutil  # https://github.com/giampaolo/psutil
import speech_recognition as sr
import os
import wikipedia
import json
import helloUser
# Speech recognitionn with Google Speech Recognition API


engine = pyttsx3.init()
r = sr.Recognizer()

# Assitante voice configurations
""" RATE"""
# For girl voice we can use the range +f1 to +f4
# Remove the +fX we will have a default man voice
engine.setProperty('voice', 'english+f2')
rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', 185)    # setting up new voice rate
print(rate)                        # printing current voice rate


file_path = 'data.json'

"""
    Wikipedia query search
"""
# Ask to the user in which language he would like to fetch the wiki
def get_result_language():
    print('Inside get result language')

    language = ask_to_user()
    print('LANGUAGE HEARD  ' + str(language))
    if "English" in language:
        return 'en'
    elif "Swedish" in language:
        return 'sv'
    elif "German" in language:
        return 'de'
    elif "French" in language:
        return 'fr'
    elif "Russian" in language:
        return 'ru'
    elif "Italian" in language:
        return 'it'
    elif "Spanish" in language:
        return 'es'
    print('Problem language retunr')
    return 'dne'


def get_page_to_search():
    engine.say('What would you like to search?')
    page = ask_to_user()
    return page


def wikipedia_search():
    engine.say('I can provide you information in English,' + 
        'Swedish, German, French, Russian, Italian or Spanish')
    engine.say('Which language do you prefer for your wikipedia search?')
    language_code = 'dne'
    while language_code == 'dne':
        language_code = get_result_language()
    # Set language
    wikipedia.set_lang(language_code)
    page_name = get_page_to_search()
    # Search page
    # ny = wikipedia.page(page_name)
    wikipedia.summary(page_name, sentences=1)
    engine.say(wikipedia.summary(page_name, sentences=1))
    # If the page does not exists, repeat search process
    '''
    if(not page_py.exists()):
        print('Soomethhing went wrong during the search, page does not exists')
        engine.say('The page that your are trying to search does not exists')
        engine.say('Please, be more specific')
        wikipedia_search()
    else:
        # Provide information found
        print('Printing page information')
        print(page_py.fullurl)
        engine.say(page_py.title)
        print(page_py.summary[0:60])
        engine.say(page_py.summary)
    '''

def ask_to_user():
    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)
        print("Time over, THANKS")
        vocal_command = r.recognize_google(audio)
        print('I heard' + str(vocal_command))
        return vocal_command

# Host device management
def turn_off_device():
    engine.say('Shutting down the device')
    os.system("shutdown /s /t 1")


def reboot_device():
    engine.say('Alright, I am rebooting the system')
    os.system("shutdown /r /t 1")


def get_battery_percentage():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    if percent <= 15.0 and plugged is False:
        engine.say('Ehi, mind that you are running out of battery')
        engine.say('Turn off your device to save battery')


# Introduce the personal assistant
def assistant_introduction():
    engine.say('Hi, I am your personal assistant and I can')
    list_functionalities()


def list_functionalities():
    engine.say('Give you current time and date')

# def ciao():
#    engine.say('Ciaooo')

# Main
def main():
    # engine.say('Main')
    # ciao()
    # print('passed main say')
    wikipedia_search()
    # assistant_introduction()
    # helloUser.current_time()
    # username = ask_to_user()
    # print(username)
    # helloUser.hello_to_user(username)
    # helloUser.say_today_date()
    get_battery_percentage()
    # Necessary to use the builtin say() method
    engine.runAndWait()


main()
