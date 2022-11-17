# แปลงข้อความภาษาไทยเป็นเสียงไทย
# โดยใช้โมดูล gTTS

from gtts import gTTS
import os

def speak(text):
    tts = gTTS(text=text, lang='th')
    filename = "voice.mp3"
    tts.save(filename)
    os.system(filename)

speak("สวัสดี")