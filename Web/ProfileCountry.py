from selenium.webdriver.common.by import By
from Utilities import *
from pyautogui import *
import pyautogui

def ProfileCountry(Driver, Mode = 1):
    if Mode==0:
        F = open('../TestCases/Country.txt', 'r')
        Countries = [Country.rstrip('\n') for Country in F.readlines()]
        F.close()
        time.sleep(2)

        for Country in Countries:
            i = 3
            EditProfile = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button', 2)
            while(i>=0):
                pyautogui.press("down")
                i-=1
            time.sleep(1)
            CountryField = Driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div[3]/div[3]/input').clear()
            CountryField = SendKeysFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[3]/input', Country, 2)

            Save = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[1]/button', 2)

            Driver.get('http://mysirius.me/user7')
            time.sleep(2)
    else:
        F = open('../TestCases/Country.txt', 'r')
        Country = (F.readline()).rstrip('\n')
        F.close()
        time.sleep(2)
        i = 3
        EditProfile = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button', 2)
        while (i >= 0):
            pyautogui.press("down")
            i -= 1
        time.sleep(1)
        CountryField = Driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div[3]/div[3]/input').clear()
        CountryField = SendKeysFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[3]/input', Country, 2)

        Save = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[1]/button', 2)

        Driver.get('http://mysirius.me/user7')
        time.sleep(2)