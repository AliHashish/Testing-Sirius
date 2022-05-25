from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from Utilities import *

def ForgotPassword(Driver):

    Driver.get('http://mysirius.me/signin')  # Goes to sign in page
    time.sleep(1)

    ForgotPass = ClickFnHttp(Driver, '/html/body/div[1]/div/div/form/button[3]')
    F = open('../TestCases/EmailTestCases.txt', 'r')
    # Email = (F.readline()).rstrip('\n')  # Email now equals the first element in the file
    Email = 'ultimatehacker925@yahoo.com'  # Hard coded, so as not to mess up other people's accounts
    F.close()
    EnterEmail = SendKeysFnHttp(Driver, "/html/body/div[1]/div/div/div/input", Email)  # Writes the email in the email field
    Search = ClickFnHttp(Driver, "/html/body/div[1]/div/div/div/button")



    time.sleep(1)
    Driver.get('http://mysirius.me/signin')  # Goes to sign in page
    time.sleep(1)

    time.sleep(1)
    EmailField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[1]', Email, 1)  # Writes the email in the email field
    time.sleep(1)
    PasswordField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[2]', 'passwordsa3ba', 1)  # Writes the password in the password field
    time.sleep(1)
    LoginButton = ClickFnHttp(Driver, '/html/body/div/div/div/form/button[2]', 1)
    time.sleep(2)
