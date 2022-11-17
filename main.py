import operator
import time
import PyPDF2
import pyaudio
import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import subprocess
import cv2
import random
from requests import get
import sys
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[len(voices)-3].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I am Cap10 Sir. Please tell me how may I help you. ")
# def userInput():
#     query = input("User input : ")

def takeCommand():
#    userInput()
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source,timeout=4,phrase_time_limit=7)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-us")
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    query = query.lower()
    return query
def news():
    main_url = "https://newsapi.org/v2/everything?q=tesla&from=2021-10-24&sortBy=publishedAt&apiKey=90d94310d8ec4bd6ae9325999e6b55de"
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head =[]
    day = ["first","second","third","forth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["tittle"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")
def pdf_reader():
    book = open('Linux_Basic_Command_book.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"total numbers of pages in the book{pages}")
    speak("Sir please enter the page number i have to read")
    pg = int(input("Please enter the page number : "))
    page =pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)
if __name__ == "__main__":
    wishMe()
    #if 1:
    while True:
        query = takeCommand()
        #print(querys)

        # Logic for executing tasks based on query
        if 'open wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            speak("sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif "open calculator" in query:
            speak("ok sir.")
            subprocess.call("calc.exe")

        elif "close calculator" in query:
            speak("okay sir,closing calculator")
            os.system("taskkill /f /im Calculator.exe")

        elif "open notepad" in query:
            speak("ok sir, opening notepad.")
            subprocess.call("notepad.exe")

        elif "close notepad" in query:
            speak("okay sir,closing notepad")
            pyautogui.leftClick(1160,218,1)

        # elif "close notepad" in query:
        #     speak("okay sir,closing notepad")
        #     os.system("taskkill /f /im notepad.exe")

        elif "open cmd" in query:
            speak("ok sir, opening Command Prompt.")
            subprocess.call("cmd.exe")

        elif "close cmd" in query:
            speak("okay sir,closing Command Prompt")
            os.system("taskkill /f /im cmd.exe")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'play music' in query:
            music_dir = 'F:\\Arefin00'
            songs = os.listdir(music_dir)
            rd =random.choice(songs)
            print(rd)
            os.startfile(os.path.join(music_dir, rd))
        elif 'play video song bangla' in query:
            music_dir = 'F:\\Video Song\\Bangla Song'
            vbsongs = os.listdir(music_dir)
            print(vbsongs)
            os.startfile(os.path.join(music_dir, rd))
        elif 'play video song english' in query:
            music_dir = 'F:\\Video Song\\English Song'
            vesongs = os.listdir(music_dir)
            print(vesongs)
            os.startfile(os.path.join(music_dir, rd))
        elif 'play video song hinde' in query:
            music_dir = 'F:\\Video Song\\Hinde Song'
            vhsongs = os.listdir(music_dir)
            print(vhsongs)
            os.startfile(os.path.join(music_dir, rd))
        elif 'set alarm' in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:
                music_dir = "F:\\Alarm"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))


        elif 'open google' in query:
            speak("ok sir opening google")
            cm = query.lower()
            webbrowser.open(f"{cm}")
            print(cm)


        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")


        elif 'open free codecamp' in query:
            webbrowser.open("free codecamo.org")

        elif 'open w3school' in query:
            webbrowser.open("w3school.com")

        elif 'open bangladesh rail' in query:
            webbrowser.open("eticket.railway.gov.bd")

        elif 'open geeks for geeks' in query:
            webbrowser.open("geeksforgeeks.org")

        elif 'open cricbuzz' in query:
            webbrowser.open("cricbuzz.com")

        elif 'open map' in query:
            webbrowser.open("maps.google.com")

        elif 'open translate' in query:
            webbrowser.open("translate.google.com")

        elif 'open chrome' in query:
            chromePath = "chrome.exe"
            os.startfile(chromePath)

############################################################################
        elif "close chrome" in query:
            speak("okay sir,closing chrome")
            os.system("taskkill /f /im chrome.exe")

        elif 'open brave' in query:
            bravePath = "brave.exe"
            os.startfile(bravePath)

        elif "close brave" in query:
            speak("okay sir,closing brave")
            os.system("taskkill /f /im brave.exe")

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif 'open pycharm' in query:
            pycharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.3\\bin\\pycharm64.exe"
            os.startfile(pycharmPath)
        elif "close pycharm" in query:
            speak("okay sir,closing pycharm")
            os.system("taskkill /f /im pycharm64.exe")

        elif 'open pycharm' in query:
            pycharmPath = "pycharm64.exe"
            os.startfile(pycharmPath)

        elif "close pycharm" in query:
            speak("okay sir,closing pycharm")
            os.system("taskkill /f /im pycharm64.exe")

        elif 'open codeblocks' in query:
            codeblocksPath = "codeblocks.exe"
            os.startfile(codeblocksPath)

        elif "close code block" in query:
            speak("okay sir,closing code block")
            os.system("taskkill /f /im codeblocks.exe")


        elif 'open vs code' in query:
            vsCodePath = "Code.exe"
            os.startfile(vsCodePath)
        elif "close vs code" in query:
            speak("okay sir,closing vs code")
            os.system("taskkill /f /im Code.exe")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret,img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
                cap.release()
                cv2.destroyAllWindows()

        elif 'where i am' in query or  'where we are' in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').txt
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                #print(geo_data)
                city = geo_data['city']
                #state =geo_data['state']
                country = geo_data['country']
                speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry sir, due to network issue i am not able to find where we are.")
                pass

############################################################
        elif 'read pdf' in query:
            pdf_reader()
        elif "IP address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

############################################################
        elif 'do some calculations' in query or 'can you calculate' in query:
            r=sr.Recognizer()
            with sr.Microphone() as source:
                speak("say what you want to calculate, example: 3 plus 3")
                print("listening.....")
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+': operator.add(),
                    '-': operator.sub(),
                    '*': operator.mul(),
                    '/': operator.__truediv__()
                }[op]
            def eval_binary_expr(op1,oper,op2):
                op1,op2 = int(op1),int(op2)
                return get_operator_fn(oper)(op1,op2)
            speak("Your result is : ")
            speak(eval_binary_expr(*(my_string.split())))

        elif "screenshot" in query or "take a screenshot" in query:
            speak("sir, please tall me the name for this screenshot file")
            name = takeCommand().lower()
            speak("please sir hold the screen for few second, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder, now im ready for next command.")
#############################################################################################################
        elif 'tell me a joke' in query:
            joke = pyjokes.get_jokes()
            speak(joke)
        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
#Full screen size.-----------------
        elif "minimize the window" in query:
            speak("ok sir i will do this")
            pyautogui.leftClick(1247, 14, 1)
        elif "max the window" in query:
            speak("ok sir i will do this")
            pyautogui.leftClick(1247, 14, 1)
        elif "close the window" in query:
            speak("ok sir closeing the window")
            pyautogui.leftClick(1247, 14, 1)
        # ---min
        # pyautogui.leftClick(1247,14,1)
        # ---Max
        # pyautogui.leftClick(1293,12,1)
        # ---close
        # pyautogui.leftClick(1341,14,1)
#---------------------------------------------------------------------------
        elif "tell me news" in query:
            speak("please wait sir, feteching the latest news")
            news()
        elif 'sut down the system' in query:
            os.system("shutdown /s /t 5")
        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")
        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'no thanks' in query or 'exit':
            speak("thanks for using me sir, have a good day sir.")
            sys.exit()
        else:
            speak("sir, do you have other work")
# takeCommand()
sys.exit()

#pyautogui.leftClick(1160,218,1)
#close notepad
#print(pyautogui.size())



#kebord shortcut
# pyautogui.press("enter")
# pyautogui.press("shift")
# pyautogui.press("tab")
# pyautogui.press("ctrl")
# pyautogui.press("ese")

##select all
# pyautogui.keyDown("ctrl")
# pyautogui.press("a")
# time.sleep(1)
# pyautogui.keyUp("ctrl")

# time.sleep(3)
# ##select this line
# x,y=pyautogui.position()
# print(x,y)
# pyautogui.leftClick(x,y,2)
# time.sleep(2)
# ##copey
# pyautogui.keyDown("ctrl")
# pyautogui.press("c")
# time.sleep(1)
# pyautogui.keyUp("ctrl")
# time.sleep(5)
# #pest
# pyautogui.keyDown("ctrl")
# pyautogui.press("v")
# time.sleep(1)
# pyautogui.keyUp("ctrl")