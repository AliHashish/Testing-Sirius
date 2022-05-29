from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Utilities import *


# Enters Email and password, then presses next
def SignUp(Driver, Mode = 1):
    # if Mode = 0, then we will focus on testing various test cases
    # for registering only.
    # if Mode = 1, then we will test the whole process with a specific element
    # namely, the first element

    Driver.get('http://mysirius.me/signup')  # Goes to sign up page
    time.sleep(1)

    # The default is testing the whole process

    if Mode == 0: # Mainly focuses on testing email and password combinations

        F = open('../TestCases/NameTestCases.txt', 'r')
        Names = [Name.rstrip('\n') for Name in F.readlines()]  # Makes a list containing all name test cases
        F.close()

        F = open('../TestCases/UserNameTestCases.txt', 'r')
        UserNames = [UserName.rstrip('\n') for UserName in F.readlines()]  # Makes a list containing all username test cases
        F.close()

        F = open('../TestCases/EmailTestCases.txt', 'r')
        Emails = [Email.rstrip('\n') for Email in F.readlines()] # Makes a list containing all email test cases
        F.close()

        F = open('../TestCases/PasswordTestCases.txt', 'r')
        Passwords = [Password.rstrip('\n') for Password in F.readlines()]  # Makes a list containing all Password test cases
        F.close()

        F = open('../TestCases/City.txt', 'r')
        Cities = [city.rstrip('\n') for city in F.readlines()]  # Makes a list containing all cities test cases
        F.close()

        F = open('../TestCases/Country.txt', 'r')
        Countries = [Country.rstrip('\n') for Country in F.readlines()]  # Makes a list containing all countries test cases
        F.close()

        counter = 0  # counts number of cases
        #print("Mode 0: \n")
        #print(Emails)
        for Name in Names:
            for UserName in UserNames:
                for Email in Emails:
                    for Password in Passwords:
                        for City in Cities:
                            for Country in Countries:
                                # Locates the input fields and the Next button
                                for i in range(2):  # Shows password in one of them, hides it in the other
                                    counter += 1
                                    print("Test number: ", counter)
                                    print("Name: ", Name)
                                    print("Username: ", UserName)
                                    print("Email: ", Email)
                                    print("Password: ", Password)
                                    print("City: ", City)
                                    print("Country: ", Country)

                                    if (i%2 == 0):
                                        time.sleep(2)
                                        ShowPassword = ClickFnHttp(Driver, '/html/body/div/div/div/form/span/i', 1)

                                    time.sleep(1)
                                    NameField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[1]', Name+str(i), 1)  # Writes the name in the name field
                                    # time.sleep(1)
                                    UserNameField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[2]', UserName+str(i), 1)  # Writes the username in the username field

                                    time.sleep(1)
                                    EmailField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[4]', Email+str(i), 1)  # Writes the email in the email field
                                    # time.sleep(1)
                                    PasswordField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[3]', Password, 1)  # Writes the password in the password field

                                    time.sleep(1)
                                    CityField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[6]', City, 1)  # Writes the city in the city field
                                    # time.sleep(1)
                                    CountryField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[5]', Country, 1)  # Writes the country in the country field
                                    time.sleep(1)


                                    try:
                                        date_input = Driver.find_element(by=By.XPATH, value='/html/body/div/div/div/form/input[7]')
                                        date_input.click()  # Focus input field
                                        date_input.send_keys(Keys.CONTROL, "a")  # Select all pre-existing text/input value by pressing CTRL + A
                                        date_input.send_keys(Keys.BACKSPACE)  # Remove that text
                                        day = str((counter % 28) + 1)
                                        month = str((counter % 12) + 1)
                                        year = str((counter % 51) + 1980)    # 1980 - 2030
                                        print("day: ", day, "\nmonth: ", month, "\nyear: ", year, "\n")
                                        if len(day) == 1:
                                            day = '0' + day      # adds 0 at the beginning in case it is only 1 digit
                                        if len(month) == 1:
                                            month = '0' + month  # adds 0 at the beginning in case it is only 1 digit
                                        date_input.send_keys(day+month+year)  # Add desired text/set input value
                                    except:
                                        print("Element not found.")


                                    time.sleep(2)
                                    NextButton = ClickFnHttp(Driver, '/html/body/div/div/div/form/button', 1)

                                    time.sleep(2)
                                    Driver.get('http://mysirius.me/signup')  # Returns to the sign up page
                                    time.sleep(1)

    else: # Mainly focuses on testing the whole process


        F = open('../TestCases/NameTestCases.txt', 'r')
        Name = (F.readline()).rstrip('\n')   # Name now equals the first element in the file
        F.close()

        F = open('../TestCases/UserNameTestCases.txt', 'r')
        UserName = (F.readline()).rstrip('\n')   # Username now equals the first element in the file
        F.close()

        F = open('../TestCases/EmailTestCases.txt', 'r')
        Email = (F.readline()).rstrip('\n')   # Email now equals the first element in the file
        F.close()

        F = open('../TestCases/PasswordTestCases.txt', 'r')
        Password = (F.readline()).rstrip('\n')   # Password now equals the first element in the file
        F.close()

        F = open('../TestCases/City.txt', 'r')
        City = (F.readline()).rstrip('\n')   # City now equals the first element in the file
        F.close()

        F = open('../TestCases/Country.txt', 'r')
        Country = (F.readline()).rstrip('\n')   # Country now equals the first element in the file
        F.close()

        try:
            ExtraChar = '001'
            time.sleep(1)
            NameField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[1]', Name + ExtraChar,
                                       1)  # Writes the name in the name field
            # time.sleep(1)
            UserNameField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[2]', UserName + ExtraChar,
                                           1)  # Writes the username in the username field

            time.sleep(1)
            EmailField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[4]', Email + ExtraChar,
                                        1)  # Writes the email in the email field
            # time.sleep(1)
            PasswordField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[3]', Password,
                                           1)  # Writes the password in the password field

            time.sleep(1)
            CityField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[6]', City,
                                       1)  # Writes the city in the city field
            # time.sleep(1)
            CountryField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[5]', Country,
                                          1)  # Writes the country in the country field
            time.sleep(1)

            date_input = Driver.find_element(by=By.XPATH, value='/html/body/div/div/div/form/input[7]')
            date_input.click()  # Focus input field
            date_input.send_keys(Keys.CONTROL, "a")  # Select all pre-existing text/input value by pressing CTRL + A
            date_input.send_keys(Keys.BACKSPACE)  # Remove that text
            date_input.send_keys("02032000")  # Add desired text/set input value
            time.sleep(1)
        except:
            print("Element not found.")


        time.sleep(1)
        SignupButton = ClickFnHttp(Driver, '/html/body/div/div/div/form/button[3]', 1)
        time.sleep(1)


        NextButton = ClickFnHttp(Driver, "/html/body/div[1]/div/div/div/button", 1)
        time.sleep(1)