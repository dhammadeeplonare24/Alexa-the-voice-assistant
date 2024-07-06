import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    while True:
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M%p')
            print(time)
            talk('current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'what ' in command:
            topic = command.replace('what ', '')
            info = wikipedia.summary(topic, 2)
            print(info)
            talk(info)
        elif 'date' in command:
            date = datetime.datetime.now().strftime('%A, %B %d, %Y')
            print(date)
            talk('Today is ' + date)
        elif 'are you single' in command:
            talk('I am in a relationship with Wifi')
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)
        elif 'how are you' in command:
            talk('I am Good, Hope so as you are')
        elif 'hi' in command:
            talk('Hello, How are you....?')
        elif 'who made you' in command:
            talk('Dhammanand Lonare and Achal Raut')
        elif 'purpose' in command:
            talk('for their college mini project')
        elif 'thank you' in command:
            talk('Its my pleasure, Have a Great Day')
        elif 'chrome' in command:
            a = 'opening chrome....'
            engine.say(a)
            engine.runAndWait()
            program = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            subprocess.Popen([program])
        elif 'youtube' in command:
            a = 'opening youtube....'
            engine.say(a)
            engine.runAndWait()
            url = "https://www.youtube.com/"
            webbrowser.open(url)
        else:
            talk('please say it again')

run_alexa()
