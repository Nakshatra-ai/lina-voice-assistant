import speech_recognition as ab
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = ab.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say('Baby,this is, lina')
engine.say('What can I do for you')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with ab.Microphone() as source:
            print('I am listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'lina' in command:
                print(command)
    except:
         pass
    return command

def run_lina():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        print(time)
        talk('Current time is ' + time)
    elif 'what is ' in command:
        matter = command.replace('what is', '')
        info = wikipedia.summary(matter, 1)
        print(info)
        talk(info)
    elif 'who is ' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('I have the pressure of assignments ')
    elif 'are you single' in command:
        talk('I am in a relationship with your laptop')
    elif 'joke' in command:
        talk(pyjokes.get_jokes())
    elif 'recognise' in command:
        talk('You are Abir Mishra')
    elif 'phone number' in command:
        talk ('97xxxxx359')
    elif 'thanks' in command:
        talk ('you are welcome baby')
    else:
        talk('please say again')

while True:
     run_lina()



