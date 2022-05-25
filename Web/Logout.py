from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from Utilities import *

def Logout(Driver):

    Driver.get('http://mysirius.me/home')  # Goes to sign in page
    time.sleep(1)

    Avatar = ClickFnHttp(Driver, '/html/body/div[1]/div/div/div[1]/div[1]/div/footer/button')
    AddAccount = ClickFnHttp(Driver, "/html/body/div[2]/div[3]/div/p[1]")
    time.sleep(1)

    Driver.get('http://mysirius.me/home')  # Goes to sign in page
    time.sleep(1)

    Avatar = ClickFnHttp(Driver, '/html/body/div[1]/div/div/div[1]/div[1]/div/footer/button')
    Logout = ClickFnHttp(Driver, "/html/body/div[2]/div[3]/div/a/p")
    Cancel = ClickFnHttp(Driver, "/html/body/div[1]/div/div/div/button[2]")
    time.sleep(1)

    Driver.get('http://mysirius.me/home')  # Goes to sign in page
    time.sleep(1)

    Avatar = ClickFnHttp(Driver, '/html/body/div[1]/div/div/div[1]/div[1]/div/footer/button')
    Logout = ClickFnHttp(Driver, "/html/body/div[2]/div[3]/div/a/p")
    Confirm = ClickFnHttp(Driver, "/html/body/div[1]/div/div/div/button[1]")
