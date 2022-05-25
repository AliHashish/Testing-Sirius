from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from Utilities import *


# Enters Email and password, then presses next
def SignIn(Driver, Mode = 1):
    # if Mode = 0, then we will focus on testing various test cases
    # for entering email and password only.
    # if Mode = 1, then we will test the whole process with a specific element
    # namely, the first element

    Driver.get('http://mysirius.me/signin')  # Goes to sign in page
    time.sleep(1)

    # The default is testing the whole process

    if Mode == 0: # Mainly focuses on testing email and password combinations
        F = open('../TestCases/EmailTestCases.txt', 'r')
        Emails = [Email.rstrip('\n') for Email in F.readlines()] # Makes a list containing all email test cases
        F.close()

        F = open('../TestCases/PasswordTestCases.txt', 'r')
        Passwords = [Password.rstrip('\n') for Password in F.readlines()]  # Makes a list containing all Password test cases
        F.close()

        counter = 0  # counts number of cases
        #print("Mode 0: \n")
        #print(Emails)
        for Email in Emails:
            for Password in Passwords:

                # Locates the email field, password field, and the login button
                for i in range(2):  # uses same email and password twice, but shows password in one of them
                    counter += 1
                    print("Test number: ", counter)
                    print("Email: ", Email)
                    print("Password: ", Password)
                    print("")

                    # EmailField = Driver.find_element(by=By.XPATH, value=
                    # '/html/body/div/div/div/div/form/input[1]')
                    #
                    # PasswordField = Driver.find_element(by=By.XPATH, value=
                    # '/html/body/div/div/div/div/form/input[2]')
                    #
                    # LoginButton = Driver.find_element(by=By.XPATH, value=
                    # '/html/body/div/div/div/div/form/button[3]')
                    #
                    # # time.sleep(1)
                    # ShowPassword = Driver.find_element(by=By.XPATH, value=
                    # '/html/body/div/div/div/div/form/span/i')

                    if (i%2 == 0):
                        time.sleep(1)
                        ShowPassword = ClickFnHttp(Driver, '/html/body/div/div/div/form/span/i', 1)

                    time.sleep(1)
                    EmailField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[1]', Email, 1)  # Writes the email in the email field
                    # time.sleep(1)
                    PasswordField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[2]', Password, 1)  # Writes the password in the password field
                    time.sleep(1)
                    LoginButton = ClickFnHttp(Driver, '/html/body/div/div/div/form/button[3]', 1)


                    time.sleep(2)
                    Driver.get('http://mysirius.me/signin')  # Returns to the login page
                    time.sleep(1)

    else: # Mainly focuses on testing the whole process
        F = open('../TestCases/EmailTestCases.txt', 'r')
        Email = (F.readline()).rstrip('\n')   # Email now equals the first element in the file
        F.close()

        F = open('../TestCases/PasswordTestCases.txt', 'r')
        Password = (F.readline()).rstrip('\n')  # Password now equals the first element in the file
        F.close()

        #print("Mode 1: \n")
        #print(Email)

        # Locates the email field, password field and the login button
        # EmailField = Driver.find_element(by=By.XPATH, value=
        # '/html/body/div/div/div/div/form/input[1]')
        #
        # PasswordField = Driver.find_element(by=By.XPATH, value=
        # '/html/body/div/div/div/div/form/input[2]')
        #
        # LoginButton = Driver.find_element(by=By.XPATH, value=
        # '/html/body/div/div/div/div/form/button[3]')

        time.sleep(1)
        EmailField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[1]', Email, 1)   # Writes the email in the email field
        time.sleep(1)
        PasswordField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[2]', Password, 1)  # Writes the password in the password field
        time.sleep(3)
        LoginButton = ClickFnHttp(Driver, '/html/body/div/div/div/form/button[2]', 1)
        time.sleep(2)
