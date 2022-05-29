from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from MobUtilities import *
def Settings(Driver):
    NavBar = ClickFnHttp(Driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]', 2)
    Settings = ClickFnHttp(Driver, '//android.view.View[@content-desc="Settings"]')
    AccountInfo = ClickFnHttp(Driver, '//android.view.View[@content-desc="Account information See your account information like your phone number and email address."]/android.widget.Button')
    Driver.back()
    ChangePassword = ClickFnHttp(Driver, '//android.view.View[@content-desc="Change your password Change your password at any time."]/android.widget.Button')
    Driver.back()
    Audience = ClickFnHttp(Driver, '//android.view.View[@content-desc="Audience Manage what information you allow other people on twitter to see."]/android.widget.Button')
    Driver.back()
    Notifications = ClickFnHttp(Driver, '//android.view.View[@content-desc="Notifications Select the kind of notifications you get."]/android.widget.Button')
    Driver.back()
    DeactivateAccount = ClickFnHttp(Driver,'//android.view.View[@content-desc="Deactivate your account Find out how you can deactivate your account."]/android.widget.Button')
    Driver.back()

    Notifications = ClickFnHttp(Driver,'//android.view.View[@content-desc="Notifications Select the kind of notifications you get."]/android.widget.Button')
    Push = ClickFnHttp(Driver, '//android.view.View[@content-desc="Push notifications"]/android.widget.Switch')
    Driver.back()
    Notifications = ClickFnHttp(Driver,'//android.view.View[@content-desc="Notifications Select the kind of notifications you get."]/android.widget.Button')
    Push = ClickFnHttp(Driver, '//android.view.View[@content-desc="Push notifications"]/android.widget.Switch')
    Push = ClickFnHttp(Driver, '//android.view.View[@content-desc="Push notifications"]/android.widget.Switch')
    Back = ClickFnHttp(Driver, '//android.widget.Button[@content-desc="Back"]')

    Audience = ClickFnHttp(Driver, '//android.view.View[@content-desc="Audience Manage what information you allow other people on twitter to see."]/android.widget.Button')
    Protect = ClickFnHttp(Driver, '//android.view.View[@content-desc="Protect your Tweets"]/android.widget.Switch')
    Driver.back()
    Audience = ClickFnHttp(Driver, '//android.view.View[@content-desc="Audience Manage what information you allow other people on twitter to see."]/android.widget.Button')
    Protect = ClickFnHttp(Driver, '//android.view.View[@content-desc="Protect your Tweets"]/android.widget.Switch')
    Protect = ClickFnHttp(Driver, '//android.view.View[@content-desc="Protect your Tweets"]/android.widget.Switch')
    Back = ClickFnHttp(Driver, '//android.widget.Button[@content-desc="Back"]')

    ChangePassword = ClickFnHttp(Driver,'//android.view.View[@content-desc="Change your password Change your password at any time."]/android.widget.Button')
    CurrentPassword = SendKeysFnHttp(Driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]',"passwordsa3ba", 2)
    NewPassword = SendKeysFnHttp(Driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]',"passwordsa3bagedan", 2)

    ShowPassword1 = ClickFnHttp(Driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]/android.widget.Button')
    ShowPassword2 = ClickFnHttp(Driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]/android.widget.Button')
    Driver.back()

    AccountInfo = ClickFnHttp(Driver,'//android.view.View[@content-desc="Account information See your account information like your phone number and email address."]/android.widget.Button')
    Username = ClickFnHttp(Driver, '//android.view.View[@content-desc="Username user7"]')
    Driver.back()
    Phone = ClickFnHttp(Driver, '//android.view.View[@content-desc="Phone 123"]')
    Driver.back()
    Email = ClickFnHttp(Driver, '//android.view.View[@content-desc="Email"]')
    Driver.back()
    Country = ClickFnHttp(Driver, '//android.view.View[@content-desc="Country"]')
    Driver.back()

    Username = ClickFnHttp(Driver, '//android.view.View[@content-desc="Username user7"]')
    NewUsername = SendKeysFnHttp(Driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText', 'Testingusername',2)
    Driver.back()

    Email = ClickFnHttp(Driver, '//android.view.View[@content-desc="Email"]')
    ConfirmPassword = SendKeysFnHttp(Driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText', 'password',2)
    Next = ClickFnHttp(Driver,'//android.widget.Button[@content-desc="Next"]')
    Ok = ClickFnHttp(Driver,'//android.widget.Button[@content-desc="OK"]')
    Cancel = ClickFnHttp(Driver,'//android.widget.Button[@content-desc="Cancel"]')
    Logout = ClickFnHttp(Driver, '//android.widget.Button[@content-desc="Log out"]')
