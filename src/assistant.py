# Author: Davide Pollicino
# Date: 26/03/2020

import pyttsx3
import psutil  # https://github.com/giampaolo/psutil
import speech_recognition as sr
import os
import wikipedia
import dateManagement as dm
import assistantInformation as ai
import systemManagement as device
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
    research_message = 'What would you like to search?'
    print(research_message)
    engine.say(research_message)
    page = ask_to_user()
    return page


def wikipedia_search(page_search):
    # Set language
    wikipedia.set_lang('en')
    page_name = {page_search.replace('search', '').replace('mean', '').replace('meaning', '')}
    print(wikipedia.summary(page_name, sentences=1))
    engine.say(wikipedia.summary(page_name, sentences=1))


def ask_to_user():
    try:
        with sr.Microphone() as source:
            print("Say something")
            audio = r.listen(source)
            print("Time over, THANKS")
            vocal_command = r.recognize_google(audio)
            print('I heard: ' + str(vocal_command))
            return str(vocal_command)   
    except:
        engine.say('I did not get what you said')
        ask_to_user()


def commands_control():
    while(True):
        engine.say('What Can I do for you?')
        command = ask_to_user()
        command = command.lower()
        # Find possible command 
        if 'hi' in command or 'hello' in command:
            dm.say_hello()
        elif 'your name' in command:
            ai.assistant_introduction()
        elif 'old are you' in command:
            ai.provide_assistant_age()
        elif 'how are you' in command:
            ai.assistant_emotion_state()
        elif 'date' in command and  'today' in command:
            dm.say_today_date()
        elif 'battery' in command:
            device.get_battery_state()
        elif 'reboot' in command:
            device.reboot_device()
        elif 'turn off' in command:
            device.turn_off_device
        elif 'search' in command or 'means' in command:
            search = get_page_to_search()
            wikipedia_search(search)
        else:
            did_not_get_information_message = 'I am sorry I did not get what you asked me'
            prit(did_not_get_information_message)
            engine.say(did_not_get_information_message)
            commands_control()

# Main
def main():
    commands_control()
    engine.runAndWait()


main()
