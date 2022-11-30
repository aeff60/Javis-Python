import pyttsx3 

#pyttsx3 เป็นไลบรารีการแปลงข้อความเป็นคำพูดใน Python 
#มันทำงานแบบออฟไลน์และเข้ากันได้กับทั้ง Python 2 และ 3
import speech_recognition as sr
import datetime
import os

# เริ่มต้นใช้งาน engine ชื่อ sapi5
# sapi5 เทคโนโลยีสำหรับ voice recognition และ synthesis โดย Microsoft
# voice recognition คือ การแปลงเสียงเป็นข้อความ
# synthesis คือ การแปลงข้อความเป็นเสียง
# ในกรณีนี้เราจะใช้เพื่อให้เสียงออกมา

engine = pyttsx3.init('sapi5') 



# รับลิสต์เสียงสำหรับ engine
#  engine.getProperty คือ แสดงรายชื่อเสียงที่สามารถใช้งานได้
voices = engine.getProperty('voices')

# เลือกเสียงแรกที่ใช้ได้ จาก voices[0] 0 คือตำแหน่งที่ 1
engine.setProperty('voice', voices[0].id)

#ฟังก์ชั่นในการพูด
def speak(audio): 
    engine.say(audio) #พูดตามข้อมูลที่อยู่ในตัวแปล audio
    engine.runAndWait() #รอให้เสียงเล่นจบ

def commands():
    

    r=sr.Recognizer() # สร้างตัวแปร r เพื่อรับค่าจากการฟัง 
      
    with sr.Microphone() as source: # ใช้ไมโครโฟนเป็น source ในการรับเสียง 
        print("Listening...")
        # ปรับความไวของตัวจำแนกตามเสียงรบกวนรอบข้างและบันทึกเสียง
        r.pause_threshold = 1 # หยุดรอคำสั่ง 1 วินาที
        r.adjust_for_ambient_noise(source, duration=1) # ปรับระดับเสียงรบกวน 1 วินาที 
        audio = r.listen(source) # รับเสียงจากไมโครโฟน

    try: # ถ้ารับเสียงได้
        print("Recognizing...")
        # อินสแตนซ์ของ Recognizer โดยใช้ Google Speech Recognition AP
        query = r.recognize_google(audio, language='en-EN') # ภาษาไทย 

        print(f"User said: {query}\n")# แสดงข้อความที่เราพูด ในคอนโซล

    except Exception as e: # ถ้าไม่มีการพูด
        print(e) # แสดงข้อความ error 
        print("Say that again please...")# แสดงข้อความ พูดใหม่ 
        return "None"# คืนค่า None 
    return query# คืนค่า query

# ฟังก์ชั่นนี้ต้องการให้ผู้ใช้ตามเวลาของวัน
def wishings():
    # รับชั่วโมงปัจจุบัน
    hour = int(datetime.datetime.now().hour)
    # ถ้าชั่วโมงอยู่ระหว่าง 0 ถึง 12, ให้พูดว่า Good Morning
    if hour>=0 and hour<12:
        speak("Good Morning!")

    # ถ้าชั่วโมงอยู่ระหว่าง 12 ถึง 18, ให้พูดว่า Good Afternoon
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    # มิฉะนั้น, ให้พูดว่า Good Evening
    else:
        speak("Good Evening!")  

    #สุดท้ายนี้ขอให้ผู้ใช้ พูดว่า สวัสดี และ ชื่อของผู้ใช้
    speak("I am Jarvis Sir. Please tell me how may I help you")

if __name__ == "__main__":

    
    while True:
        wishings()# ให้เรียกใช้ฟังก์ชั่น wishings
        query = commands().lower()# รับคำสั่งจากฟังก์ชั่น commands และเปลี่ยนเป็นตัวพิมพ์เล็กทั้งหมด
        if 'time' in query:  
         
            # ใช้เมธอด now() เพื่อรับเวลาปัจจุบันมาและเมธอด strftime() เพื่อทำให้เวลาอยู่ในรูปแแบบข้อความ
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            # ใช้ฟังก์ชัน speak() เพื่อพูดเวลา
            speak(f"Sir, the time is {strTime}") 

        elif 'open browser' in query:
            # ใช้ฟังก์ชัน speak() เพื่อพูดว่า กำลังเปิด Firefox
            speak("Opening Browser")
            # ใช้ฟังก์ชัน webbrowser.open() เพื่อเปิด Firefox
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
