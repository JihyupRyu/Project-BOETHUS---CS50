import pyttsx3
import datetime
import os
import json
import requests
from core import *
from respond import *

import csv

if __name__=='__main__':
    speak("Activating")

    settings = check_settings()
    if settings['gender'] == 'male':
        title = "Sir"
    else:
        title = "Madam"
    counter = 0
    if counter == 0:
        greeting(title)
    counter = 1
    print(settings)

    # if settings['first_loading'] == "True":
    #     first_setup = True

    # while first_setup == True:
    #     first_loading()
    #     break

    started = True

    while started == True:
        statement = takeCommand("").lower()
        if "hey" in statement or "hi" in statement or "hello" in statement or "Are you there?" in statement or "Help" in statement:
            speak("What can I help you with?")
            started = False
            take_command = True

    while take_command == True:
        print('working')
        statement = takeCommand("").lower()
        if "who are you" in statement:
            respond_name()
        if "what time" in statement:
            respond_time()
        if "change setting" in statement or "setting" in statement:
            respond_settings(settings)
        if "google" in statement or "search" in statement:
            respond_google()
        if "youtube" in statement:
            respond_youtube()
        if 'location' in statement:
            respond_location()
        if 'where is' in statement:
            respond_where(statement)
        if 'what is' in statement and statement != "What is your name":
            respond_what(statement)
        if 'wikipedia' in statement:
            respond_wikipedia()
        if "turn off computer" in statement or "Turn off pc" in statement or "Shut down pc" in statement or "Shut down computer" in statement:
            respond_turn_off()
        if "terminate" in statement or "stop" in statement:
            speak("Goodbye " + title)
            break