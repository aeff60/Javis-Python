import pyttsx3
import speech_recognition as sr
import datetime
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def commands():
    while True:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='th-TH')
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return query

def wishings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")


if __name__ == "__main__":

    wishings()
    query = commands().lower()
    while True:
        if 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}") 

        elif 'open firefox' in query:
            speak("Opening Firefox")
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            try:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                speak("Sorry, I can't find it")
                print("Sorry, I can't find it")

