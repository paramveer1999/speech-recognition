import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib



engine=pyttsx3.init("sapi5")
""" pyttsx3 helps in taking in build voices in your operating system"""
voices=engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(" hey good morning!")

    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak("Hi i am your virtual assistant.Tell me how may i help you")


def takecommand():
    """IT TAKES INPUT FROM THE USER USING MICROPHONE AND RETURNS STRING OUTPUT"""

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        """ Pause_threshold will let you to speak with your own pace"""

        #r.energy_threshold=500
        """ energy threshold will stop hindrens from outside"""

        audio=r.listen(source)

    try:
        print("In process of recognizing..")
        query=r.recognize_google(audio,language="en-in")
        """ query will take date that has been spoken by user with the help of google API"""
        print("you said :",query)

    except Exception as e:
        print("can you speak this again")
        return "none"
    return query


def sendemail(to,content):
    """ TO ACCESS THIS FUNCTION.FIRST GO TO THIS LINK https://devanswers.co/allow-less-secure-apps-access-gmail-account/ .
    THEN CLICK https://www.google.com/settings/security/lesssecureapps"""
    server=smtplib.SMTP("smtp.gmail.com",587)
    #smtplib module helps in sending accessing gmail smoothly
    server.ehlo()

    server.starttls()

    server.login("YOURgmail.com","YOUR-GMAIL-PASSWORD")

    server.sendmail("YOURgmail.com",to,content)

    server.close()


if __name__=="__main__":

    wishme()
    while True:

        query=takecommand().lower()

        #CODE FOR EXCECUTING TASKS GIVEN BY USERS

        if "wikipedia"in query:

            speak("Getting things ready...")

            query=query.replace("wikipedia"," ")

            results=wikipedia.summary(query,sentences=2)

            speak("As given in wikipedia")
            print(results)
            speak(results)

        elif "youtube" in query:
            webbrowser.open("youtube.com")

        elif "github"in query:
            webbrowser.open("github.com")


        elif "google "in query:
            webbrowser.open("google.com")


        elif "stackoverflow"in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            """ give path for your music directory in variable music_dir"""
            music_dir="C:\\Users\\pc\\Desktop\\songs"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "the time" in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" the time is {time}")

        elif " pycharm" in query:
            """IN THE PATH VARIABLE ADD YOUR FILE PATH YOUR WANT TO OPEN"""
            path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains"
            os.startfile(path)

        elif "email to param" in query:

            try:
                speak("what should i say!")
                content=takecommand()
                to="ADD GMAIL OF THE person to whom message is send"
                sendemail(to,content)
                speak("email has been sent")

            except Exception as e:
                speak("sorry can't send your message")

