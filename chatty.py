import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print("Listening....")
        audio = r.listen(source, phrase_time_limit=10)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language = 'en-in')
        print(query)
        
    except Exception as e:
        print(e)
        speak('Please say that again')
        return "None"
    
    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%I:%M")
    speak('The current time is')
    speak(time)


def date():
    year = int(datetime.datetime.now().year)
    mon = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak('Today is')
    speak(day)
    speak(mon)
    speak(year)
    
def hours():
    hourspeak = ''    
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        hourspeak = 'Good morning Sir!'
    elif hour>=12 and hour<17:
        hourspeak = 'Good afternoon Sir!'
    else:
        hourspeak = 'Good evening Sir!'
    speak(hourspeak)
        
def greeting():
    speak('Welcome back!')
    hours()
    speak('How may I help you?')

def wiki():
    speak('searching')
    print('Searching....')
    wikisearch=''
    wikisearch = wikisearch.replace('wikipedia',' ')
    result = wikipedia.summary(query, sentences = 2)
    print(result)
    speak(result)

def ChromeSearch():
    speak('What should I search for?')
    search = TakeCommand()
    chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    wb.register('chrome', None, wb.BackgroundBrowser(chromepath))
    wb.get('chrome').open_new_tab(search+'.com')

def notes():
    speak("what should I remind you about?")
    data = TakeCommand()
    speak("I will remind you " +data)
    remind = open('data.txt', 'w')
    remind.write(data)
    remind.close()
    
def reminder():
    rem = open('data.txt', 'r')
    speak("You told me to remind you"+rem.read())
    rem.close()  
    
def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\govind\\Documents\\ss.png")
    speak("Done!")

def info():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage + "percent")
    battery = psutil.sensors_battery()
    speak("The battery is at ")
    speak(battery.percent)
    speak("percent")
    
def joke():
    speak(pyjokes.get_joke())
    
if __name__ == '__main__':
    greeting()
    while True:
        query = TakeCommand().lower()
        
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'search' in query:
            wiki()
        elif 'chrome' in query:
            ChromeSearch()
        elif 'logout' in query:
            os.system("shutdown -l")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'remind' in query:
            notes()
        elif 'something' in query:
            reminder()
        elif 'screenshot' in query:
            screenshot()
        elif 'performance' in query:
            info()
        elif 'joke' in query:
            joke()
        elif 'bye' in query:
            speak('see you later!')
            break
        
            