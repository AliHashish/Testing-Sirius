from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from EnterEmail import EnterEmail

def EnterUserName(Driver, Mode = 1):
    # if Mode = 0, then we will focus on testing various test cases
    # for entering username only.
    # if Mode = 1, then we will test the whole process with a specific element
    # namely, the first element

    # The default is testing the whole process

    if Mode == 0: # Mainly focuses on testing usernames
        F = open('../TestCases/UserNameTestCases.txt', 'r')
        UserNames = [UserName.rstrip('\n') for UserName in F.readlines()] # Makes a list containing all username test cases
        F.close()
        #print("Mode 0: \n")
        #print(UserNames)
        for UserName in UserNames:
            print("Username: ", UserName)
            # Locates the UserName field, and the next button
            LoginField = Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            NextButton = Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')
            time.sleep(3)

            LoginField.send_keys(UserName)  # Writes the UserName in the loginField
            time.sleep(2)

            NextButton.click()  # Clicks the next button
            time.sleep(3)

            Driver.get('https://twitter.com/i/flow/login')  # Returns to the login page
            time.sleep(3)
            EnterEmail(Driver)  # Entes the email, using the default testing mode

    else: # Mainly focuses on testing the whole process
        F = open('../TestCases/UserNameTestCases.txt', 'r')
        UserName = (F.readline()).rstrip('\n')   # UserName now equals the first element in the file
        F.close()
        #print("Mode 1: \n")
        #print(UserName)

        # Locates the UserName field, and the next button
        LoginField = Driver.find_element(by=By.XPATH, value=
            '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        NextButton = Driver.find_element(by=By.XPATH, value=
            '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')
        time.sleep(3)

        LoginField.send_keys(UserName)  # Writes the UserName in the loginField
        time.sleep(2)

        NextButton.click()  # Clicks the next button
        time.sleep(3)