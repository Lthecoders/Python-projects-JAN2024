
"""
author: Nikhil Gaikwad
date: 23th March 2024
project: Jarvis Virtual Assistant

description: Jarvis is a voice-activated virtual assistant designed to perform tasks such as web 
browsing, playing music, fetching news, and responding to user queries using OpenAI's 
GPT-3.5-turbo model.

"""
# print("Hello World")

# # Importing the required libraries
import speech_recognition as sr
import webbrowser
import pyttsx3


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text): # Function to convert text to speech
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open" in c:
        if "YouTube" in c.lower():
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com/")
        elif "Google" in c.lower():
            speak("Opening Google")
            webbrowser.open("https://www.google.com/")
        # elif "GitHub" in c.lower():
        #     speak("Opening GitHub")
        #     webbrowser.open(

if __name__ == "__main__":
    speak("Initiallizing Jarvis")
    while True:
        # listen for the wake word 'Jarvis'
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing...")

        # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("Ya") 
                # listen for the user's command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                     
                    processCommand(command)

        except Exception as e:
            print("error; {0}".format(e))
    




