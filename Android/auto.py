import self as self
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from MobUtilities import *
from AndroidTweeting import AndroidTweeting
from Interactable import Buttons
from selenium.webdriver.common.by import By
import time
from MobSignIn import Signin

#overall bugs till now
    #every scroll does a click
    #bookmarks tab is not working
    #doent post the tweet outside
    #when clicking on the icon of the navigation bar then clicks on notification ====> i want to go back so i click on the same icon brfore it returns me to the profile page
#in tweeting a tweet:
    #not limit for the tweet it self
    #tweet button not working
    #no scrolling when scrolling it clicks on the tweet

DesiredCapabilities = {
    "platformName": "Android",
    "platformVersion": "11",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", DesiredCapabilities)
#first run the program then start the test
##login step
# Signin(driver)

##tweet at home step
# AndroidTweeting(driver) #tweeting a tweet DONE
# Buttons(driver)

# print("aloooo")


