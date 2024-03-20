from gtts import gTTS
import speech_recognition as sr
import librosa
import python_weather
import time
import platform
import os
import pickle
import numpy as np
import re
import selenium.webdriver as webdriver
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pyaudio

span = None
user = None

class AI():

    def __init__(self, name):
        print(f"Hello, I'm {name}!")
        self.name = name
    ##Defines speech to text function, sets what happens when user loads up, speaks in spanish, or english
    def speech (self):
        rec = sr.Recognizer()
        with sr.Microphone() as mic:
            if span == None:
                print("Listening/Escuchando...")
            if span == True:
                print("Escuchando")
            if span == False:
                print("Listening")
            audio = rec.listen(mic)
            self.text = "ERROR PROCESSING"
        try:
            self.text = rec.recognize_google(audio)
            print("You -->", self.text)

        except:
            print("ERROR PROCESSING")
    @staticmethod
    def txt(text):
        ##Reads computer's OS
        if getattr(platform.uname(), "system") == "Windows":
            print("FRIDAY -->", text)
            if span == False:
                speak = gTTS(text = text, lang = "en", slow = False)
                speak.save("ans.mp3")
                statbuf = os.stat("ans.mp3")
                mbytes = statbuf.st_size / 1024
                duration = mbytes / 200
                os.system("start ans.mp3")
                time.sleep(int(7*duration))
                os.remove("ans.mp3")
            if span == True:
                speak = gTTS(text = text, lang = "es", slow = False)
                speak.save("ans.mp3")
                statbuf = os.stat("ans.mp3")
                mbytes = statbuf.st_size / 1024
                duration = mbytes / 200
                os.system("start ans.mp3")
                time.sleep(int(7*duration))
                os.remove("ans.mp3")

        if getattr(platform.uname(), "system") == "macOS":
            print("FRIDAY -->", text)
            if span == False:
                speak = gTTS(text = text, lang = "en", slow = False)
                speak.save("ans.mp3")
                statbuf = os.stat("ans.mp3")
                mbytes = statbuf.st_size / 1024
                duration = mbytes / 200
                os.system("afplay ans.mp3")
                time.sleep(int(7*duration))
                os.remove("ans.mp3")
            if span == True:
                speak = gTTS(text = text, lang = "es", slow = False)
                speak.save("ans.mp3")
                statbuf = os.stat("ans.mp3")
                mbytes = statbuf.st_size / 1024
                duration = mbytes / 200
                os.system("afplay ans.mp3")
                time.sleep(int(7*duration))
                os.remove("ans.mp3")

##Wake Friday up
    def wake(self, text):
        return True if self.name in text.lower() else False
##Run

if __name__ =="__main__":
    fri = AI(name = "friday")
    f = True

    while f:
        fri.speech()
        if fri.wake(fri.text) is True:
            ans = "I'm here to help you in whatever you need!"
            span = False

        if fri.text == "hola friday":
            ans = "Estoy aqui para ayudarte!"
            spanish = True
            
        fri.txt(ans)