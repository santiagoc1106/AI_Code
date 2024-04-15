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
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from fastai.vision.all import * 
#animals

#from credemo import username,pwd
import pyaudio
import sounddevice
span = None
user = None
username = 'ay_itsyaboiii_1@icloud.com'
pwd = 'James@2017santi'
options = webdriver.ChromeOptions()
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
                #os.system("start ans.mp3")
                time.sleep(int(7*duration))
                os.remove("ans.mp3")
            if span == True:
                speak = gTTS(text = text, lang = "es", slow = False)
                speak.save("ans.mp3")
                statbuf = os.stat("ans.mp3")
                mbytes = statbuf.st_size / 1024
                duration = mbytes / 200
                #os.system("start ans.mp3")
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

        if fri.text == "hola Friday":
            ans = "Estoy aqui para ayudarte!"
            span = True
        
        elif any(i in fri.text for i in ["Bye", "Goodbye", "See you", "See ya"]):
            ans = np.random.choice(["Goodbye!","See you later!", "I'll see ya!", "See you later, boss."])
            f = False

        elif any(i in fri.text for i in ["search", "look"]):
            words = fri.text.split("up")
            if len(words)==2:
                search_term = words[1].strip() 
            def get_results(search_term):
                url = "https://www.google.com"
                chrome_options = Options()
                chrome_options.add_experimental_option("detach", True)  
                browser = Chrome(options = chrome_options)
                browser.get(url)
                search_box = browser.find_element(By.CLASS_NAME, "gLFyf")
                search_box.send_keys(search_term)
                search_box.submit()
                try:
                    links = browser.find_elements(By.XPATH, "//ol[@class='web_regular_results']//h3//a")
                except:
                    links = browser.find_elements(By.XPATH, "//h3//a")
                results = []
                for link in links:
                    href = link.get_attribute("href")
                    print(href)
                    results.append(href)
                return results
            get_results(search_term)
            res = "This is what I found!"

        elif any(i in fri.text for i in ["play"]):

            chrome_opt = Options()
            chrome_opt.add_experimental_option("detach", True)
            browser = webdriver.Chrome(options = chrome_opt)

            song = fri.text.split("play")
            if len(song) == 2:
                search = song[1].strip

            def hover_and_click(song_name):
                time.sleep(5)
                a = ActionChains(browser)
                hover = browser.find_element(By.XPATH, '//button[@aria-label="'+song_name+'"]')
                a.move_to_element(hover).click().perform()
                time.sleep(20)



            def spotify(search):
                aw = browser.window_handles[0]
                wa = browser.window_handles[1]
                browser.switch_to.window(wa)
                browser.maximize_window()
                wait = WebDriverWait(browser, 5)
                wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "YeKN11KAw61rZoyjcgZ DzWw3g4E_66wu9ktqn36"))).click()
                #wait = WebDriverWait(browser, 10)
                # elem = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Desktop_LeftSidebar_Id"]/nav/div[1]/ul/li[2]/a')))
                # elem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Search"]')))
                #browser.find_element(By.CLASS_NAME, "YeKN11KAw61rZoyjcgZ DzWw3g4E_66wu9ktqn36").click()
                # inner_html = bar.get_attribute('innerHTML')
                # song_soup = BeautifulSoup(inner_html, 'html.parser')
                # all_tags = [tag for tag in song_soup.find_all()]
                # for tag in all_tags:
                #      tag_name = tag.name
                #      if tag_name == 'a':
                #          aria_name = tag['aria-label']
                #          if aria_name[0] == "Search":
                #              data_name = tag['data-context-menu-open']
                #              hover_and_click(data_name)
                # elem.click()
                time.sleep(3)
                #browser.find_element(By.XPATH, '//a[@href="/search"]').click()
                time.sleep(3)
                browser.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[3]/header/div[3]/div/div/form/input').send_keys(search)
                # time.sleep(3)
                # browser.find_element(By.XPATH, '//a[@href="/search/'+search+'/tracks"]').click()

            def login():
                url = "https://accounts.spotify.com/en/login"
                chrome_opt = Options()
                chrome_opt.add_experimental_option("detach", True)
                browser = webdriver.Chrome(options = chrome_opt)
                browser.get(url)
                browser.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/ul/li[3]/button').click()
                browser.find_element(By.XPATH, '/html/body/div[1]/oauth-init/div[1]/div/oauth-signin/div/apple-auth/div/div[1]/div/sign-in/div/div[1]/div[1]/div/div/div[1]/div/div/input').send_keys(username)
                browser.find_element(By.XPATH, '/html/body/div[1]/oauth-init/div[1]/div/oauth-signin/div/apple-auth/div/div[1]/div/sign-in/div/div[1]/button[1]').click()
                time.sleep(3)
                browser.find_element(By.XPATH, '/html/body/div[1]/oauth-init/div[1]/div/oauth-signin/div/apple-auth/div/div[1]/div/sign-in/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]/button').click()
                browser.find_element(By.XPATH, '/html/body/div[1]/oauth-init/div[1]/div/oauth-signin/div/apple-auth/div/div[1]/div/sign-in/div/div[1]/div[1]/div/div/div[2]/div/div/input').send_keys(pwd)
                browser.find_element(By.XPATH, '/html/body/div[1]/oauth-init/div[1]/div/oauth-signin/div/apple-auth/div/div[1]/div/sign-in/div/div[1]/button[1]').click()
                time.sleep(15)
                wait = WebDriverWait(browser, 10)
                elem = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/div/button[2]')))
                elem.click()
                time.sleep(20)
                spotify(search)
            login()
            print(song)


        elif any(i in fri.text for i in["show me a picture of dogs and cats"]):
            path = untar_data(URLs.PETS)
            files = get_image_files(path/"images")
            def label_func(f): 
                return f[0].isupper()
            
        



        fri.txt(ans)