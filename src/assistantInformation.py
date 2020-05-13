
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

# Introduce the personal assistant
def assistant_introduction():
    presentation = 'I am Sophia, your personal assistant'
    print(presentation)
    engine.say(presentation)


def provide_assistant_age():
    age_response = 'I am quite young, I am still learning'
    print(age_response)
    engine.say(age_response)


def assistant_emotion_state():
    state = 'I am very well, thank you'
    print(state)
    engine.say(state)