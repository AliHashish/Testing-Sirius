from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from Utilities import *
from pyautogui import *
import pyautogui

def ProfileNames(Driver, Mode = 1):
    if Mode==0:
        F = open('../TestCases/Names.txt', 'r')
        names = [Name.rstrip('\n') for Name in F.readlines()]
        F.close()
        time.sleep(2)

        for name in names:
            i = 2
            EditProfile = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button', 2)
            while(i>=0):
                pyautogui.press("down")
                i-=1

            # NameField = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[1]/input', 1)
            NameField = Driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div[3]/div[1]/input').clear()
            NameField = SendKeysFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[1]/input', name, 2)

            Save = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[1]/button', 2)

            Driver.get('http://mysirius.me/user7')
            time.sleep(1)
    else:
        F = open('../TestCases/Names.txt', 'r')
        Name = (F.readline()).rstrip('\n')
        F.close()
        time.sleep(2)

        EditProfile = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button', 2)

        NameField = SendKeysFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[1]/p', Name, 2)

        Save = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[1]/button', 2)

        Driver.get('http://mysirius.me/user7')
        time.sleep(2)
