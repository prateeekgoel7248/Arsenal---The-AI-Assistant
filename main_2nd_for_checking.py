# Using Mysql commands to store data in a database.
import datetime
import getpass
import operator
# from datetime import datetime
import os
import random
import smtplib
import sys
import time
# import csv
# import time
import webbrowser
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import PyPDF2
import cv2
import instaloader as instaloader
import mysql.connector as c
import numpy as np
import psutil
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit as kit
# import pyaudio
import requests
import speech_recognition as sr
import speedtest as speedtest
import wikipedia
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtWidgets import *
from bs4 import BeautifulSoup
# import pandas as pd
# from numpy import spacing
from pywikihow import search_wikihow
from requests import get

import MyAlarm
import Twitter_Bot
# from PyQt5.uic import loadUi
# from PyQt5.uic import loadUiType
from GUI_2nd_Time import Ui_MainWindow

# from PyQt5.uic import ui

# database
con = c.connect(host="localhost", user="root", passwd="", database="arsenal")
cursor = con.cursor()
# cursor =''

# from datetime import date

# import bullet
# from bullet import VerticalPrompt,Password
# it works only on linux
# pyttsx3 - for engine , speak function


engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices)
# print(voices[1].id)
engine.setProperty('voice', voices[3].id)

# data of members

names = ["prateek", "prachi", "ujjawal", "prerna", "shubhankar", "yash", "deepanshi", "himanshu", "anirudh", "aaradhya",
         'aayush', 'neeraj', 'kailash']

numbers = [['+91 72488 44385', 'prateek.goel.cs.2019@mitmeerut.ac.in'],
           ['+91 76685 11296', 'prachi.cs.2019@mitmeerut.ac.in'],
           ['+91 86302 24424', 'ujjawal.jindal.cs.2019@mitmeerut.ac.in'],
           ['+91 76687 73430', 'prerna.choudhary.cs.2019@mitmeerut.ac.in'],
           ['+91 98971 53347', 'shubhankar.mittal.cs.2019@mitmeerut.ac.in'],
           ['+91 84399 45310', 'yash.bansal.cs.2019@mitmeerut.ac.in'],
           ['+91 84330 99203', 'deepanshi.pal.cs.2019@mitmeerut.ac.in'],
           ['+91 97603 82653', 'himanshu.cs.2019@mitmeerut.ac.in'],
           ['+91 6396 189 212', 'anirudh.verma.cs.2019@mitmeerut.ac.in'],
           ['+91 79064 27794', 'aaradhya.saini.cs.2019@mitmeerut.ac.in'],
           ['+91 99979 62331', 'ayush.singhal@mitmeerut.ac.in'], ['+91 98973 35329', 'neeraj.pratap@mitmeerut.ac.in'],
           ['+91 86304 30234', 'kailash.tripathi@mitmeerut.ac.in']]

phone_dict = dict(zip(names, numbers))

GREETINGS = ["hello arsenal", "arsenal", "wake up arsenal", "you there arsenal", "time to work arsenal", "hey arsenal",
             "ok arsenal", "are you there"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]


# engine.setProperty('rate',180)


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.MainFunction()

    # text to speech
    def speak(self, audio):
        engine.say(audio)
        print(audio)
        engine.runAndWait()

    # for taking command from the user

    # To convert voice to text

    def wish(self):
        hour = int(datetime.datetime.now().hour)
        date = str(datetime.datetime.now().date())
        # self.speak(date)
        birth = '2021-09-25'
        # if date == birth:
        #     self.speak('Happy Birthday sir, thanks for made me')
        ti = time.strftime("%I:%M %p")
        if 0 <= hour < 12:
            self.speak(f"Good Morning sir , its {ti}")
        elif 12 <= hour < 18:
            self.speak(f"Good Afternoon sir , its {ti}")
        else:
            self.speak(f"Good Evening sir , its {ti}")
        self.speak("I am Arsenal sir. please tell me how can i help you ..")

    def news(self):
        main_url = 'https://newsapi.org/v2/everything?q=tesla&from=2021-06-17&sortBy=publishedAt&apiKey=9d65eb3b6e934fb5ac892018a162fbe8'
        main_page = requests.get(main_url).json()

        articles = main_page['articles']

        head = []
        day = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eight', 'ninth', 'tenth']
        for ar in articles:
            head.append(ar['title'])
        for i in range(len(day)):
            self.speak(f"today's {day[i]} news is: {head[i]}")

    def pdf_reader(self):
        book = open('pyt.PDF', 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        self.speak(f"Total number of pages in this pdf is {pages} ")
        self.speak(f"sir please enter the page number i have to read")
        pg = int(input("Please enter the page number: "))
        page = pdfReader.getPage(pg - 1)
        text = page.extractText()
        self.speak(text)

    def MathematicalCalculation(self):
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                self.speak('Say what you want to calculate, example: 3 plus 5')
                print('Listening...')
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)

            def get_operator_fn(op):
                return {
                    '+': operator.add,
                    '-': operator.sub,
                    '*': operator.mul,
                    'divided': operator.__truediv__,
                }[op]

            def eval_binary_expr(op1, oper, op2):
                op1, op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)

            self.speak('Your result is')
            self.speak(eval_binary_expr(*(my_string.split())))

        except Exception as e:
            print(e)
            self.speak('sorry sir, i am unable to do that calculation')

    def MathsCalculation(self, query):
        calList = query.split()

        try:
            my_string = str(calList[-3]) + ' ' + str(calList[-2] + ' ' + str(calList[-1]))

            def get_operator_fn(op):
                return {
                    '+': operator.add,
                    '-': operator.sub,
                    '*': operator.mul,
                    'X': operator.mul,
                    'into': operator.mul,
                    'divide': operator.__truediv__,
                    'divided': operator.__truediv__,
                }[op]

            def eval_binary_expr(op1, oper, op2):
                op1, op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)

            self.speak('Your result is')
            self.speak(eval_binary_expr(*(my_string.split())))

        except Exception as e:
            print(e)
            self.speak('sorry sir, i am unable to do that calculation')

    def FaceRecognition(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()  # Local Binary Patterns Histograms
        recognizer.read('trainer/trainer.yml')  # load trained model
        # cascadePath = "hdf123.xml"
        cascadePath = 'hdf123.xml'
        faceCascade = cv2.CascadeClassifier(cascadePath)  # initializing haar cascade for object detection approach

        font = cv2.FONT_HERSHEY_SIMPLEX  # denotes the font type

        # id = 4  # number of persons you want to Recognize

        names = ['', 'Prateek', 'Prachi', 'Prerna', 'Ujjwal']  # names, leave first empty bcz counter starts from 0

        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # cv2.CAP_DSHOW to remove warning
        cam.set(3, 640)  # set video FrameWidth
        cam.set(4, 480)  # set video FrameHeight

        # Define min window size to be recognized as a face
        minW = 0.1 * cam.get(3)
        minH = 0.1 * cam.get(4)

        # flag = True

        while True:

            ret, img = cam.read()  # read the frames using the above created object

            converted_image = cv2.cvtColor(img,
                                           cv2.COLOR_BGR2GRAY)  # The function converts an input image from one color
            # space to another

            faces = faceCascade.detectMultiScale(
                converted_image,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(minW), int(minH)),
            )

            for (x, y, w, h) in faces:

                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # used to draw a rectangle on any image

                id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])  # to predict on every single image

                # Check if accuracy is less them 100 ==> "0" is perfect match
                if 100 > accuracy > 10:
                    id = names[id]
                    accuracy = "  {0}%".format(round(100 - accuracy))
                    MainThread.TaskExecution(self)

                else:
                    id = "unknown"
                    accuracy = "  {0}%".format(round(100 - accuracy))

                cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
                cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

            cv2.imshow('camera', img)

            k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
            if k == 27:
                break

        # Do a bit of cleanup
        print("Thanks for using this program, have a good day.")
        cam.release()
        cv2.destroyAllWindows()

    def AccuracyOfFace(self):
        try:
            recognizer = cv2.face.LBPHFaceRecognizer_create()  # Local Binary Patterns Histograms
            recognizer.read('trainer/trainer.yml')  # load trained model
            # cascadePath = "hdf123.xml"
            cascadePath = 'hdf123.xml'
            faceCascade = cv2.CascadeClassifier(cascadePath)  # initializing haar cascade for object detection approach

            font = cv2.FONT_HERSHEY_SIMPLEX  # denotes the font type

            id = 4  # number of persons you want to Recognize

            names = ['', 'Prateek', 'Prachi', 'Prerna', 'Ujjwal']  # names, leave first empty bcz counter starts from 0

            cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # cv2.CAP_DSHOW to remove warning
            cam.set(3, 640)  # set video FrameWidth
            cam.set(4, 480)  # set video FrameHeight

            # Define min window size to be recognized as a face
            minW = 0.1 * cam.get(3)
            minH = 0.1 * cam.get(4)

            # flag = True
            counterflag = 0
            Accuracy = 0

            while True:
                counterflag += 1
                ret, img = cam.read()  # read the frames using the above created object

                converted_image = cv2.cvtColor(img,
                                               cv2.COLOR_BGR2GRAY)  # The function converts an input image from one color
                # space to another

                faces = faceCascade.detectMultiScale(
                    converted_image,
                    scaleFactor=1.2,
                    minNeighbors=5,
                    minSize=(int(minW), int(minH)),
                )

                for (x, y, w, h) in faces:

                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # used to draw a rectangle on any image

                    id, accuracy = recognizer.predict(
                        converted_image[y:y + h, x:x + w])  # to predict on every single image

                    # Check if accuracy is less them 100 ==> "0" is perfect match
                    Accuracy = accuracy
                    if 100 > accuracy > 20:
                        # self.speak('Verification successful')
                        id = names[id]
                        accuracy = "  {0}%".format(round(100 - accuracy))
                        break

                    else:
                        id = "unknown"
                        accuracy = "  {0}%".format(round(100 - accuracy))

                    cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
                    cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

                cv2.imshow('camera', img)

                k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
                if k == 27:
                    break
                elif Accuracy > 20:
                    break
                elif counterflag > 100:
                    break

            # Do a bit of cleanup
            # print("Thanks for using this program, have a good day.")
            cam.release()
            cv2.destroyAllWindows()
            return Accuracy
        except Exception as e:
            print(e)
            return 15

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 2
            # agr hum khi ruke toh humara Arsenal wait krega 2 sec ke liye
            audio = r.listen(source, timeout=5, phrase_time_limit=8)

        try:
            print("Recognizing....")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"User said : {self.query}")

        except Exception as e:
            self.speak("Say that again please...")
            return "none sir"
        current_moment = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        count = 1
        try:
            self.query_data = "insert into arsn_data(query,count,date_time) values('{}',{},'{}')".format(
                self.query, count,
                current_moment)
            cursor.execute(self.query_data)
        except Exception as e:
            # self.query='how are you prateek?'
            self.query_update = "update arsn_data set count = count + 1 where query = '{}'".format(self.query)
            self.query_update1 = "update arsn_data set query_time = '{}' where query = '{}'".format(
                current_moment, self.query)
            cursor.execute(self.query_update)
            cursor.execute(self.query_update1)
        con.commit()

        return self.query.lower()

    def MainFunction(self):
        Accur = self.AccuracyOfFace()
        print('Accuracy of Face Recognition :', Accur, '%')
        if Accur > 20:
            # print(Accur)
            self.TaskExecution()
        else:
            self.speak('sorry sir but i am not able to recognizes you face')
            self.speak('please enter your password')
            # n=("Enter Your Password : ")
            password_real = 'ArsenalAI'
            count = 0
            while count < 3:
                # cli = VerticalPrompt(
                #     [
                #         Password(prompt='Enter your password : ', hidden="😵")
                #     ], spacing=0) #only works on linux
                # this will only work in terminal not on console
                main_pass = getpass.getpass()
                if main_pass == password_real:
                    self.speak('Authentication successful')
                    self.TaskExecution()
                    break
                else:
                    count = count + 1
                    count_left = 3 - count
                    self.speak(f"You have entered wrong password sir ,you have {count_left} more attempts left")
            if count == 3:
                self.speak("sorry sir but you can't access the program")

    def TaskExecution(self):
        self.wish()

        while True:
            self.query = self.takecommand().lower()

            # Tasks for performing

            if 'open notepad' in self.query:
                npath = 'C:\\Windows\\system32\\notepad.exe'
                os.startfile(npath)
                self.speak("Opening notepad..")

            elif 'hello' in self.query:
                self.speak('hello sir')

            elif 'how are you' in self.query:
                self.speak('i am fine sir , thanks for asking')
                # os.system("taskkill /f /im notepad.exe")

            elif 'tell me a joke' in self.query:
                joke = pyjokes.get_joke()
                self.speak(joke)

            elif "today's" in self.query or "today's date" in self.query or "today date" in self.query:
                day = time.strftime('%A')
                date = datetime.datetime.now()
                self.speak(f"sir , it's {day} and {date}")

            elif 'what are you doing' in self.query:
                self.speak('i am just trying to help you ,sir')

            elif 'close notepad' in self.query:
                self.speak('okay sir , closing notepad')
                os.system("taskkill /f /im notepad.exe")

            elif 'open history' in self.query or 'show database' in self.query or 'show history' in self.query or 'show me history' in self.query or 'show me my last search' in self.query or 'show me my history' in self.query or 'show me' in self.query:
                self.speak('look into camera sir')
                accuracy_for_history = self.AccuracyOfFace()
                if accuracy_for_history > 50:
                    self.speak('showing you history sir ...')
                    # arsen = pd.read_csv('ArsenalData.csv')
                    arsen = "select *from arsn_data"
                    cursor.execute(arsen)
                    print("Id\tQuery\t\tCount\tDate & Time")
                    for row in cursor:
                        print(row[0], "\t", row[1], "\t\t", row[2], "\t", row[3])
                        # print(row[3])
                    con.commit()

                else:
                    self.speak('sorry sir ,i am not able to show you the history')
            elif 'delete database' in self.query or 'delete history' in self.query or 'delete search' in self.query or 'remove history' in self.query or 'remove database' in self.query or 'remove search' in self.query:
                self.speak('look into camera sir')
                accuracy_for_history = self.AccuracyOfFace()
                if accuracy_for_history > 50:
                    self.speak('sir are you sure to delete all searches?')
                    self.query3 = self.takecommand().lower()
                    if 'yes' in self.query3 or 'sure' in self.query3 or 'delete' in self.query3:
                        self.speak('Deleting the history sir..')
                        arsena = "delete from arsn_data"
                        cursor.execute(arsena)
                        con.commit()
                        self.speak('history deleted.')
                    elif 'no' in self.query3 or 'not' in self.query3:
                        self.speak('ok sir i am not deleting the history')
                    else:
                        self.speak('ok sir')
                else:
                    self.speak('Sorry sir but i am not able to delete the history.')
            elif self.query in GREETINGS:
                self.speak(random.choice(GREETINGS_RES))

            elif 'open command prompt' in self.query:
                os.system('start cmd')
                self.speak("Opening command prompt..")

            elif 'birthday' in self.query or 'birth date' in self.query:
                birth_date = date.fromisoformat('2002-09-25')
                self.speak(f"your birth date is {birth_date} sir")
                if date.today().month == birth_date.month:
                    if date.today().day == birth_date.day:
                        self.speak('Happy birthday sir! i hope you will achieve everything in your life')
                    elif birth_date.day > date.today().day:
                        self.speak('your birthday is coming sir!')
                        self.speak('sir if you want i can cancel all your meeting for your birthday sir')
                else:
                    if date.today().month > birth_date.month:
                        # self.speak
                        self.speak(
                            f"for your birthday {(date.today() - birth_date.replace(year=date.today().year)).days} days are left sir")
                    else:
                        self.speak(
                            f"for your birthday {(birth_date.replace(year=date.today().year) - date.today()).days} days are left sir")

            elif 'close command prompt' in self.query or 'close cmd' in self.query:
                self.speak('okay sir , closing notepad')
                os.system("close cmd")
            elif 'open visual studio' in self.query:
                npath = 'C:\\Users\\parte\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe'
                os.startfile(npath)
                self.speak("Opening visual studio..")
            elif 'open camera' in self.query:
                cap = cv2.VideoCapture(0)
                # 0 for internal camera and one for external camera
                while True:
                    reg, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(58)
                    if k == 27:
                        break
                cap.release()
                cv2.destroyAllWindows()
            elif 'play music' in self.query or 'play song' in self.query or 'play a song' in self.query or 'play some music' in self.query:
                music_dir = 'C:\\Users\\parte\\Music'
                songs = os.listdir(music_dir)
                # rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3' or '.mpeg' or '.MPEG'):
                        self.speak(f"playing {song}")
                        os.startfile(os.path.join(music_dir, song))
                        break

            elif 'set alarm to' in self.query or 'set alarm for' in self.query:
                # self.speak('sir please tell me the time to set alarm. for example , set alarm for 5:30 AM')
                tt = self.query
                try:
                    # tt = self.takecommand()
                    tt = tt[-10:]
                    # print(tt)
                    tt = tt.replace('.', '')
                    tt = tt.replace(' ', ':')
                    tt = tt.upper()
                    MyAlarm.alarm(tt)
                except Exception as e:
                    self.speak("sorry sir , i am unable to set your alarm")
                    print(e)

            elif 'set alarm ' in self.query or 'alarm' in self.query:
                self.speak('sir please tell me the time to set alarm. for example , set alarm to 5:30 AM')
                try:
                    tt = self.takecommand()
                    tt = tt.replace('set alarm to ', "")
                    tt = tt.replace('.', '')
                    tt = tt.replace(' ', ':')
                    tt = tt.upper()
                    print(tt)
                    MyAlarm.alarm(tt)
                except Exception as e:
                    print(e)
                    self.speak("sorry sir , i am unable to set your alarm")

                # ho = int(datetime.datetime.now().hour)
                # if ho == 7:
                #     music_dir = 'C:\\Users\\parte\\Music'
                #     songs = os.listdir(music_dir)
                #     # rd = random.choice(songs)
                #     for song in songs:
                #         if song.endswith('.mp3' or '.mpeg' or '.MPEG'):
                #             self.speak(f"playing {song}")
                #             os.startfile(os.path.join(music_dir, song))

            elif 'ip address' in self.query:
                ip = get('https://api.ipify.org')
                self.speak(f"your ip address is {ip}")

            elif 'open mobile camera' in self.query:
                import urllib.request

                # import cv2
                # import numpy as np
                # import time
                URL = "http://192.168.74.217:8080/shot.jpg"
                while True:
                    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
                    img = cv2.imdecode(img_arr, -1)
                    cv2.imshow('IPWebcam', img)
                    q = cv2.waitKey(1)
                    if q == ord('q'):
                        break

                cv2.destroyAllWindows()

            elif 'thank you' in self.query:
                self.speak("its my pleasure sir")

            elif 'on google' in self.query:
                cm = self.query.replace('on google', '')
                kit.search(cm)

            elif 'hide all my files' in self.query or 'hide all files' in self.query or 'hide this folder' in self.query or 'visible for everyone' in self.query:
                self.speak('sir please tell me you want to hide this folder or make it visible for everyone')
                condition = self.takecommand().lower()
                if 'hide' in condition:
                    os.system("attrib +h /s /d")
                    self.speak('sir, all the files in this folder are now hidden.')

                elif 'visible' in condition:
                    os.system('attrib -h /s /d')
                    self.speak('sir, all the files in this folder are visible to everyone')

                elif 'leave it' in condition or 'leave it now' in condition:
                    self.speak('ok sir')

            elif 'wikipedia' in self.query or 'who is' in self.query:
                self.speak('searching wikipedia...')
                if 'wikipedia' in self.query:
                    self.query = self.query.replace('wikipedia', '')
                if 'who is' in self.query:
                    self.query = self.query.replace('who is', '')
                if 'according to' in self.query:
                    self.query = self.query.replace('according to', '')

                results = wikipedia.summary(self.query, sentences=3)
                self.speak(f'according to wikipedia {results}')
                # self.speak(results)

            elif 'send sms' in self.query or 'send message using message' in self.query:
                self.speak('sir , what should i send ?')
                msz = self.takecommand()

                from twilio.rest import Client

                account_sid = 'AC31be20080d2596193c5af81bd9ceb0fc'
                auth_token = '44469f2f8fd2815e0f7da58ff108f711'

                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                    body=msz,
                    from_="+12408835781",
                    to='13'
                )
                print(message.sid)

                # pass

            elif 'open youtube' in self.query:
                self.speak("Opening youtube..")
                webbrowser.open('www.youtube.com')

            elif 'open facebook' in self.query:
                self.speak("Opening facebook..")
                webbrowser.open('www.facebook.com')

            elif 'open stack overflow' in self.query:
                self.speak("Opening stack overflow..")
                webbrowser.open('www.stackoverflow.com')

            elif 'open instagram' in self.query:
                self.speak("Opening instagram..")
                webbrowser.open('www.instagram.com')

            elif 'open twitter' in self.query:
                self.speak("Opening twitter..")
                webbrowser.open('www.twitter.com')

            elif 'open google' in self.query:
                self.speak('sir, what should i search on google')
                cm = self.takecommand().lower()
                webbrowser.open(f'{cm}')

            elif 'send message' in self.query or 'on whatsapp' in self.query:
                self.speak('Look into camera sir')
                Accur = self.AccuracyOfFace()
                if Accur > 45:
                    hour = int(datetime.datetime.now().hour)
                    minute = int(datetime.datetime.now().minute)
                    self.speak('Whom you want to send message on whatsapp sir ?')
                    self.query_wht = self.takecommand().lower()
                    if self.query_wht in phone_dict.keys():
                        number_wht = phone_dict[self.query_wht][0]
                        self.speak('sir, what should i send on whatsapp')
                        cm = self.takecommand().lower()
                        kit.sendwhatmsg(number_wht, cm, hour, minute + 2)

                    else:
                        self.speak('sorry sir but i did not find any contact by this name..')
                else:
                    self.speak("sorry sir i am not able to recognize your face , you can't send message")

            elif 'play song on youtube' in self.query:
                self.speak('sir, what should i play on youtube')
                cm = self.takecommand().lower()
                kit.playonyt(cm)

            elif 'switch the window' in self.query:
                # self.speak('i am fine sir , thanks for asking')
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                time.sleep(2)
                pyautogui.keyUp('alt')

            elif 'tell me news' in self.query:
                self.speak('please wait sir , fetching the latest news')
                self.news()

            elif 'weather' in self.query or 'temperature' in self.query:
                search = self.query
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, 'html.parser')
                temp = data.find("div", class_="BNeawe").text
                self.speak(f"current temperature is {temp}")

            elif 'on youtube' in self.query:
                self.query = self.query.replace('play', '')
                self.speak(f'playing{self.query}')
                self.query = self.query.replace('on youtube', '')
                kit.playonyt(self.query)

            elif 'volume up' in self.query or 'volume increase' in self.query:
                pyautogui.press("volumeup")

            elif 'volume down' in self.query or 'volume decrease' in self.query:
                pyautogui.press("volumedown")

            elif 'volume mute' in self.query or 'mute' in self.query:
                pyautogui.press('mute')

            elif 'email to' in self.query or 'email' in self.query or 'mail' in self.query:
                self.speak('Whom you want to send email sir ?')
                self.query_wht = self.takecommand().lower()
                if self.query_wht in phone_dict.keys():
                    to = phone_dict[self.query_wht][1]
                    self.speak('sir, what should i say?')
                    message = self.takecommand().lower()
                    if 'send a file' in message:
                        email = 'gkbr221698@gmail.com'
                        password = 'pg.vijay'
                        # to = 'parteekgoyal.8057996696@gmail.com'
                        self.speak('okay sir, what is the subject for this email say?')
                        self.query = self.takecommand().lower()
                        subject = self.query
                        self.speak('and sir, what is the message for this email say?')
                        self.query2 = self.takecommand().lower()
                        message = self.query2
                        self.speak('sir, please enter the correct path of the file into the shell')
                        file_location = input("Please enter the path here : ")

                        self.speak('please wait , i am sending the email now')

                        msg = MIMEMultipart()
                        msg['From'] = email
                        msg['To'] = to
                        msg['Subject'] = subject

                        msg.attach(MIMEText(message, 'plain'))

                        # setup the attachment

                        filename = os.path.basename(file_location)
                        attachment = open(file_location, 'rb')
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)

                        # attach the attachment to the Mimemultipart object

                        msg.attach(part)

                        server = smtplib.SMTP("smtp.gmail.com", 587)
                        # server.ehlo()
                        server.starttls()
                        server.login(email, password)
                        text = msg.as_string()

                        server.sendmail(email, to, text)
                        server.quit()
                        self.speak(f"Email has been send to {to}")

                        # pass

                    else:
                        email = 'gkbr221698@gmail.com'
                        password = 'pg.vijay'
                        # to = 'parteekgoyal.8057996696@gmail.com'
                        message = self.query  # message

                        server = smtplib.SMTP("smtp.gmail.com", 587)
                        # server.ehlo()
                        server.starttls()
                        server.login(email, password)
                        server.sendmail(email, to, message)
                        server.quit()
                        self.speak(f"Email has been send to {to}")
                else:
                    self.speak('sorry sir but i did not find any contact by this name')
                    # try:
                    #     self.speak('sir, what should i say?')
                    #     content = self.takecommand().lower()
                    #     to = 'parteekgoyal.8057996696@gmail.com'
                    #     # sendEmail(to,content)
                    #     self.speak(f"Email has been send to {to}")
                    #
                    # except Exception as e:
                    #     print(e)
                    #     self.speak(f"Sorry Sir, I am not able to send this message to {to}")

            elif 'internet speed' in self.query or 'speed of internet' in self.query or 'net speed' in self.query:
                self.speak('ok sir ,checking internet speed')
                try:
                    st = speedtest.Speedtest()
                    dl = st.download() // 8192
                    up = st.upload() // 8192
                    if dl > 5100 and up > 5100:
                        self.speak('sir we have very good internet speed')

                    elif 5100 > dl > 1024 and 5100 > up > 1024:
                        self.speak('sir we have good internet speed')
                    else:
                        self.speak("sir we don't have a good internet speed")
                    self.speak(f'we have {dl} KB per second downloading speed and {up} KB per second uploading speed')
                except Exception as e:
                    print(e)
                    self.speak('sorry sir , i am not able to find internet speed')

                # we can use os.system('cmd /k "speedtest"') but it will exit our program

            elif 'how much battery left' in self.query or 'battery percentage' in self.query or 'battery' in self.query or 'power' in self.query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                self.speak(f'sir our system have {percentage} percent battery')

                if percentage >= 75:
                    self.speak('we have enough power to continue the work')
                elif 40 <= percentage < 75:
                    self.speak('we should connect our system to charging point to charge our battery')
                elif 15 <= percentage < 40:
                    self.speak("we don't have enough power to continue work, please connect to charging")
                else:
                    self.speak(
                        'we have very low power to continue work , please connect to charging otherwise system will '
                        'shutdown very soon')

            elif 'shut down the system' in self.query:
                self.speak('Shutting down the system, sir')
                os.system("shutdown /s /t 5")

            elif 'restart the system' in self.query:
                self.speak('Restarting the system, sir')
                os.system("restart /s /t 5")

            elif 'sleep the system' in self.query:
                self.speak('Sleeping the system sir')
                os.system("rundll33.exe powrprof.dll,SetSuspendState 0,1,0")

            elif 'no thanks' in self.query:
                self.speak('Thanks for using me sir, have a good dary')
                sys.exit()

            elif 'you can sleep' in self.query:
                self.speak('Thanks for using me sir, have a good day')
                sys.exit()

            elif 'how to' in self.query:
                try:
                    max_results = 1
                    how_to = search_wikihow(self.query, max_results)
                    assert len(how_to) == 1
                    how_to[0].print()
                    self.speak(how_to[0].summary)
                except Exception as e:
                    self.speak('sorry sir , i am not able to find this')
                    print(e)

            elif 'are you mad' in self.query:
                self.speak("sorry , i don't know sir , you made me sir")

            elif 'what you can do' in self.query:
                self.speak('I can play music , play news and many things ,sir')

            elif 'tell me about' in self.query or 'what is' in self.query:
                if 'tell me about' in self.query:
                    cm = self.query.replace('tell me about', '')
                elif 'what is' in self.query:
                    cm = self.query.replace('what is', '')
                else:
                    cm = self.query
                # self.speak(kit.info(cm, lines=2,True))
                sp = kit.info(cm,2,True)
                self.speak(sp)
                # sp = str(sp)
                # for_speaking = str(sp)
                # print(type(sp))
                # print(for_speaking)
                # self.speak(for_speaking)

                # self.speak(sp)

            elif 'take a screenshot' in self.query or 'screenshot' in self.query:
                self.speak('sir please tell me the name of this screenshot file')
                name = self.takecommand().lower()
                self.speak('please sir hold the screen for few seconds, i am taking screenshot')
                time.sleep(1.5)
                img = pyautogui.screenshot()
                img.save(f'{name}.png')
                self.speak(f' i am done sir , the screenshot {name}.png is saved in main folder.')

            elif 'read pdf' in self.query or 'read my pdf' in self.query:
                self.pdf_reader()

            elif 'tweet a message' in self.query:
                self.speak('what should i tweet on twitter sir')
                cm = self.takecommand().lower()
                try:
                    Twitter_Bot.tweet_msg(cm)
                    self.speak('The tweet has been twitted sir')
                except Exception as e:
                    self.speak('Due to network issue i am unable to tweet sir')
                    print(e)

            elif 'instagram profile' in self.query or 'profile on instagram' in self.query:
                self.speak('sir please enter the user name correctly.')
                name = input('Enter username here : ')
                webbrowser.open(f'www.instagram.com/{name}')
                self.speak(f'here is the profile of the user {name}')
                time.sleep(5)
                self.speak('sir would you like to download the profile picture of this account.')
                cond = self.takecommand().lower()
                if 'yes' in cond:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    self.speak('i am done sir, profile picture is saved in our main folder.')
                else:
                    self.speak('ok sir')

            elif 'can you calculate' in self.query:
                self.MathematicalCalculation()

            elif 'calculate' in self.query:
                self.MathsCalculation(self.query)

            elif 'where i am' in self.query or 'where we are' in self.query or 'location' in self.query:
                self.speak('wait sir, let me check')
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    # state = geo_data['state']
                    country = geo_data['country']
                    self.speak(f'sir , i am not sure , but i think we are in {city} city of {country} country')
                except Exception as e:
                    self.speak('Sorry sir , Due to network issue i am not able to find where we are.')
                    print(e)

            self.speak('sir, do you have any other work ?')


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("../../Downloads/jrvis3.gif")
        # self.ui.movie = QtGui.QMovie("C:\\Users\\parte\\Downloads\\arsenal\\vs.gui")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("../../Downloads/jrvis.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
arsenal = Main()
arsenal.show()
exit(app.exec_())
# if __name__ == "__main__":
#     MainFunction()
