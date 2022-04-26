from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


def TweetComp(Driver):
    Driver.get('http://34.236.108.123/home')
    time.sleep(3)

    # Media = Driver.find_element(by=By.XPATH, value=
    #             '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[1]/div[1]/div')
    # time.sleep(3)
    # Media.click()
    # time.sleep(3)
    # Driver.get('http://34.236.108.123/home')
    # time.sleep(3)

    # Gif = Driver.find_element(by=By.XPATH, value=
    #             '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[1]/div[2]/div')
    # time.sleep(3)
    # Gif.click()
    # time.sleep(3)
    # Driver.get('http://34.236.108.123/home')
    # time.sleep(3)

    Poll = Driver.find_element(by=By.XPATH, value=
    '/html/body/div/div/div/div[2]/div[1]/div[2]/div[2]/input')
    time.sleep(1)
    Poll.click()
    time.sleep(1)
    Driver.get('http://34.236.108.123/home')
    time.sleep(1)

    Schedule = Driver.find_element(by=By.XPATH, value=
    '/html/body/div/div/div/div[2]/div[1]/div[2]/div[4]/input')
    time.sleep(3)
    Schedule.click()
    time.sleep(3)
    Driver.get('http://34.236.108.123/home')
    time.sleep(3)

    Emoji = Driver.find_element(by=By.XPATH, value=
    '/html/body/div/div/div/div[2]/div[1]/div[2]/div[5]/input')
    time.sleep(1)
    Emoji.click()
    time.sleep(1)
    Driver.get('http://34.236.108.123/home')
    time.sleep(1)

    Poll = Driver.find_element(by=By.XPATH, value=
    '/html/body/div/div/div/div[2]/div[1]/div[2]/div[2]/input')
    time.sleep(1)
    Poll.click()
    time.sleep(1)

    CancelPoll = Driver.find_element(by=By.XPATH, value=
    '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[2]/button')
    time.sleep(3)
    CancelPoll.click()
    time.sleep(1)

    Schedule = Driver.find_element(by=By.XPATH, value=
    '/html/body/div/div/div/div[2]/div[1]/div[2]/div[4]/input')
    time.sleep(1)
    Schedule.click()
    time.sleep(1)

    ConfirmSchedule = Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/button')
    time.sleep(3)
    ConfirmSchedule.click()
    time.sleep(1)

    # Note that: after pressing Confirm, the components disappear {BUG}
    # So we need to refresh the page.

    Driver.get('http://34.236.108.123/home')
    time.sleep(1)






