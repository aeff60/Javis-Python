#speech to text using google api
#รับค่าเสียงจากไมค์ เป็นภาษาไทยได้


import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    print("Got it! Now to recognize it...")
    text = r.recognize_google(audio, language="th")
    print(text)