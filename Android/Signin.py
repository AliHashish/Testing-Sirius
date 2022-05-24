from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from Utilities import *
def Signin(Driver, Mode = 1):
    if Mode==0:

        F = open('../TestCases/EmailTestCases.txt', 'r')
        Emails = [Email.rstrip('\n') for Email in F.readlines()]  # Makes a list containing all email test cases
        F.close()

        F = open('../TestCases/PasswordTestCases.txt', 'r')
        Passwords = [Password.rstrip('\n') for Password in F.readlines()]  # Makes a list containing all Password test cases
        F.close()

        counter = 0

        for Email in Emails:
            for Password in Passwords:
                LoginField = ClickFnHttp(Driver, '//android.widget.Button[@content-desc="Log in"]', 2)
                for i in range(2):
                    counter +=1
                    print("Test number: ", counter)
                    print("Email: ", Email)
                    print("Password: ", Password)
                    print("")

                    #send email first
                    EmailField = ClickFnHttp(Driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText', 2)

                    EmailField = SendKeysFnHttp(Driver,
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText',Email, 2)
                    Driver.hide_keyboard()

                    NextField = ClickFnHttp(Driver, '//android.widget.Button[@content-desc="Next"]', 1)

                    if (i%2 == 0):
                        time.sleep(1)
                        ShowPassword = ClickFnHttp(Driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText/android.widget.Button', 1)

                    time.sleep(2)
                    PasswordField = ClickFnHttp(Driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText',2)
                    PasswordField = SendKeysFnHttp(Driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText', Password, 2)
                    Driver.hide_keyboard()
                    NextField = ClickFnHttp(Driver, '//android.widget.Button[@content-desc="Next"]', 1)
                    Driver.back()
    else:
        F = open('../TestCases/EmailTestCases.txt', 'r')
        Emails = (F.readline()).rstrip('\n')  # Email now equals the first element in the file
        F.close()

        F = open('../TestCases/PasswordTestCases.txt', 'r')
        Passwords = (F.readline()).rstrip('\n')  # Password now equals the first element in the file
        F.close()

        LoginField = ClickFnHttp(Driver, '//android.widget.Button[@content-desc="Log in"]', 2)

        # send email first
        # EmailField = ClickFnHttp(Driver,
        #         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText',3)

        EmailField = Driver.find_element(by=By.XPATH,value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText')
        time.sleep(2)
        EmailField.click()
        time.sleep(2)
        EmailField.send_keys(Emails)
        time.sleep(2)
        Driver.hide_keyboard()
        # EmailField = SendKeysFnHttp(Driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText', Emails, 2)
        # Driver.hide_keyboard()
        print("t")
        NextField = ClickFnHttp(Driver, '//android.widget.Button[@content-desc="Next"]', 1)

        PasswordField = ClickFnHttp(Driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText', 2)
        PasswordField = SendKeysFnHttp(Driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText', Passwords, 2)
        Driver.hide_keyboard()

        ShowPassword = ClickFnHttp(Driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText/android.widget.Button', 2)
        ShowPassword = ClickFnHttp(Driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText/android.widget.Button', 1)
        time.sleep(1)

        NextField = ClickFnHttp(Driver, '//android.widget.Button[@content-desc="Next"]', 1)
        time.sleep(3)
        Driver.back()