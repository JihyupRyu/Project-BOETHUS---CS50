from core import *

import webbrowser
import time
import wikipedia
import subprocess

def respond_name():
    print('?')
    speak('My name is Boethus')

def respond_time():
    speak(time.ctime())

def respond_settings(settings):
    speak("Which settings would you like to change?")
    settings_statement = takeCommand("").lower()
    if "language" in settings_statement:
        change_language_setting()
    if "gender" in settings_statement:
        change_gender_setting(settings)

def respond_google():
    print('?')
    search = takeCommand("What do you want to search for?")
    url = 'https://google.com/search?q=' + search
    webbrowser.get().open(url)
    speak('Here is what I found for ' + search)

def respond_youtube():
    search = takeCommand("What do you want to search for in Youtube?")
    url = 'https://www.youtube.com/results?search_query=' + search
    webbrowser.get().open(url)
    speak('Here is what I found for ' + search)

def respond_location():
    location = takeCommand('What is the location?')
    url = 'https://google.nl/maps/place/' + location + '/&amp;'
    webbrowser.get().open(url)
    speak("Here is the location of " + location)

def respond_where(statement):
    location = statement.split()[2]
    url = 'https://google.nl/maps/place/' + location + '/&amp;'
    webbrowser.get().open(url)
    speak("Here is the location of " + location)

def respond_what(statement):
    keyword = statement.split()[2]
    results = wikipedia.summary(keyword, sentences = 3)
    print(results)
    speak(keyword + " is " + results)

def respond_wikipedia():
    keyword = takeCommand('What do you want to know about?')
    results = wikipedia.summary(keyword, sentences = 3)
    print(results)
    speak("According to Wikipedia " + results)

def respond_turn_off():
    speak("Ok , your pc will turn off in 10 seconds")
    subprocess.call(["shutdown", "/l"])