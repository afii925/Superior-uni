## Voice Assistant

import wolframalpha
import pyttsx3
import json
import random
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import shutil
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning Sir!")
    elif hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    
    assname = "Parlina"
    speak("I am your Assistant")
    speak(assname)

def username():
    speak("What should I call you, sir?")
    uname = takeCommand()
    speak("Welcome Afzaal")
    speak(uname)
    columns = shutil.get_terminal_size().columns
    
    print("#####################".center(columns))
    print(f"Welcome Mr. {uname}".center(columns))
    print("#####################".center(columns))
    
    speak("How can I help you, Sir?")

def takeCommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e) 
        print("Unable to recognize your voice.") 
        return "None"
    
    return query

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        
        # Enable low security in Gmail
        server.login('your_email@gmail.com', 'your_email_password')  # Update with your email credentials
        server.sendmail('your_email@gmail.com', to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("I am not able to send this email")

clear = lambda: os.system('cls')
clear()
wishMe()
username()
    
while True:
    query = takeCommand().lower()
    
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        speak("Here you go to YouTube\n")
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        speak("Here you go to Google\n")
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        speak("Here you go to Stack Overflow. Happy coding!")
        webbrowser.open("stackoverflow.com") 

    elif 'play music' in query or "play song" in query:
        speak("Here you go with music")
        music_dir = r"C:\Users\AFZAAL MUSTAFA\Desktop\DSA LAB TASKS\DSA lab-4 Task\songs"
        songs = os.listdir(music_dir)
        print(songs) 
        os.startfile(os.path.join(music_dir, random.choice(songs)))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S") 
        speak(f"Sir, the time is {strTime}")

    elif 'email to Afzaal Mustafa' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "receiver_email@example.com"  # Update with actual receiver email
            sendEmail(to, content)
        except Exception as e:
            print(e)
            speak("I am not able to send this email")

    elif 'how are you' in query:
        speak("I am fine, thank you.")
        speak("How are you, Sir?")

    elif 'fine' in query or "good" in query:
        speak("It's good to know that you're fine.")

    elif "what's your name" in query or "what is your name" in query:
        speak("My friends call me Parlina.")

    elif 'exit' in query:
        speak("Thanks for giving me your time")
        exit()

    elif "who made you" in query or "who created you" in query: 
        speak("I have been created by Afzaal Mustafa.")

    elif "calculate" in query: 
        app_id = "LPXJ99-4RYVYHLVU4"  # Replace with your actual API ID
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('calculate') 
        query = query.split()[indx + 1:] 
        res = client.query(' '.join(query)) 
        answer = next(res.results).text
        print("The answer is " + answer) 
        speak("The answer is " + answer) 

    elif 'search' in query or 'play' in query:
        query = query.replace("search", "").replace("play", "").strip()
        webbrowser.open(query) 

    elif "who am i" in query:
        speak("If you talk, then definitely you're human.")

    elif 'news' in query:
        try: 
            jsonObj = urlopen('https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey= 31951f7391c245bc8bb9d51a6ffb7e2d')  # Update with your API key
            data = json.load(jsonObj)
            i = 1
            
            speak('Here are some top news from the Times of PAKISTAN:')
            print('''=============== TIMES OF PAKISTAN ============''' + '\n')
            
            for item in data['articles']:
                print(str(i) + '. ' + item['title'] + '\n')
                print(item['description'] + '\n')
                speak(str(i) + '. ' + item['title'] + '\n')
                i += 1 
        except Exception as e:
            print(str(e))
            speak("Could not fetch news.")
