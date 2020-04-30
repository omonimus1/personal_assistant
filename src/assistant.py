#!/usr/bin/env python

# Author: Davide Pollicino
# Date: 26/03/2020

import psutil  # https://github.com/giampaolo/psutil
import speech_recognition as sr
import pyttsx3
import os
import wikipediaapi
engine = pyttsx3.init()
import json
import helloUser
# Speech recognitionn with Google Speech Recognition API

r = sr.Recognizer()
file_path = 'data.json'

"""
    Wikipedia query search
"""
# Ask to the user in which language he would like to fetch the wiki
def get_result_language():
    print('Inside get result language')
    engine.say('I can provide you information in English,' + 
        'Swedish, German, French, Russian, Italian or Spanish')
    engine.say('Which language do you prefer for your wikipedia search?')
    language = ask_to_user()
    if language == 'English':
        language_code = 'en'
        return language_code
    elif language == 'Swedish':
        language_code = 'sv'
        return language_code
    elif language == 'German':
        language_code = 'de'
        return language_code
    elif language == 'French':
        language_code = 'fr'
        return language_code
    elif language == 'Russian':
        language_code = 'ru'
        return language_code
    elif language == 'Italian':
        language_code = 'it'
        return language_code
    elif language == 'Spanish':
        language_code = 'es'
        return language_code
    else:
        engine.say('Sorry, I did not get the language '+
            'o the language that you have indicated is not available, try again' )
        get_result_language()


def get_page_to_search():
    engine.say('What would you like to search?')
    page = ask_to_user()
    return page

def wikipedia_search():
    language_code = get_result_language()
    # Filter the search on a specific language
    wiki_wiki = wikipediaapi.Wikipedia(language_code)
    page_name = get_page_to_search()
    # Check if the page exists
    page_py = wiki_wiki.page(page) 
    # If the page does not exists, repeat search process
    if( not page_py.exists()):
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
        engine.say(page_py.summary[0:150])
        
        

"""
    User profile Management 
"""

# Get User information Secondion
def does_user_exists(json_str):
    resp = json.loads(json_str)
    return resp['username']


def load_default_user_data():
    data = {  'username': '1' ,'email': '1' }
    with open(file_path, "w") as write_file:
        json_str = json.dumps(data)
    return json_str


def ask_to_user():
    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)
        print("Time over, THANKS")
    try:
        vocal_command = r.recognize_google(audio)
        return vocal_command
    except:
        engine.say('I am sorry, there was an error while getting your name')
        pass


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


# Assitante voice configurations
""" RATE"""
# For girl voice we can use the range +f1 to +f4
# Remove the +fX we will have a default man voice
engine.setProperty('voice', 'english+f2')
rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', 185)    # setting up new voice rate
print(rate)                        # printing current voice rate


# Introduce the personal assistant
def assistant_introduction():
    engine.say('Hi, I am your personal assistant and I can')
    list_functionalities()


def list_functionalities():
    engine.say('Give you current time and date')


# Main
def main():
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
