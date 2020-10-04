import speech_recognition as sr
import csv
import pyttsx3
import datetime
import time

engine=pyttsx3.init()
# engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

# def first_loading():
#     speak("First loading... build settings")
#     name = takeCommand("What is your name?")
#     gender = takeCommand("What is your gender?")

def check_settings():
    with open("./assets/csv/settings.csv", 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            return dict(row)

def change_language_setting():
    speak("I'm sorry, this function is not avaiable for now")
    # takeCommand('What language would you prefer?')

def change_gender_setting(settings):
    gender = takeCommand('What is your gender?')
    if "male" in gender or "man" in gender or "female" in gender or "woman" in gender:
        if "male" in gender or "man" in gender:
            temp_gender = "male"
            if settings['gender'] == "male":
                speak("I'm afraid sir, you already told me you are male")
            else:
                with open("./assets/csv/settings.csv", mode='w') as file:
                    male_fieldsnames = ['language', 'gender', 'first_loading']
                    writer = csv.DictWriter(file, fieldnames = male_fieldsnames)
                    writer.writeheader()
                    writer.writerow({'language': settings['language'], 'gender': temp_gender, 'first_loading': settings['first_loading']})
            
        if "female" in gender or "woman" in gender:
            temp_gender = "female"
            if settings['gender'] == "female":
                speak("I'm afraid madam, you already told me you are female")
            else:
                with open("./assets/csv/settings.csv", mode='w') as file:
                    fe_fieldsnames = ['language', 'gender']
                    writer = csv.DictWriter(file, fieldnames = fe_fieldsnames)
                    writer.writeheader()
                    writer.writerow({'language': settings['language'], 'gender': temp_gender, 'first_loading': settings['first_loading']})
    else:
        speak("Sorry you must tell me you are male or female")


def speak(text):
    engine.say(text)
    engine.runAndWait()

def greeting(title):
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning " + title)
        print("Good Morning " + title)
    elif hour>=12 and hour<18:
        speak("Good Afternoon " + title)
        print("Good Afternoon " + title)
    else:
        speak("Good Evening " + title)
        print("Good Evening " + title)

def takeCommand(ask):
    print(ask)
    r=sr.Recognizer()
    with sr.Microphone() as source:
        if ask != "":
            speak(ask)
        print("Listening...")
        audio=r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio,language='en-in')
            print(f"user said:{voice_data}\n")
            return voice_data
        except sr.UnknownValueError:
            speak("Unknown error restarting")
        except sr.RequestError:
            speak("Something went wrong with server")
        return voice_data

# import time
# ts = time.gmtime()
# print(time.strftime("%Y-%m-%d %H:%M:%S", ts))