from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


def TweetComp(Driver):
    time.sleep(3)


    Gif = Driver.find_element(by=By.XPATH, value=
                '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[1]/div[2]/div')
    time.sleep(3)
    Gif.click()
    time.sleep(3)
    Driver.get('https://twitter.com/home')
    time.sleep(3)

    Poll = Driver.find_element(by=By.XPATH, value=
                '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[1]/div[3]/div')
    time.sleep(3)
    Poll.click()
    time.sleep(3)
    Driver.get('https://twitter.com/home')
    time.sleep(3)

    Emoji = Driver.find_element(by=By.XPATH, value=
                '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[1]/div[4]/div')
    time.sleep(3)
    Emoji.click()
    time.sleep(3)
    Driver.get('https://twitter.com/home')
    time.sleep(3)

    Schedule = Driver.find_element(by=By.XPATH, value=
                '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[1]/div[5]/div')
    time.sleep(3)
    Schedule.click()
    time.sleep(3)
    Driver.get('https://twitter.com/home')
    time.sleep(3)

    Media = Driver.find_element(by=By.XPATH, value=
                '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[1]/div[1]/div')
    time.sleep(3)
    Media.click()
    time.sleep(3)
    Driver.get('https://twitter.com/home')
    time.sleep(3)



