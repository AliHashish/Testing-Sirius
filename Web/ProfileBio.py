from selenium.webdriver.common.by import By
from Utilities import *
from pyautogui import *
import pyautogui

def ProfileBio(Driver, Mode = 1):
    if Mode==0:
        F = open('../TestCases/Bios.txt', 'r')
        Bios = [Bio.rstrip('\n') for Bio in F.readlines()]
        F.close()
        time.sleep(2)

        for Bio in Bios:
            i = 3
            EditProfile = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button', 2)
            while(i>=0):
                pyautogui.press("down")
                i-=1
            time.sleep(1)
            # NameField = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[1]/input', 1)
            BioField = Driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div[3]/div[2]/input').clear()
            BioField = SendKeysFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[2]/input', Bio, 2)

            Save = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[1]/button', 2)

            Driver.get('http://mysirius.me/user7')
            time.sleep(1)
    else:
        F = open('../TestCases/Bios.txt', 'r')
        Bio = (F.readline()).rstrip('\n')
        F.close()
        time.sleep(2)
        i=3
        EditProfile = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button', 2)

        EditProfile = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button', 2)
        while (i >= 0):
            pyautogui.press("down")
            i -= 1
        time.sleep(2)
        # NameField = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[1]/input', 1)
        BioField = Driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div[3]/div[2]/input').clear()
        BioField = SendKeysFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[2]/input', Bio, 2)

        Save = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[1]/button', 2)

        Driver.get('http://mysirius.me/user7')
        time.sleep(2)