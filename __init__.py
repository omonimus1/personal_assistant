import pyttsx3
import json
from helloUser import *
import speech_recognition as sr

engine = pyttsx3.init()
r = sr.Recognizer()

user_name = "The system did not recognize the name"

with sr.Microphone() as source:
	print("Say your name")
	audio = r.listen(source)
	print("Time over, THANKS")

try:
	user_name = r.recognize_google(audio);
	print("TEXT : " + user_name)
	# Store the username in json file
	user = {}
	user['name'] = user_name
	with open('user_data.json', 'w') as f:
		json.dump(user , f)

except:
		pass;

""" RATE"""
engine.setProperty('voice', 'english+f2') # For girl voice we can use the range +f1 to +f4, remove the +fX we will have a default man voice
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 185)     # setting up new voice rate
print (rate)                        #printing current voice rate

say_hello_in_base_to_hour(user_name)
engine.runAndWait()
