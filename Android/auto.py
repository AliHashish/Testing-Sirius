#import self as self
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from MobUtilities import *
from AndroidTweeting import AndroidTweeting
from Interactable import Buttons
from selenium.webdriver.common.by import By
import time
from MobSignIn import Signin
from NavBar import NavBar
from Settings import Settings

#overall bugs till now
    #every scroll does a click
    #bookmarks tab is not working
    #doent post the tweet outside
    #when clicking on the icon of the navigation bar then clicks on notification ====> i want to go back so i click on the same icon brfore it returns me to the profile page
#in tweeting a tweet:
    #not limit for the tweet it self
    #tweet button not working
    #no scrolling when scrolling it clicks on the tweet

#######################################################################################################################
########### NEW BUGS ###########
# 1- When pressing profile ----> Tweet ----> Cancel = Runtime Error
# 2- Bookmarks doesn't work in NavBar
# 3- Tweeting in profile has no limits
# 4- When entering profile, then entering a huge bio description. it shows overflow in pixels error after saving
# 5- Upon opening Navbar and entering Inbox, we can't open Navbar again except through pressing back
# 6- When tweeting, no character limit. and doesn't wrap around text(enter a new line) when out of space
# 7- Tweets is not working
# 8- (An old unchanged error) When changing password, both "show password" icons are connected
# 9- When changing settings ----> Accountinfo ----> email ----> verify password, it says incorrect password, even though it is correct
# 10- When changing settings ----> Accountinfo ----> Country ----> doesn't open


# We are not sure whether the application is connected to the server database, but when signing up through web, you can't
##### access the same account through the application


DesiredCapabilities = {
    "platformName": "Android",
    "platformVersion": "11",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", DesiredCapabilities)
##first run the program then start the test
##login step
Signin(driver)
NavBar(driver)
Settings(driver)
Signin(driver)




##tweet at home step
# AndroidTweeting(driver) #tweeting a tweet DONE
# Buttons(driver)

# print("aloooo")


