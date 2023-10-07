from googletrans import Translator#pip install googletrans==4.0.0-rc1
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound#pip install playsound==1.2.2
import mysql.connector
import keyboard
from tkinter import *
from PIL import Image, ImageTk
import os
import datetime
 
DateAndTime = datetime.datetime.now()
to_lang = Selected_lang = storeInput = Count = mycursor = translator = ""

try: 
    myconn = mysql.connector.connect(
    host="sql9.freesqldatabase.com",
    user="sql9584553",
    password="YgWhetpvQ8",
    database="sql9584553"
    )
    mycursor = myconn.cursor()
except:
    get_sentence = "Internal Server Error, Please try to give your feedback After some time"
    text_to_translate = translator.translate(get_sentence, dest= "en")	
    text = text_to_translate.text
    speak = gTTS(text=text, lang=to_lang, slow= False)
    speak.save("hello.mp3")    
    playsound("hello.mp3")
    os.remove("hello.mp3")
    sys.exit()

#mycursor.execute("CREATE TABLE FunFairFeedBack (id INT AUTO_INCREMENT PRIMARY KEY, Name Varchar(50), City Varchar(50), Institute Varchar(50), Experience Varchar(50), Rating Varchar(2), Feedback Varchar(600))")

####################################################Speak() Method#####################################################

mycursor.execute("SELECT Id FROM FunFairFeedBack ORDER BY Id DESC LIMIT 1")
result = mycursor.fetchone()
Count = result[0]

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.9)
        print("Listening......")
        r.pause_threshold = .5
        audio = r.listen(source)
    
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio)
        print((f"you said: {query.lower()} \n"))
    except Exception as e:
        return "none"
    return query

root = Tk()

def Feedback():
    mycursor.execute("SELECT Id FROM FunFairFeedBack ORDER BY Id DESC LIMIT 1")
    result = mycursor.fetchone()
    Count = result[0]
    to_lang = 'gu'
    translator = Translator()
    get_sentence = "Select Gujarati, hindi or english language for feedback"
    text_to_translate = translator.translate(get_sentence, dest= to_lang)	
    text = text_to_translate.text
    speak = gTTS(text=text, lang=to_lang, slow= False)
    speak.save("ab.mp3")    
    playsound("ab.mp3")
    os.remove("ab.mp3")
    get_sentence = "Speak your selected language name"
    text_to_translate = translator.translate(get_sentence, dest= to_lang)
    text = text_to_translate.text
    speak = gTTS(text=text, lang=to_lang, slow= False)
    speak.save("ab.mp3")    
    playsound("ab.mp3")
    os.remove("ab.mp3")
    Selected_lang = takeCommand().lower()
    while Selected_lang != "gujarati" and Selected_lang != "gujrati" and Selected_lang != "hindi" and Selected_lang != "english" and Selected_lang != "angrezi" and Selected_lang != "gu" and Selected_lang != "hi" and Selected_lang != "en":
        get_sentence = "Speak your selected language name"
    
        text_to_translate = translator.translate(get_sentence, dest= to_lang)
        text = text_to_translate.text
        speak = gTTS(text=text, lang=to_lang, slow= False)
        speak.save("ab.mp3")    
        playsound("ab.mp3")
        os.remove("ab.mp3")
        Selected_lang = takeCommand().lower()
    if "gujarati" in Selected_lang or "gu" in Selected_lang or "gujrati" in Selected_lang:
        to_lang = 'gu'
    
        #Name
        get_sentence = "speak your name"
        text_to_translate = translator.translate(get_sentence, dest= to_lang)
        text = text_to_translate.text
        speak1 = gTTS(text=text, lang=to_lang, slow= False)
        speak1.save("ab.mp3")    
        playsound("ab.mp3")
        os.remove("ab.mp3")
        Name = takeCommand().lower()
        while Name == "none":
            get_sentence = "speak your name"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            Name = takeCommand().lower()
        text_to_translate = translator.translate(Name, dest= 'en')
        Name = text_to_translate.text
        storeInput = gTTS(text=Name, lang=to_lang, slow= False)
        storeInput.save(f"Person{Count}_Name.mp3")  

        #city
        get_sentence = "speak your city name"
    
        text_to_translate = translator.translate(get_sentence, dest= to_lang)
        text = text_to_translate.text
        speak1 = gTTS(text=text, lang=to_lang, slow= False)
        speak1.save("ab.mp3")    
        playsound("ab.mp3")
        os.remove("ab.mp3")
        City = takeCommand().lower()
        while City == "none":
            get_sentence = "speak your city name"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            City = takeCommand().lower()
        text_to_translate = translator.translate(City, dest= 'en')
        City = text_to_translate.text
        storeInput = gTTS(text=City, lang=to_lang, slow= False)
        storeInput.save(f"Person{Count}_City.mp3")
    
        #Institute
        get_sentence = "speak your Institute or designation name"
        text_to_translate = translator.translate(get_sentence, dest= to_lang)
        text = text_to_translate.text
        speak1 = gTTS(text=text, lang=to_lang, slow= False)
        speak1.save("ab.mp3")    
        playsound("ab.mp3")
        os.remove("ab.mp3")
        Institute = takeCommand().lower()
        while Institute == "none":
            get_sentence = "speak your Institute or designation name"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            Institute = takeCommand().lower()
        text_to_translate = translator.translate(Institute, dest= 'en')
        Institute = text_to_translate.text
        storeInput = gTTS(text=Institute, lang=to_lang, slow= False)
        storeInput.save(f"Person{Count}_Institute.mp3")   
    
        #Experience
        get_sentence = "How was your experiece about this funFair?"
        text_to_translate = translator.translate(get_sentence, dest= to_lang)
        text = text_to_translate.text
        speak1 = gTTS(text=text, lang=to_lang, slow= False)
        speak1.save("ab.mp3")    
        playsound("ab.mp3")
        os.remove("ab.mp3")
        get_sentence = "Good or Bad"
        text_to_translate = translator.translate(get_sentence, dest= to_lang)
        text = text_to_translate.text
        speak1 = gTTS(text=text, lang=to_lang, slow= False)
        speak1.save("ab.mp3")    
        playsound("ab.mp3")
        os.remove("ab.mp3")
        Experience = takeCommand().lower()
        while "none" in Experience and "s" not in Experience and "sa" not in Experience and "saro" not in Experience and "kharab" not in Experience and "khara" not in Experience and "kh" not in Experience:
            get_sentence = "How was your experiece about this funFair?"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            get_sentence = "Good or Bad"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            Experience = takeCommand().lower()
        
        if "saro" in Experience or "sa" in Experience or "s" in Experience:
            Experience = "good"
        else:
            Experience = "bad"
    
        text_to_translate = translator.translate(Experience, dest= 'en')
        Experience = text_to_translate.text
        storeInput = gTTS(text=Experience, lang=to_lang, slow= False)
        storeInput.save(f"Person{Count}_Experience.mp3")    
    
        #Rating
        get_sentence = "Give yor rating between 1 to 5 where 1 for very bad and 5 for very good"
        text_to_translate = translator.translate(get_sentence, dest= to_lang)
        text = text_to_translate.text
        speak1 = gTTS(text=text, lang=to_lang, slow= False)
        speak1.save("ab.mp3")    
        playsound("ab.mp3")
        os.remove("ab.mp3")
        Rating = takeCommand().lower()
        while Rating == "none":
            get_sentence = "Give yor rating between 1 to 5 where 1 for very bad and 5 for very good"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            Rating = takeCommand().lower()
        while "ek" not in Rating and "be" not in Rating and "tran" not in Rating and "char" not in Rating and "panch"  not in Rating and "e" not in Rating and "b" not in Rating and "t" not in Rating and "c" not in Rating and "p" not in Rating and "1" not in Rating and "one" not in Rating  and "2" not in Rating and "two" not in Rating and "3" not in Rating and "three" not in Rating and "4" not in Rating and "four" not in Rating and "5" not in Rating and "five" not in Rating:
            get_sentence = "Give yor rating between 1 to 5 where 1 for very bad and 5 for very good"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            Rating = takeCommand().lower()
        if "ek" in Rating or "1" in Rating or "one" in Rating:
            Rating = "1"
        elif "be" in Rating or "2" in Rating or "two" in Rating:
            Rating = "2"
        elif "tran" in Rating or "3" in Rating or "three" in Rating:
            Rating = "3"
        elif "char" in Rating or "4" in Rating or "four" in Rating:
            Rating = "4"
        else:
            Rating = "5"
    
        text_to_translate = translator.translate(Rating, dest= 'en')
        Rating = text_to_translate.text
        storeInput = gTTS(text=Rating, lang=to_lang, slow= False)
        storeInput.save(f"Person{Count}_Rating.mp3")    
        
        #feedback
        get_sentence = "speak your feedback"
        text_to_translate = translator.translate(get_sentence, dest= to_lang)
        text = text_to_translate.text
        speak1 = gTTS(text=text, lang=to_lang, slow= False)
        speak1.save("ab.mp3")    
        playsound("ab.mp3")
        os.remove("ab.mp3")
        Feedback = takeCommand().lower()
        while Feedback == "none":
            get_sentence = "speak your Feedback"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            Feedback = takeCommand().lower()
        text_to_translate = translator.translate(Feedback, dest= 'en')
        Feedback = text_to_translate.text
        storeInput = gTTS(text=Feedback, lang=to_lang, slow= False)
        storeInput.save(f"Person{Count}_Feedback.mp3")     
        try:
            sql = ("INSERT INTO FunFairFeedBack(Name, City, Institute, Experience, Rating, Feedback, DateAndTime) values(%s, %s, %s, %s, %s, %s, %s)")
            val = (Name, City, Institute, Experience, Rating, Feedback, DateAndTime)
            mycursor.execute(sql, val)
            myconn.commit()
            #Submit
            get_sentence = "Thank you for giving your precious feedback, thank you for visiting, have a good day"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak = gTTS(text=text, lang=to_lang, slow= False)
            speak.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
        except:
            get_sentence = "Internal Server error, try to give your feedback again"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak = gTTS(text=text, lang=to_lang, slow= False)
            speak.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
    
    elif "hindi" in Selected_lang or "hi" in Selected_lang:
        to_lang = 'hi'
        #Name
        get_sentence = "speak your name"
        text_to_translate = translator.translate(get_sentence, dest= to_lang)
        text = text_to_translate.text
        speak1 = gTTS(text=text, lang=to_lang, slow= False)
        speak1.save("ab.mp3")    
        playsound("ab.mp3")
        os.remove("ab.mp3")
        Name = takeCommand().lower()
        while Name == "none":
            get_sentence = "speak your city name"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            Name = takeCommand().lower()
        text_to_translate = translator.translate(Name, dest= 'en')
        Name = text_to_translate.text
        storeInput = gTTS(text=Name, lang=to_lang, slow= False)
        storeInput.save(f"Person{Count}_Name.mp3")     
    
        #city
        get_sentence = "speak your city name"
        text_to_translate = translator.translate(get_sentence, dest= to_lang)
        text = text_to_translate.text
        speak1 = gTTS(text=text, lang=to_lang, slow= False)
        speak1.save("ab.mp3")    
        playsound("ab.mp3")
        os.remove("ab.mp3")
        City = takeCommand().lower()
        while City == "none":
            get_sentence = "speak your city name"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            City = takeCommand().lower()
        text_to_translate = translator.translate(City, dest= 'en')
        City = text_to_translate.text
        storeInput = gTTS(text=City, lang=to_lang, slow= False)
        storeInput.save(f"Person{Count}_City.mp3")    
    
        #Institute
        get_sentence = "speak your Institute or designation name"
        text_to_translate = translator.translate(get_sentence, dest= to_lang)
        text = text_to_translate.text
        speak1 = gTTS(text=text, lang=to_lang, slow= False)
        speak1.save("ab.mp3")    
        playsound("ab.mp3")
        os.remove("ab.mp3")
        Institute = takeCommand().lower()
        while Institute == "none":
            get_sentence = "speak your Institute or designation name"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            Institute = takeCommand().lower()
        text_to_translate = translator.translate(Institute, dest= 'en')
        Institute = text_to_translate.text
        storeInput = gTTS(text=Institute, lang=to_lang, slow= False)
        storeInput.save(f"Person{Count}_Institute.mp3")   
    
        #Experience
        get_sentence = "How was your experiece about this funFair?"
        text_to_translate = translator.translate(get_sentence, dest= to_lang)
        text = text_to_translate.text
        speak1 = gTTS(text=text, lang=to_lang, slow= False)
        speak1.save("ab.mp3")    
        playsound("ab.mp3")
        os.remove("ab.mp3")
        get_sentence = "Good or Bad"
        text_to_translate = translator.translate(get_sentence, dest= to_lang)
        text = text_to_translate.text
        speak1 = gTTS(text=text, lang=to_lang, slow= False)
        speak1.save("ab.mp3")    
        playsound("ab.mp3")
        os.remove("ab.mp3")
        Experience = takeCommand().lower()
        while "none" in Experience and "a" not in Experience and "ac" not in Experience and "accha" not in Experience and "bura" not in Experience and "bu" not in Experience and "b" not in Experience:
            get_sentence = "How was your experiece about this funFair?"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            get_sentence = "Good or Bad"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            Experience = takeCommand().lower()
        
        if "achha" in Experience or "ac" in Experience or "a" in Experience:
            Experience = "good"
        else:
            Experience = "bad"
    
        text_to_translate = translator.translate(Experience, dest= 'en')
        Experience = text_to_translate.text
        storeInput = gTTS(text=Experience, lang=to_lang, slow= False)
        storeInput.save(f"Person{Count}_Experience.mp3")    
    
        #Rating
        get_sentence = "Give yor rating between 1 to 5 where 1 for very bad and 5 for very good"
        text_to_translate = translator.translate(get_sentence, dest= to_lang)
        text = text_to_translate.text
        speak1 = gTTS(text=text, lang=to_lang, slow= False)
        speak1.save("ab.mp3")    
        playsound("ab.mp3")
        os.remove("ab.mp3")
        Rating = takeCommand().lower()
        while Rating == "none":
            get_sentence = "Give yor rating between 1 to 5 where 1 for very bad and 5 for very good"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            Rating = takeCommand().lower()
        while "ek" not in Rating and "do" not in Rating and "teen" not in Rating and "char" not in Rating and "panch" not in Rating and "e" not in Rating and "d" not in Rating and 't' not in Rating and "c" not in Rating and "p" not in Rating and "1" not in Rating and "one" not in Rating  and "2" not in Rating and "two" not in Rating and "3" not in Rating and "three" not in Rating and "4" not in Rating and "four" not in Rating and "5" not in Rating and "five" not in Rating:
            get_sentence = "Give yor rating between 1 to 5 where 1 for very bad and 5 for very good"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            Rating = takeCommand().lower()
        if "ek" in Rating or "e" in Rating or "1" in Rating or "one" in Rating:
            Rating = "1"
        elif "do" in Rating or "d" in Rating  or "2" in Rating or "two" in Rating:
            Rating = "2"
        elif "teen" in Rating or "t" in Rating or "3" in Rating or "three" in Rating:
            Rating = "3"
        elif "char" in Rating or "ch" or "4" in Rating or "four" in Rating:
            Rating = "4"
        else:
            Rating = "5"
    
        text_to_translate = translator.translate(Rating, dest= 'en')
        Rating = text_to_translate.text
        storeInput = gTTS(text=Rating, lang=to_lang, slow= False)
        storeInput.save(f"Person{Count}_Rating.mp3")    
    
        #feedback
        get_sentence = "speak your feedback"
        text_to_translate = translator.translate(get_sentence, dest= to_lang)
        text = text_to_translate.text
        speak1 = gTTS(text=text, lang=to_lang, slow= False)
        speak1.save("ab.mp3")    
        playsound("ab.mp3")
        os.remove("ab.mp3")
        Feedback = takeCommand().lower()
        while Feedback == "none":
            get_sentence = "speak your feedback"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            Feedback = takeCommand().lower()
        text_to_translate = translator.translate(Feedback, dest= 'en')
        Feedback = text_to_translate.text
        storeInput = gTTS(text=Feedback, lang=to_lang, slow= False)
        storeInput.save(f"Person{Count}_Feedback.mp3")     
        try:
            sql = ("INSERT INTO FunFairFeedBack(Name, City, Institute, Experience, Rating, Feedback, DateAndTime) values(%s, %s, %s, %s, %s, %s, %s)")
            val = (Name, City, Institute, Experience, Rating, Feedback, DateAndTime)
            mycursor.execute(sql, val)
            myconn.commit()
            #Submit
            get_sentence = "Thank you for giving your precious feedback, thank you for visiting, have a good day"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak = gTTS(text=text, lang=to_lang, slow= False)
            speak.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
        except:
            get_sentence = "Internal Server error, try to give your feedback again"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak = gTTS(text=text, lang=to_lang, slow= False)
            speak.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            os.remove("ab.mp3")
    
    elif "english" in Selected_lang or "en" in Selected_lang or "angrezi" in Selected_lang:
        to_lang = 'en'
    
        #Name
        get_sentence = "speak your name"
        text_to_translate = translator.translate(get_sentence, dest= to_lang)
        text = text_to_translate.text
        speak1 = gTTS(text=text, lang=to_lang, slow= False)
        speak1.save("ab.mp3")    
        playsound("ab.mp3")
        os.remove("ab.mp3")
        Name = takeCommand().lower()
        while Name == "none":
            get_sentence = "speak your name"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            Name = takeCommand().lower()
        text_to_translate = translator.translate(Name, dest= 'en')
        Name = text_to_translate.text
        storeInput = gTTS(text=Name, lang=to_lang, slow= False)
        storeInput.save(f"Person{Count}_Name.mp3")
    
        #city
        get_sentence = "speak your city name"
        text_to_translate = translator.translate(get_sentence, dest= to_lang)
        text = text_to_translate.text
        speak1 = gTTS(text=text, lang=to_lang, slow= False)
        speak1.save("ab.mp3")    
        playsound("ab.mp3")
        os.remove("ab.mp3")
        City = takeCommand().lower()
        while City == "none":
            get_sentence = "speak your city name"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            City = takeCommand().lower()
        text_to_translate = translator.translate(City, dest= 'en')
        City = text_to_translate.text
        storeInput = gTTS(text=City, lang=to_lang, slow= False)
        storeInput.save(f"Person{Count}_City.mp3")
    
        #Institute
        get_sentence = "speak your Institute or designation name"
        text_to_translate = translator.translate(get_sentence, dest= to_lang)
        text = text_to_translate.text
        speak1 = gTTS(text=text, lang=to_lang, slow= False)
        speak1.save("ab.mp3")    
        playsound("ab.mp3")
        os.remove("ab.mp3")
        Institute = takeCommand().lower()
        while Institute == "none":
            get_sentence = "speak your Institute or designation name"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            Institute = takeCommand().lower()
        text_to_translate = translator.translate(Institute, dest= 'en')
        Institute = text_to_translate.text
        storeInput = gTTS(text=Institute, lang=to_lang, slow= False)
        storeInput.save(f"Person{Count}_Institute.mp3")   
    
        #Experience
        get_sentence = "How was your experiece about this funFair?"
        text_to_translate = translator.translate(get_sentence, dest= to_lang)
        text = text_to_translate.text
        speak1 = gTTS(text=text, lang=to_lang, slow= False)
        speak1.save("ab.mp3")    
        playsound("ab.mp3")
        os.remove("ab.mp3")
        get_sentence = "Good or Bad"
        text_to_translate = translator.translate(get_sentence, dest= to_lang)
        text = text_to_translate.text
        speak1 = gTTS(text=text, lang=to_lang, slow= False)
        speak1.save("ab.mp3")    
        playsound("ab.mp3")
        os.remove("ab.mp3")
        Experience = takeCommand().lower()
        while "none" in Experience and "g" not in Experience and "go" not in Experience and "good" not in Experience and "bad" not in Experience and "ba" not in Experience and "b" not in Experience:
            get_sentence = "How was your experiece about this funFair?"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            get_sentence = "Good or Bad"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            Experience = takeCommand().lower()
        
        if "good" in Experience or "go" in Experience or "g" in Experience:
            Experience = "good"
        else:
            Experience = "bad"
    
        text_to_translate = translator.translate(Experience, dest= 'en')
        Experience = text_to_translate.text
        storeInput = gTTS(text=Experience, lang=to_lang, slow= False)
        storeInput.save(f"Person{Count}_Experience.mp3")    
    
        #Rating
        get_sentence = "Give yor rating between 1 to 5 where 1 for very bad and 5 for very good"
        text_to_translate = translator.translate(get_sentence, dest= to_lang)
        text = text_to_translate.text
        speak1 = gTTS(text=text, lang=to_lang, slow= False)
        speak1.save("ab.mp3")    
        playsound("ab.mp3")
        os.remove("ab.mp3")
        Rating = takeCommand().lower()
        while Rating == "none":
            get_sentence = "Give yor rating between 1 to 5 where 1 for very bad and 5 for very good"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            Rating = takeCommand().lower()
        while "1" not in Rating and "one" not in Rating and "2" not in Rating and "two" not in Rating and "3" not in Rating and "three" not in Rating and "4" not in Rating and "four" not in Rating and "5" not in Rating and "five" not in Rating:
            get_sentence = "Give yor rating between 1 to 5 where 1 for very bad and 5 for very good"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            Rating = takeCommand().lower()
        if "1" in Rating or "one" in Rating:
            Rating = "1"
        elif "2" in Rating or "two" in Rating:
            Rating = "2"
        elif "3" in Rating or "three" in Rating:
            Rating = "3"
        elif "4" in Rating or "four" in Rating:
            Rating = "4"
        else:
            Rating = "5"
    
        text_to_translate = translator.translate(Rating, dest= 'en')
        Rating = text_to_translate.text
        storeInput = gTTS(text=Rating, lang=to_lang, slow= False)
        storeInput.save(f"Person{Count}_Rating.mp3")    
    
        #feedback
        get_sentence = "speak your feedback"
        text_to_translate = translator.translate(get_sentence, dest= to_lang)
        text = text_to_translate.text
        speak1 = gTTS(text=text, lang=to_lang, slow= False)
        speak1.save("ab.mp3")    
        playsound("ab.mp3")
        os.remove("ab.mp3")
        Feedback = takeCommand().lower()
        while Feedback == "none":
            get_sentence = "speak your feedback"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak1 = gTTS(text=text, lang=to_lang, slow= False)
            speak1.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")
            Feedback = takeCommand().lower()
        text_to_translate = translator.translate(Feedback, dest= 'en')
        Feedback = text_to_translate.text
        storeInput = gTTS(text=Feedback, lang=to_lang, slow= False)
        storeInput.save(f"Person{Count}_Feedback.mp3") 
    
        try:
            sql = ("INSERT INTO FunFairFeedBack(Name, City, Institute, Experience, Rating, Feedback, DateAndTime) values(%s, %s, %s, %s, %s, %s, %s)")
            val = (Name, City, Institute, Experience, Rating, Feedback, DateAndTime)
            mycursor.execute(sql, val)
            myconn.commit()
            #Submit
            get_sentence = "Thank you for giving your precious feedback, thank you for visiting, have a good day"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak = gTTS(text=text, lang=to_lang, slow= False)
            speak.save("a.mp3")    
            playsound("a.mp3")
            os.remove("a.mp3")
        except:
            get_sentence = "Internal Server error, try to give your feedback again"
            text_to_translate = translator.translate(get_sentence, dest= to_lang)
            text = text_to_translate.text
            speak = gTTS(text=text, lang=to_lang, slow= False)
            speak.save("ab.mp3")    
            playsound("ab.mp3")
            os.remove("ab.mp3")

if __name__ == "__main__":
    translator = Translator()

    def activate():
        while True:
            get_sentence = "Press Enter from keyboard For give your feedback"
            text_to_translate = translator.translate(get_sentence, dest= 'gu')	
            text = text_to_translate.text
            speak = gTTS(text=text, lang='gu', slow= False)
            speak.save("a.mp3")    
            playsound("a.mp3")
            os.remove("a.mp3")
            inputPress = keyboard.read_key()
            if inputPress == 'delete':
                exit()
            while inputPress != 'enter':
                get_sentence = "Press Enter from keyboard For give your feedback"
                text_to_translate = translator.translate(get_sentence, dest= 'gu')	
                text = text_to_translate.text
                speak = gTTS(text=text, lang='gu', slow= False)
                speak.save("b.mp3")    
                playsound("b.mp3")
                os.remove("b.mp3")
            get_sentence = "Welcome to savjani college funfair's IT-Management Department"
            text_to_translate = translator.translate(get_sentence, dest= 'gu')	
            text = text_to_translate.text
            speak = gTTS(text=text, lang='gu', slow= False)
            speak.save("c.mp3")    
            playsound("c.mp3")
            os.remove("c.mp3")
            get_sentence = "I am G Feedbacks 1.0, I'll Accept your feedbacks"
            text_to_translate = translator.translate(get_sentence, dest= 'en')	
            text = text_to_translate.text
            speak = gTTS(text=text, lang='en', slow= False)
            speak.save("d.mp3")    
            playsound("d.mp3")
            os.remove("d.mp3")
            Feedback()
    root.title("G Feedbacks")
    root.iconbitmap("Logo_Icon.ico")
    image  = Image.open("Logo.jpg")
    photo = ImageTk.PhotoImage(image)
    LogoLabel = Label(image = photo)
    LogoLabel.pack()
    Start = Button(root, text="Activate", font="sanserif 19", command=activate)
    Start.pack()
    root.mainloop()