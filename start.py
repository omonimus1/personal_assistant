#!/usr/bin/env python

# Author: Davide Pollicino
# Date: 26/03/2020


import pyttsx3
engine = pyttsx3.init()
import json
import os
import helloUser
import speech_recognition as sr

r = sr.Recognizer()
file_path = 'data.json'

"""
	User profile Management 
"""
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
		username = r.recognize_google(audio);
		return username
	except:
		print('Error while getting username')
		pass



""" RATE"""
engine.setProperty('voice', 'english+f2') # For girl voice we can use the range +f1 to +f4, remove the +fX we will have a default man voice
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 185)     # setting up new voice rate
print(rate)                        #printing current voice rate

# Main
def main():
	username = ask_name_to_user()
	helloUser.say_hello_to_user(username)
	helloUser.say_today_date()
	# Necessary to use the builtin say() method
	engine.runAndWait()


main()