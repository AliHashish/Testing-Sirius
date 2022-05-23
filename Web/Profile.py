from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
# import keyboard
from pyautogui import *
import pyautogui
from Utilities import ClickFnHttp
#this file has been modified

def ProfileTest(Driver):
    #after login click on profile icon
    # time.sleep(3)
    # ProfileIcon = Driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]')
    # time.sleep(3)
    # ProfileIcon.click()
    # time.sleep(3)

    ###NEW
    Driver.get('http://34.236.108.123/profile')
    time.sleep(1)
    # Uncomment this part when you're visiting another user's profile, not your own
    # FollowButton = Driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button[3]') #FOR SIRIUS FOLLOW BUTTON
    # time.sleep(1)
    # FollowButton.click()
    # time.sleep(1)
    # ### for unfollow
    # FollowButton.click()
    # time.sleep(1)
    # UnFollowButton = Driver.find_element(by=By.XPATH, value= '/html/body/div[2]/div[3]/button[1]') #confirms the unfollow
    # UnFollowButton.click()
    # time.sleep(1)
    # ## for cancelling the confirmation
    # FollowButton.click()
    # time.sleep(1)
    # FollowButton.click()
    # time.sleep(1)
    # CancelButton = Driver.find_element(by=By.XPATH, value = '/html/body/div[2]/div[3]/button[2]') #cancels the unollow
    # CancelButton.click()
    # time.sleep(3) #Should Be following the user after this step
    ###END

    TweetAndRetweetField = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[4]/div/div/div/a[2]/button', 1)
    # TweetsAndRetweetsField = Driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[4]/div/div/div/a[2]/button') #MODIFIED FOR SIRIUS
    # time.sleep(1)
    # TweetsAndRetweetsField.click()

    MediaField = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[4]/div/div/div/a[3]/button', 1)
    # MediaFeild = Driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[4]/div/div/div/a[3]/button') #MODIFIED FOR SIRIUS
    # time.sleep(1)
    # MediaFeild.click()

    LikesField = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[4]/div/div/div/a[4]/button', 1)
    # LikesField = Driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[4]/div/div/div/a[4]/button')  #MODIFIED FOR SIRIUS
    # time.sleep(1)
    # LikesField.click()
    # time.sleep(1)

    TweetsField = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[4]/div/div/div/a[1]/button', 1)
    # TweetsFields = Driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[4]/div/div/div/a[1]/button') #MODIFIED FOR SIRIUS
    # time.sleep(1)
    # TweetsFields.click()
    # time.sleep(1)
    # ####

    #Followers list
    Followings = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[3]/div[3]/a[1]/span', 1)
    # Followings = Driver.find_element(by=By.XPATH, value = '/html/body/div/div/div/div[2]/div[1]/div[3]/div[3]/a[1]/span')
    # Followings.click()
    # time.sleep(1)

    pyautogui.press("down")
    time.sleep(2)
    pyautogui.press("up")
    time.sleep(2)

    # Backbutton = Driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[2]/div[1]/div[1]/div/a')
    # time.sleep(2)

    FollowerTab = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div/div/a[1]/button', 2)
    # FollowersTab = Driver.find_element(by=By.XPATH,value='/html/body/div/div/div/div[2]/div[1]/div[2]/div/div/a[1]/button')
    # time.sleep(2)
    # FollowersTab.click()
    # time.sleep(3)

    FollowingTab = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div/div/a[2]/button', 2)
    # FollowingTab = Driver.find_element(by=By.XPATH,value='/html/body/div/div/div/div[2]/div[1]/div[2]/div/div/a[2]/button')
    # FollowingTab.click()
    # time.sleep(3)

    #BackButton = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[1]/div/a', 1)
    # Backbutton.click()
    Driver.get('http://34.236.108.123/profile') #doesnt want to click on back button even though it is implemented correctly by FT
    time.sleep(3)

    Followers = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[3]/div[3]/a[2]/span', 2)
    # Followers = Driver.find_element(by=By.XPATH,value = '/html/body/div/div/div/div[2]/div[1]/div[3]/div[3]/a[2]/span')
    # Followers.click()
    # time.sleep(2)

    FollowingTab = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div/div/a[2]/button', 2)
    # FollowingTab2 = Driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[2]/div[1]/div[2]/div/div/a[2]/button') #New Variable because
    # FollowingTab2.click()
    # time.sleep(2)

    FollowerTab = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div/div/a[1]/button', 2)
    # FollowersTab2 = Driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[2]/div[1]/div[2]/div/div/a[1]/button')
    # time.sleep(2)
    # FollowersTab2.click()
    # time.sleep(2)

    # BackButton = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[1]/div/a', 1)
    # Backbutton.click()
    Driver.get('http://34.236.108.123/profile')  # doesnt want to click on back button even though it is implemented correctly by FT
    time.sleep(2)

    ##Notification Bell
    #NotificationBell = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button[2]', 1)

    # NotificationBell = Driver.find_element(by=By.XPATH,value = '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button[2]')
    # NotificationBell.click()
    # time.sleep(2)
    #####

    # MoreSettingsButton = ClickFnHttp(Driver, '//*[@id="root"]/div/div/div[2]/div[1]/div[2]/div[3]/div/button[1]', 2)
    # MoreSettingsButton = Driver.find_element(by=By.XPATH,value = '//*[@id="root"]/div/div/div[2]/div[1]/div[2]/div[3]/div/button[1]')
    # MoreSettingsButton.click()
    # time.sleep(2)


    # EditProfileButton = Driver.find_element_by_xpath('                                           #dont uncomment this
    #       /html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/a')
    # time.sleep(3)
    # EditProfileButton.click()
    # time.sleep(3)

    #EditprofileButton = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div/div[2]/div[3]/button', 2)
    # EditProfileButton = Driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/div[3]/button')
    # time.sleep(3)
    # EditProfileButton.click()
    # time.sleep(3)

    # CloseButton = ClickFnHttp(Driver, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[1]/div', 2)
    # CloseButton = Driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[1]/div')
    # time.sleep(3)
    # CloseButton.click()
    # time.sleep(3)