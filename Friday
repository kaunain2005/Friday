import wikipedia
import pyttsx3
import speech_recognition as sr
import datetime
import time as t
import webbrowser
import os
import smtplib
# from camera import *

#?voice setup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

#! Speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#? introduction
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning konain sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon konain sir")
    else:
        speak("Good Evening konain sir")
    speak("I am Friday. speed capacity of 1 Terahertz memory capacity of 1 Zettabyte. How I can help you sir.")

#?command taking
def takeCommand():
    #! It takes microphone inputs and return string out put
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print('Recognizing...')
        query=r.recognize_google(audio,language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:

        print('Say that again please...')
        return 'None'
    return query

#?command taking 2
'''def takeCommand2():
    #! It takes microphone inputs and return string out put

    try:
        query=input('Enter command :\n')

    except Exception as e:

        print('Type that again please...')
        return 'None'
    return query'''

#?For emmail
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourEmail@example.com', 'your_password')
    server.sendmail('yourEmail@example.com', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()

    while True:
        query=takeCommand().lower()
        #!query=takeCommand2().lower()

        #? logic for executing task based on query
#!All commands
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia"," ")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening google")
        elif 'my name' in query:
            speak("Your name is konain sir")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Opening stackoverflow")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak("Opening facebook")
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%p:%I{}:%M{}:%S{}".format('hours', 'minutes', 'seconds'))
            print(strTime)
            speak(f"Sir, the time is {strTime}")
        elif 'date' in query:
            strDate=datetime.datetime.now().strftime("%B %d, %Y")
            speak(strDate)
            print(strDate)
        elif 'open code' in query:
            codepath='C:\\Users\\Family\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code'
            os.system(codepath)
            speak("Opening visual studio code")
        elif 'email' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                #content=takeCommand2()
                to="envkt@example.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("I am sorry sir, I am unable to send the email")
        elif 'play music' in query:
            music_dir='D:\\kaunain\\songs'
            songs=os.listdir(music_dir)
            print(songs)
            songs=os.startfile(os.path.join(music_dir, songs[0]))
            speak("Playing music")
        # elif 'capture my image' in query:
        #     speak('Say  cheeez')
        #     try:
        #         camera()
        #         print('Image captured...')
        #     except:
        #         speak("Image successfully captured")

        #!shut down
        elif'shutdown' in query:
            speak("Good Bye sir")
            exit()
        #!wait
        elif 'wait' in query:
            speak('ok sir')
            print('Wait....')
            t.sleep(5)
