from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from Utilities import *

def ProfileNames(Driver, Mode = 1):

    if Mode==0:
        F = open('../TestCases/Names.txt', 'r')
        names = [Name.rstrip('\n') for Name in F.readlines()]
        F.close()
        time.sleep(2)

        for name in names:

            EditProfile = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button', 2)

            NameField = SendKeysFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[1]/p', name, 2)

            Save = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[1]/button', 2)

            Driver.get('http://mysirius.me/user3')
            time.sleep(1)
    else:
        F = open('../TestCases/Names.txt', 'r')
        Name = (F.readline()).rstrip('\n')
        F.close()
        time.sleep(2)

        EditProfile = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button', 2)

        NameField = SendKeysFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[1]/p', Name, 2)

        Save = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[1]/button', 2)

        Driver.get('http://mysirius.me/user3')
        time.sleep(2)
