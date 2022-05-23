import self as self
from appium import webdriver
from AndroidTweeting import AndroidTweeting
from Interactable import Buttons
from selenium.webdriver.common.by import By
import time

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
    "deviceName": "Android Emulator"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", DesiredCapabilities)
#first run the program then start the test
##login step
##tweet at home step

# AndroidTweeting(driver) #tweeting a tweet DONE
# Buttons(driver)


#very importanttttt
# Next = driver.find_element(by=By.XPATH,value='//android.view.View[@content-desc="Notifications Select the kinds of notifications you get about your activities,interests and recommendations"]').click()
# action = TouchAction(driver)
# action.long_press(Next,2000)
# action.press()
# time.sleep(3)
######
