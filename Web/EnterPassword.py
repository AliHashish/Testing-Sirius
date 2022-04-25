from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from EnterEmail import EnterEmail
from EnterUserName import EnterUserName

def EnterPassword(Driver, Mode = 1):
    # if Mode = 0, then we will focus on testing various test cases
    # for entering Password only.
    # if Mode = 1, then we will test the whole process with a specific element
    # namely, the first element

    # The default is testing the whole process

    if Mode == 0: # Mainly focuses on testing Passwords
        F = open('../TestCases/PasswordTestCases.txt', 'r')
        Passwords = [Password.rstrip('\n') for Password in F.readlines()] # Makes a list containing all Password test cases
        F.close()
        #print("Mode 0: \n")
        #print(Passwords)
        for Password in Passwords:
            print("Password: ", Password)
            # Locates the Password field, and the next button
            time.sleep(3)
            PasswordField = Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            LoginButton = Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div')
            time.sleep(3)

            PasswordField.send_keys(Password)  # Writes the Password in the loginField
            time.sleep(2)

            LoginButton.click()  # Clicks the next button
            time.sleep(3)

            Driver.get('https://twitter.com/i/flow/login')  # Returns to the login page
            time.sleep(3)
            EnterEmail(Driver)      # Enters the email, using the default testing mode
            time.sleep(3)
            EnterUserName(Driver)   # Enters the username, using the default testing mode
            time.sleep(3)

    else: # Mainly focuses on testing the whole process
        F = open('../TestCases/PasswordTestCases.txt', 'r')
        Password = (F.readline()).rstrip('\n')   # Password now equals the first element in the file
        F.close()
        #print("Mode 1: \n")
        #print(Password)

        # Locates the Password field, and the next button
        PasswordField = Driver.find_element(by=By.XPATH, value=
            '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        LoginButton = Driver.find_element(by=By.XPATH, value=
            '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div')
        time.sleep(3)

        PasswordField.send_keys(Password)  # Writes the Password in the loginField
        time.sleep(2)

        LoginButton.click()  # Clicks the next button
        time.sleep(3)