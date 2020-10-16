# To make these RUN Successfully you will have to make some of the changes in code and install all packages below except "in-built packages"

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import time
import pyperclip
import wolframalpha
import win10toast
from pytube import YouTube
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
for v in voices:
    print()
engine.setProperty(
    'voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0')

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('<-- YOUR EMAIl-->', '<--YOUR PASSWORD-->')
    server.sendmail('<-- YOUR EMAIl-->', to, content)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Pritish, how may I help you?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)

    try:
        global query
        query = r.recognize_google(audio, language='en-us')
        user = f"User said: {query}"
        print(user)

    except Exception:
        return "None"

    return query


def internal_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        global query_1
        query_1 = r.recognize_google(audio)

    except Exception:
        print('Say that again please')
        return "None"

    return query_1

# For win10toast


def notifier(x="", y=""):
    notify = win10toast.ToastNotifier()
    notify.show_toast(x, y, duration=5)


dictionary = {'launch google': 'www.google.com',
              'launch gmail': 'www.gmail.com',
              'launch youtube': 'www.youtube.com',
              'launch udemy': 'www.udemy.com'
              }

dictionary_1 = {'open c drive': 'C:\\',
                'open e drive': 'E:\\',
                'open f drive': 'F:\\',
                'open paint': 'C:\\Windows\\system32\\mspaint.exe',
                'open notepad': 'C:\\Users\\Admin\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk',
                'open cmd': 'C:\\Users\\Admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk'
                }

if __name__ == '__main__':
    wish_me()
    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            try:
                speak("Searching wikipedia...")
                query = query.replace('wikipedia', '')
                results = wikipedia.summary(query)
                print(results)
                speak("According to wikipedia")
                speak(results)

            except Exception:
                print('Sorry, Something went wrong')
                speak('Sorry, Something went wrong')

        elif 'set alarm' in query:
            speak('Ok, when for?')

            def alarm():
                hour = int(input('Enter the hour:'))
                minute = int(input('Enter the minute:'))
                second = int(input('Enter the second:'))
                topic = str(input('What is the topic of alarm : '))
                notifier("Alarm Set", f"Alarm set for {hour}:{minute}")

                while True:
                    if time.localtime().tm_hour == hour and time.localtime().tm_min == minute and\
                            time.localtime().tm_sec == second:
                        os.startfile(
                            'C:\\Users\\Default\\Music\\Imagine Dragons.mp3')
                        print(topic)
                        break

            alarm()
            continue

        elif 'launch' in query:
            query.replace('launch', '')
            for x, y in dictionary.items():
                if query == x:
                    speak(f'Opening {x[6:]}')
                    webbrowser.open(y)

        elif 'open' in query:
            for x, y in dictionary_1.items():
                if x == query:
                    speak(f'Opening {x[5:]}')
                    os.startfile(y)

        elif 'hi' in query:
            speak("Hello, Human")
            print("Hello, Human")

        elif 'google search' in query:
            speak("Searching google...")
            query = query.replace('google search', '')
            tabUrl = 'https://google.com/?#q='
            webbrowser.open(tabUrl + query)

        elif 'set timer' in query:
            query.replace('set timer', '')
            speak('Of how many seconds?')
            query_1 = internal_command()
            print(query_1)
            stopwatch_time = int(query_1)
            while True:
                print(stopwatch_time)
                time.sleep(1)
                stopwatch_time -= 1
                if stopwatch_time == 0:
                    os.startfile(
                        'C:\\Users\\Admin\\Music\\Imagine Dragons.mp3')
                    break

        elif 'play music' in query:
            speak("Enjoy your music")
            lst = os.listdir('C:\\Users\\Default\\Music')
            choose = random.randint(0, len(lst)-1)
            music_dir = 'C:\\Users\\Default\\Music' + '\\' + lst[choose]
            os.startfile(music_dir)

        elif 'exit' in query:
            speak("Thank you, sir")
            break

        elif 'date' in query:
            d = datetime.datetime.now()
            print("Date is {}".format(d.date()))
            speak("Date is {}".format(d.date()))

        elif 'youtube search' in query:
            query = query.replace('youtube search', '')
            query = query.replace('youtube', '')
            speak("Showing results")
            link = "https://www.youtube.com/results?search_query="
            webbrowser.open(link + query)

        elif 'copy' in query:
            query = query.replace("copy", "")
            query = query.replace("to my clipboard", "")
            query = query.replace("to clipboard", "")
            pyperclip.copy(query)
            speak("The text has been copied to your clipboard")

        elif "find prime number" in query:
            query = query.replace("find prime number", "")
            speak("Which number")
            try:
                query_1 = internal_command().lower()
                int(query_1)

            except:
                speak("Sorry, I didn't understand")

            try:
                for i in range(2, int(query_1)):
                    if int(query_1) % i == 0:
                        print(
                            f"{query_1} is not a prime number.It is divisible by {i}")
                        speak(
                            f"{query_1} is not a prime number.It is divisible by {i}")
                        break

                else:

                    print(f"{query_1} is a prime number")
                    speak(f"{query_1} is a prime number")

            except Exception:
                speak("Sorry, I didn't understand")

        elif 'automatic mode' in query:
            webbrowser.open("www.youtube.com")
            webbrowser.open("www.google.com")
            os.startfile("E:\\pritish")

        elif 'random video' in query:
            print("Showing a random video from youtube...")
            speak("Showing a random video from youtube...")
            lst = ['https://www.youtube.com/watch?v=jAXijgNm0vs', 'https://www.youtube.com/watch?v=ARWbsGi-dWU', 'https://www.youtube.com/watch?v=OCeqeJi_jYI',
                   'https://www.youtube.com/watch?v=JGwWNGJdvx8', 'https://www.youtube.com/watch?v=mZ-9JrzflIE', 'https://www.youtube.com/watch?v=STl_OcFFrIw', 'https://www.youtube.com/watch?v=qFkNATtc3mc']
            choice = random.randint(0, len(lst)-1)
            webbrowser.open(lst[choice])

        elif 'com'in query:
            query = query.replace('.com', '')
            query = query.replace('dot com', '')
            query = query.replace('www', '')
            query = query.replace('www.', '')
            query = query.replace('www dot', '')
            speak(f'Opening {query}.com')
            webbrowser.open(f'www.{query}.com')


        elif 'send email' in query:
            print("What should I say ?")
            speak("What should I say ?")
            to = '<-- YOUR EMAIl-->'
            content = take_command()
            sendemail(to, content)
            speak('Email has been sent...')


        elif 'sam' in query:
            try:
                query = query.replace('sam', '')
                client = wolframalpha.Client("<--Your WOlframalpha API--> For more info see these : https://www.youtube.com/watch?v=Lc43YZ6VRY0&t")
                res = client.query(query)
                ans = next(res.results).text
                print(ans)
                speak(ans)
            except:
                try:
                    query = query.replace('wikipedia', '')
                    query = query.replace('sam', '')
                    results = wikipedia.summary(query, sentences=1)
                    print(results)
                    speak(results)
                except:
                    try:
                        speak("I found these on web")
                        query = query.replace('sam', '')
                        if query == 'Sam':
                            speak("Yes, that's my name")
                        tabUrl = 'https://google.com/?#q='
                        webbrowser.open(tabUrl + query)
                    except:
                        speak("It's wierd but I found nothing..")
                        print("It's wierd but I found nothing..")


        elif 'joke' in query:
            joke = ['I ate a clock yesterday, it was very time-consuming.',
                    'A perfectionist walked into a bar…apparently, the bar wasn’t set high enough.',
                    'Question: What vegetables do librarians like? Answer: Quiet peas.',
                    'I just saw my math teacher lock himself in his office with a piece of graph paper. I think he must be plotting something.',
                    'Question: Which is closer, Florida or the moon? Answer: The moon. You can’t see Florida from here.',
                    'Q. Did Adam and Eve ever have a date?A. No, they had an apple!']

            joke_choice = random.randint(0, len(joke)-1)
            print(joke[joke_choice])
            speak(joke[joke_choice])

        elif 'riddle' in query:
            speak("I am not interested telling you riddles")

        elif 'download video' in query:
            speak("Please enter the URL of YouTube video that you have to download")
            url = input(
                "Give the link of the video that you have to download : ")

            try:
                yt = YouTube(url)
                videos = yt.streams.first()
                destination = "E:\\pritish\\Youtube_dowloader"
                videos.download(destination)
                print("The video has been downloaded")
                notify = win10toast.ToastNotifier()
                notify.show_toast("Your YouTube video is Downloaded",
                                  "Go and see it offline", duration=5)
                speak("Your video has been downloaded")

            except:
                print(
                    "ERROR OCCURRED : \n   May be the link you have provided is Invalid\n   Or the video is not downloadable")
                speak(
                    "ERROR OCCURRED : May be the link you have provided is Invalid Or the video is not downloadable")
