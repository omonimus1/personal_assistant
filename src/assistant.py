#!/usr/bin/env python

# Author: Davide Pollicino
# Date: 26/03/2020

import psutil  # https://github.com/giampaolo/psutil
import speech_recognition as sr
import pyttsx3
import os
engine = pyttsx3.init()
import json
import helloUser
# Speech recognitionn with Google Speech Recognition API

r = sr.Recognizer()
file_path = 'data.json'

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


def ask_name_to_user():
    with sr.Microphone() as source:
        print("Say your name")
        audio = r.listen(source)
        print("Time over, THANKS")
    try:
        username = r.recognize_google(audio)
        return username
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
    # assistant_introduction()
    # helloUser.current_time()
    # username = ask_name_to_user()
    # print(username)
    # helloUser.hello_to_user(username)
    # helloUser.say_today_date()
    get_battery_percentage()
    # Necessary to use the builtin say() method
    engine.runAndWait()


main()
