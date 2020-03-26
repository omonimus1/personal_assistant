import pyttsx3
import json
from helloUser import *
import os.path
from os import path
import speech_recognition as sr


engine = pyttsx3.init()
r = sr.Recognizer()
user_data_path = 'data/user_data.json'
user_name = "The system did not recognize the name"


def is_data_file_present():
	"""
		:rtype: bool
	"""
	try:
		if str(path.exists(user_data_path)):
			return True
	except IOError:
			return False


def get_username_from_data_source():
	try:
		with open(user_data_path, 'r') as f:
			with open('jsonfile.txt') as jsonfile:
				parsed = json.load(jsonfile)
			print json.dumps(parsed, indent=2, sort_keys=True)
			f.close()
		return parsed['name']
	except IOError:
			print('Error while loading data source file in path: ' + user_data_path)
			return "Username not found"


def store_username_in_data_source(username):
	# Store the username in json file
	user = { }
	user['name'] = username
	with open(user_data_path, 'w') as f:
		json.dump(user, f)


def ask_username_to_user():
	with sr.Microphone() as source:
		print("Say your name")
		audio = r.listen(source)
		print("Time over, THANKS")
	try:
		username = r.recognize_google(audio);
		print("TEXT : " + username)
		return username
	except:
			pass;


""" RATE"""
engine.setProperty('voice', 'english+f2') # For girl voice we can use the range +f1 to +f4, remove the +fX we will have a default man voice
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 185)     # setting up new voice rate
print(rate)                        #printing current voice rate

# Main
def main():
	data_source_present = is_data_file_present()
	if  data_source_present:
		username = get_username_from_data_source()
		print('Name fetched from source: ' + username)
		say_hello_in_base_to_hour(username)
		engine.runAndWait()

	else:
		username = ask_username_to_user()
		store_username_in_data_source(username)
		say_hello_in_base_to_hour(username)
		engine.runAndWait()


main()