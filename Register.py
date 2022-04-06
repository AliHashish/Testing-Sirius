from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def Register(Driver, Mode = 1):
    Driver.get('https://twitter.com/i/flow/signup')  # Returns to the signup page
    time.sleep(3)
    Signup = Driver.find_element(by=By.XPATH, value=
        '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]')
    time.sleep(3)
    Signup.click()
    time.sleep(3)
    # if Mode = 0, then we will focus on testing various test cases
    # for entering Name only.
    # if Mode = 1, then we will test the whole process with a specific element
    # namely, the first element

    # The default is testing the whole process

    if Mode == 0: # Mainly focuses on testing Names
        F = open('UserNameTestCases.txt', 'r')
        Names = [Name.rstrip('\n') for Name in F.readlines()] # Makes a list containing all Name test cases
        F.close()

        F = open('PhoneTestCases.txt', 'r')
        Phones = [Phone.rstrip('\n') for Phone in F.readlines()]  # Makes a list containing all Phone test cases
        F.close()

        #print("Mode 0: \n")
        #print(Names)
        for Name in Names:
            for Phone in Phones:
                print("Name: ", Name)
                print("Phone: ", Phone, '\n')
                # Locates the Name field, and the next button
                NameField = Driver.find_element(by=By.XPATH, value=
                    '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/label/div/div[2]/div/input')
                PhoneField = Driver.find_element(by=By.XPATH, value=
                    '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/label/div/div[2]/div/input')

                time.sleep(3)

                NameField.send_keys(Name)  # Writes the Name in the loginField
                time.sleep(2)

                PhoneField.send_keys(Phone)  # Writes the Phone in the loginField
                time.sleep(2)

                MonthField = Select(Driver.find_element(by=By.XPATH, value=
                    '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[4]/div[3]/div/div[1]/select'))
                time.sleep(3)
                MonthField.select_by_visible_text('January')
                time.sleep(3)

                DayField = Select(Driver.find_element(by=By.XPATH, value=
                    '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[4]/div[3]/div/div[2]/select'))
                time.sleep(3)
                DayField.select_by_visible_text('14')
                time.sleep(3)

                YearField = Select(Driver.find_element(by=By.XPATH, value=
                    '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[4]/div[3]/div/div[3]/select'))
                time.sleep(3)
                YearField.select_by_visible_text('2001')
                time.sleep(3)

                NextButton = Driver.find_element(by=By.XPATH, value=
                    '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')

                NextButton.click()  # Clicks the next button
                time.sleep(3)

                Driver.get('https://twitter.com/i/flow/signup')  # Returns to the signup page
                time.sleep(3)

                Signup = Driver.find_element(by=By.XPATH, value=
                    '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]')
                time.sleep(3)
                Signup.click()
                time.sleep(3)

    else: # Mainly focuses on testing the whole process
        F = open('UserNameTestCases.txt', 'r')
        Name = (F.readline()).rstrip('\n')   # Name now equals the first element in the file
        F.close()

        F = open('PhoneTestCases.txt', 'r')
        Phone = (F.readline()).rstrip('\n')  # Phone now equals the first element in the file
        F.close()

        #print("Mode 1: \n")
        #print(Name)

        # Locates the Name field, and the next button
        NameField = Driver.find_element(by=By.XPATH, value=
            '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/label/div/div[2]/div/input')
        PhoneField = Driver.find_element(by=By.XPATH, value=
            '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/label/div/div[2]/div/input')
        time.sleep(3)

        NameField.send_keys(Name)  # Writes the Name in the loginField
        time.sleep(2)

        PhoneField.send_keys(Phone)  # Writes the Phone in the loginField
        time.sleep(2)
        MonthField = Select(Driver.find_element(by=By.XPATH, value=
            '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[4]/div[3]/div/div[1]/select'))
        time.sleep(3)
        MonthField.select_by_visible_text('January')
        time.sleep(3)

        DayField = Select(Driver.find_element(by=By.XPATH, value=
            '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[4]/div[3]/div/div[2]/select'))
        time.sleep(3)
        DayField.select_by_visible_text('14')
        time.sleep(3)

        YearField = Select(Driver.find_element(by=By.XPATH, value=
            '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[4]/div[3]/div/div[3]/select'))
        time.sleep(3)
        YearField.select_by_visible_text('2001')
        time.sleep(3)


        NextButton = Driver.find_element(by=By.XPATH, value=
            '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')

        NextButton.click()  # Clicks the next button
        time.sleep(3)