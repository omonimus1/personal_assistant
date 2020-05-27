# Author: Davide Pollicino
# Date: 26/03/2020

import os

# Third part modules
import pyttsx3
import psutil 
import speech_recognition as sr
import wikipedia
# Custom modules
import dateManagement as dm
import assistantInformation as ai
import systemManagement as device
import youtube

engine = pyttsx3.init()
r = sr.Recognizer()

"""
SET Assistant voice configuration
For girl voice we can use the range +f1 to +f4
Remove the +fX we will have a default man voice
"""
engine.setProperty('voice', 'english+f2')
rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', 185)    # setting up new voice rate
print(rate)                        # printing current voice rate



"""
    Wikipedia query search
"""
# Ask to the user what to search on wikipedia
def get_page_to_search():
    research_message = 'What would you like to search?'
    print(research_message)
    engine.say(research_message)
    page = ask_to_user()
    return page


# Search on wikipedia 
def wikipedia_search(page_search):
    # Set language
    wikipedia.set_lang('en')
    page_name = {page_search.replace('search', '').replace('mean', '').replace('meaning', '')}
    print(wikipedia.summary(page_name, sentences=1))
    engine.say(wikipedia.summary(page_name, sentences=1))

# Create an instante of the Microphone object and listen to what the user says
def ask_to_user():
    try:
        with sr.Microphone() as source:
            print("Say something")
            audio = r.listen(source)
            print("Time over, THANKS")
            # If not understandable is said, or the user do not say anything
            # r.recognize_google() will rise an expetion
            vocal_command = r.recognize_google(audio)
            print('I heard: ' + str(vocal_command))
            return str(vocal_command)   
    except:
        engine.say('I did not get what you said')
        ask_to_user()


# Execute a command in according to what the user says 
def commands_control():
    engine.say('What Can I do for you?')
    while(True):
        command = ask_to_user()
        command = command.lower()
        # Find possible command 
        if command in ['hi', 'hello']:
            dm.say_hello()
        elif command in 'your name':
            ai.assistant_introduction()
        elif command in 'old are you':
            ai.provide_assistant_age()
        elif command in 'how are you':
            ai.assistant_emotion_state()
        elif 'date' in command and  'today' in command:
            dm.say_today_date()
        elif command  in ['means','search', 'mean', 'wikipedia']:
            search = get_page_to_search()
            wikipedia_search(search)
        elif command in ['play', 'song', 'youtube']:
            # Try to filter the query search to have more optimal results
            if 'play' in command:
                command.replace('play','')
            elif 'song' in command:
                command.replace('song', '')
            elif 'youtube' in command:
                command.replace('youtube', '')
            youtube.play_video('https://www.youtube.com/watch?v=FQkaH5ppFek')
        elif 'battery' in command:
            device.get_battery_state()
        elif 'reboot' in command:
            device.reboot_device()
        elif 'turn off' in command:
            device.turn_off_device
        engine.runAndWait()



# Entry point of the application 
if __name__ == '__main__':
    commands_control()
