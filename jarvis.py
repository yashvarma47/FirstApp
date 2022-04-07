import datetime
import os
import random


import webbrowser
import pyttsx3
import speech_recognition as sr
import pywhatkit as kit
import pyjokes
import pyautogui
from time import sleep 
import sys 
chrome_path=r"C:\Users\user\AppData\Local\Google\Chrome\Application\chrome.exe" 
webbrowser.register("chrome",None,webbrowser.BackgroundBrowser(chrome_path))


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    tt= datetime.datetime.now().strftime("%I %M %p")
    if hour>=0 and hour<12:
        speak(f"Good Morning!, its {tt}")
    elif hour>=12 and hour<18:
        speak(f"good Afternoon!, its {tt}")
    else:
        speak(f"Good Night!, its {tt}")

    speak("I am Jarvis sir. Please tell me how may I help you ")


def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"Master said: {query}\n")
    
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query 


    

if __name__=="__main__":
    wishMe()
    while True :
    #if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query= query.replace("wikipedia", "")
            results= wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com",1)

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            n=random.randint(0,40)
            music_dir='D:\\instrumental song'
            songs= os.listdir(music_dir)
            print(songs)
           
            os.startfile(os.path.join(music_dir,songs[n]))

        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'hello jarvis' in query:
            speak("Hii Master How May i help u?")
            

        elif 'exit' in query:
            speak("Jarvis Never quits")


        elif 'search' in query:
            speak("what should i search?")
            ans= takeCommand().lower()
            kit.search(f"{ans}")

        elif 'play youtube' in query:
            speak("what should i play?")  
            quest = takeCommand().lower()
            kit.playonyt(f"{quest}")  

        elif 'joke' in query:
            jokes=pyjokes.get_joke()
            speak(jokes)
            print(jokes)

        elif 'close google' in query:
            speak("closing now!")
            os.system(f"taskkill /f /im chrome.exe")

        elif 'window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            
            pyautogui.keyUp("alt")
            pyautogui.press('enter')

        elif 'screenshot' in query:
            im1 = pyautogui.screenshot()
            im2 = pyautogui.screenshot('my_screenshot.png')

        # elif 'down' in query:
            # os.system('shutdown /s')

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'instagram profile'  in query:
            speak("Master please type the username!")
            user_name = input("Master please type the username!")
            webbrowser.open(f"instagram.com/{user_name}")

        elif 'sleep'in query or 'close'in query:
            sys.exit()
        
        

        
        

