from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from MobUtilities import *
def NavBar(Driver):
    NavBar = ClickFnHttp(Driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]', 2)
    Profile = ClickFnHttp(Driver,'//android.view.View[@content-desc="Profile"]')
    Driver.back()
    Notification = ClickFnHttp(Driver, '//android.view.View[@content-desc="Notifications"]')
    Driver.back()
    Bookmarks = ClickFnHttp(Driver, '//android.view.View[@content-desc="Bookmarks"]')
    Driver.back()
    Inbox = ClickFnHttp(Driver, '//android.view.View[@content-desc="Inbox"]')
    Driver.back()
    Settings = ClickFnHttp(Driver, '//android.view.View[@content-desc="Settings"]')
    Driver.back()
    Policies = ClickFnHttp(Driver, '//android.view.View[@content-desc="Policies"]')
    Driver.back()
    AdminView = ClickFnHttp(Driver, '//android.view.View[@content-desc="Admin View"]')
    Driver.back()
    Policies = ClickFnHttp(Driver, '//android.view.View[@content-desc="Policies"]')
    Driver.back()