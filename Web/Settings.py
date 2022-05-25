from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from Utilities import *

def Settings(Driver):

    Driver.get('http://mysirius.me/settings/')  # Goes to settings page
    time.sleep(1)

    Notifications = ClickFnHttp(Driver, '/html/body/div[1]/div/div/div[2]/button[3]', 1)
    Mute = ClickFnHttp(Driver, '/html/body/div[1]/div/div/div[2]/input')

    Driver.get('http://mysirius.me/settings/')  # Goes to settings page
    time.sleep(1)

    Notifications = ClickFnHttp(Driver, '/html/body/div[1]/div/div/div[2]/button[3]', 1)
    Mute = ClickFnHttp(Driver, '/html/body/div[1]/div/div/div[2]/input')
    Mute = ClickFnHttp(Driver, '/html/body/div[1]/div/div/div[2]/input')
    time.sleep(1)






    Driver.get('http://mysirius.me/settings/')  # Goes to settings page
    time.sleep(1)

    ChangePassword = ClickFnHttp(Driver, '/html/body/div[1]/div/div/div[2]/button[2]', 1)

    F = open('../TestCases/PasswordTestCases.txt', 'r')
    # Password = (F.readline()).rstrip('\n')  # Password now equals the first element in the file
    Password = "passwordsa3ba"  # hardcoded so as not to mess other people's accounts
    F.close()

    EnterPassword = SendKeysFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/input[1]", Password,
                                   1)  # Writes the password in the password field

    NewPassword = SendKeysFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/input[2]", Password,
                                 1)  # Writes the password in the password field
    ConfirmNewPassword = SendKeysFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/input[3]", Password,
                                        1)  # Writes the password in the password field

    Save = ClickFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/button", 1)
    time.sleep(1)







    Driver.get('http://mysirius.me/settings/changepassword')  # Goes to settings page
    time.sleep(1)
    EnterPassword = SendKeysFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/input[1]", Password + "Wrong",
                                   1)  # Writes the password in the password field

    NewPassword = SendKeysFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/input[2]", Password,
                                 1)  # Writes the password in the password field
    ConfirmNewPassword = SendKeysFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/input[3]", Password,
                                        1)  # Writes the password in the password field

    Save = ClickFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/button", 1)
    time.sleep(1)







    Driver.get('http://mysirius.me/settings/changepassword')  # Goes to settings page
    time.sleep(1)
    ForgotPassword = ClickFnHttp(Driver, "/html/body/div/div/div/div[2]/a")
    time.sleep(1)

    Driver.get('http://mysirius.me/settings/changepassword')  # Goes to settings page
    time.sleep(1)
    EnterPassword = SendKeysFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/input[1]", Password, 1)  # Writes the password in the password field

    NewPassword = SendKeysFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/input[2]", Password+"New", 1)  # Writes the password in the password field
    ConfirmNewPassword = SendKeysFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/input[3]", Password+"New", 1)  # Writes the password in the password field

    Save = ClickFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/button", 1)







    F = open('../TestCases/EmailTestCases.txt', 'r')
    # Email = (F.readline()).rstrip('\n')  # Email now equals the first element in the file
    Email = 'ultimatehacker925@yahoo.com'       # Hard coded, so as not to mess up other people's accounts
    F.close()

    time.sleep(1)
    Driver.get('http://mysirius.me/signin')  # Goes to sign in page
    time.sleep(1)

    time.sleep(1)
    EmailField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[1]', Email,
                                1)  # Writes the email in the email field
    time.sleep(1)
    PasswordField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[2]', Password+"New",
                                   1)  # Writes the password in the password field
    time.sleep(1)
    LoginButton = ClickFnHttp(Driver, '/html/body/div/div/div/form/button[2]', 1)
    time.sleep(2)
    # //////////// el password f3ln et8ayaret, w 3mlt login at2kd
    # brg3ha tany b2a
    Driver.get('http://mysirius.me/settings/changepassword')  # Goes to settings page
    time.sleep(1)
    EnterPassword = SendKeysFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/input[1]", Password+"New",
                                   1)  # Writes the password in the password field

    NewPassword = SendKeysFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/input[2]", Password,
                                 1)  # Writes the password in the password field
    ConfirmNewPassword = SendKeysFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/input[3]", Password,
                                        1)  # Writes the password in the password field

    Save = ClickFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/button", 1)
    time.sleep(1)










    Driver.get('http://mysirius.me/settings/')  # Goes to settings page
    time.sleep(1)

    AccountInfo = ClickFnHttp(Driver, "/html/body/div/div/div/div[2]/button[1]")
    Protected = ClickFnHttp(Driver, "/html/body/div/div/div/div[2]/button[3]")
    TickBox = ClickFnHttp(Driver, "/html/body/div/div/div/div[2]/input")
    time.sleep(1)


    Driver.get('http://mysirius.me/settings/')  # Goes to settings page
    time.sleep(1)

    AccountInfo = ClickFnHttp(Driver, "/html/body/div/div/div/div[2]/button[1]")
    Protected = ClickFnHttp(Driver, "/html/body/div/div/div/div[2]/button[3]")
    TickBox = ClickFnHttp(Driver, "/html/body/div/div/div/div[2]/input")
    TickBox = ClickFnHttp(Driver, "/html/body/div/div/div/div[2]/input")
    time.sleep(1)
    # ///////////////////////////////////// kda 5lst el protected tweets












    Driver.get('http://mysirius.me/settings/accountinformation')  # Goes to settings page
    time.sleep(1)
    F = open('../TestCases/UserNameTestCases.txt', 'r')
    UserName = (F.readline()).rstrip('\n')  # Username now equals the first element in the file
    F.close()

    ChangeUserName = ClickFnHttp(Driver, "/html/body/div/div/div/div[2]/button[1]")
    NewUserName = SendKeysFnHttp(Driver, "/html/body/div/div/div/div[2]/input", UserName)
    Save = ClickFnHttp(Driver, "/html/body/div/div/div/div[2]/button")
    time.sleep(1)
    Driver.get('http://mysirius.me/settings/accountinformation')  # Goes to settings page
    time.sleep(1)
    Driver.get('http://mysirius.me/settings/accountinformation')  # Goes to settings page
    time.sleep(1)

    # Entering same username again
    ChangeUserName = ClickFnHttp(Driver, "/html/body/div/div/div/div[2]/button[1]")
    NewUserName = SendKeysFnHttp(Driver, "/html/body/div/div/div/div[2]/input", UserName)
    Save = ClickFnHttp(Driver, "/html/body/div/div/div/div[2]/button")
    # Finished username











    #//////////////////////////////// Changing email
    time.sleep(1)
    Driver.get('http://mysirius.me/settings/accountinformation')  # Goes to settings page
    time.sleep(1)
    F = open('../TestCases/EmailTestCases.txt', 'r')
    Email = (F.readline()).rstrip('\n')  # Email now equals the first element in the file
    F.close()

    ChangeEmail = ClickFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/button[2]")
    NewEmail = SendKeysFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/input", Email)
    Save = ClickFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/button")
    time.sleep(1)
    Driver.get('http://mysirius.me/settings/accountinformation')  # Goes to settings page
    time.sleep(1)


    # Entering same email again
    ChangeEmail = ClickFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/button[2]")
    NewEmail = SendKeysFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/input", "ultimatehacker925@yahoo.com")
    Save = ClickFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/button")
    time.sleep(1)
    Driver.get('http://mysirius.me/settings/accountinformation')  # Goes to settings page
    time.sleep(1)

    # Entering same email again
    ChangeEmail = ClickFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/button[2]")
    NewEmail = SendKeysFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/input", "wrongemail@fake.com")
    Save = ClickFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/button")
    time.sleep(1)
    Driver.get('http://mysirius.me/settings/accountinformation')  # Goes to settings page
    time.sleep(1)

    # Testing the new email
    time.sleep(1)
    Driver.get('http://mysirius.me/signin')  # Goes to sign in page
    time.sleep(1)

    time.sleep(1)
    EmailField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[1]', "wrongemail@fake.com", 1)  # Writes the email in the email field
    time.sleep(1)
    PasswordField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[2]', Password, 1)  # Writes the password in the password field
    time.sleep(1)
    LoginButton = ClickFnHttp(Driver, '/html/body/div/div/div/form/button[2]', 1)
    time.sleep(2)

    Driver.get('http://mysirius.me/settings/accountinformation')  # Goes to settings page
    time.sleep(1)
    # Entering my email again
    ChangeEmail = ClickFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/button[2]")
    NewEmail = SendKeysFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/input", "ultimatehacker925@yahoo.com")
    Save = ClickFnHttp(Driver, "/html/body/div[1]/div/div/div[2]/button")
    time.sleep(1)

    Driver.get('http://mysirius.me/settings/accountinformation')  # Goes to settings page
    time.sleep(1)











