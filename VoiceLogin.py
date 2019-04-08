import sys
!{sys.executable} -m pip install speech_recognition
!{sys.executable} -m pip install gtts
!{sys.executable} -m pip install urllib3
!{sys.executable} -m pip install webdriver
!{sys.executable} -m pip install time
!{sys.executable} -m pip install pygame
!{sys.executable} -m pip install selenium

#importing packages
import speech_recognition as sr
from gtts import gTTS
import urllib3
from selenium import webdriver
from time import sleep
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from pygame import mixer

mixer.init()

while 1:
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source, duration=1)
        print("Which account do you want to log into")
        audio = r.listen(source, phrase_time_limit=4)

    try:

        response = r.recognize_google(audio)
        print("Did you say'" + response + "'")
        tts = gTTS(text="Logging into " + str(response), lang='en')
        tts.save("response.mp3")
        mixer.music.load('response.mp3')
        mixer.music.play()
        if response in ['Facebook', 'LinkedIn', 'Outlook']:
            driver = webdriver.Chrome()
            if (response == 'Facebook'):
                usr = 'enter your email'
                pwd = 'enter your password here'
                driver.get('https://www.facebook.com/')
                print ("Opened facebook")
                sleep(1)

                username_box = driver.find_element_by_id('email')
                username_box.send_keys(usr)
                print ("Email Id entered")
                sleep(1)

                password_box = driver.find_element_by_id('pass')
                password_box.send_keys(pwd)
                print ("Password entered")

                login_box = driver.find_element_by_id('loginbutton')
                login_box.click()

                print ("Done")
                input('Press anything to quit')
                driver.quit()
                print("Finished")

            elif (response == 'LinkedIn'):
                usr = 'enter your email'
                pwd = 'enter you password here'
                driver.get('https://www.linkedin.com/')
                print ("Opened LinkedIn")
                sleep(1)

                username_box = driver.find_element_by_id('login-email')
                username_box.send_keys(usr)
                print ("Email Id entered")
                sleep(1)

                password_box = driver.find_element_by_id("login-password")
                password_box.send_keys(pwd)
                print ("Password entered")

                login_box = driver.find_element_by_id("login-submit")
                login_box.click()

                print ("Done")
                input('Press anything to quit')
                driver.quit()
                print("Finished")

            elif (response == 'Outlook'):
                usr = 'enter your email'
                pwd = 'enter you password here'
                driver.get('https://login.microsoftonline.com/common/oauth2/authorize?client_id=00000002-0000-0ff1-ce00-000000000000&redirect_uri=https%3a%2f%2foutlook.office.com%2fowa%2f&resource=00000002-0000-0ff1-ce00-000000000000&response_mode=form_post&response_type=code+id_token&scope=openid&msafed=0&client-request-id=3e2d941c-91cb-4302-98e0-92c86b128c9f&protectedtoken=true&domain_hint=utdallas.edu&nonce=636902704285294457.309d0ad2-98a7-4187-9a4b-3389158cf995&state=DctLDsIwDADRBO7CAimtm09tLyruwA1MYwRSKqSQiOuTxZvdWGPMeTgNFkYMrmFl8AjRU_IcY8IpAGeQ7B2ToIsLoWOJDxcC8ZJofzInO97r_PnJfKsq5dh6y1KKfCfN_SK9ve6a31X3trXa9Q8')
                print ("Opened Outlook")
                sleep(1)

                username_box = driver.find_element_by_id('i0116')
                username_box.send_keys(usr)
                print ("Email Id entered")
                sleep(1)

                next_box = driver.find_element_by_id("idSIButton9")
                next_box.click()
                sleep(1)

                password_box = driver.find_element_by_id("i0118")
                password_box.send_keys(pwd)
                print ("Password entered")

                final_box = driver.find_element_by_id("idSIButton9")
                final_box.click()
                sleep(1)

                final_final_box = driver.find_element_by_id("idSIButton9")
                final_final_box.click()
                sleep(1)

                print ("Done")
                input('Press anything to quit')
                driver.quit()
                print("Finished")

            else:
                print("Don't know what you want from me!")
        else:
            print('Please try again')
        break
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
