from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

def EnterEmail(Driver, Mode = 1):
    # if Mode = 0, then we will focus on testing various test cases
    # for entering email only.
    # if Mode = 1, then we will test the whole process with a specific element
    # namely, the first element

    # The default is testing the whole process

    if Mode == 0: # Mainly focuses on testing emails
        F = open('../TestCases/EmailTestCases.txt', 'r')
        Emails = [Email.rstrip('\n') for Email in F.readlines()] # Makes a list containing all email test cases
        F.close()
        #print("Mode 0: \n")
        #print(Emails)
        for Email in Emails:
            print("Email: ", Email)
            # Locates the email field, and the next button
            LoginField = Driver.find_element(by=By.XPATH, value=
            '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
            NextButton = Driver.find_element(by=By.XPATH, value=
            '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]')
            time.sleep(3)

            LoginField.send_keys(Email)  # Writes the email in the loginField
            time.sleep(2)

            NextButton.click()  # Clicks the next button
            time.sleep(3)

            Driver.get('https://twitter.com/i/flow/login')  # Returns to the login page
            time.sleep(3)

    else: # Mainly focuses on testing the whole process
        F = open('../TestCases/EmailTestCases.txt', 'r')
        Email = (F.readline()).rstrip('\n')   # Email now equals the first element in the file
        F.close()
        #print("Mode 1: \n")
        #print(Email)

        # Locates the email field, and the next button
        LoginField = Driver.find_element(by=By.XPATH, value=
        '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        NextButton = Driver.find_element(by=By.XPATH, value=
        '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]')
        time.sleep(3)

        LoginField.send_keys(Email)  # Writes the email in the loginField
        time.sleep(2)

        NextButton.click()  # Clicks the next button
        time.sleep(3)