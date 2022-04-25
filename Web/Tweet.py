from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
######
#gozz2 7ashish ana asef :(
######
def Tweet(Driver):
    #check return to user profile
    #go to profile from Profile Icon
    Small_Profile_Icon_Redirect = Driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/a')
    Small_Profile_Icon_Redirect.click()
    time.sleep(2)
    # to return back
    BackButton=Driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[2]/div[1]/div[1]/div/a')
    BackButton.click()
    time.sleep(2)
    #now we are back to the original tweet (no check by clicking on the name
    Profile_Name_Redirect = Driver.find_element(by=By.XPATH,value='/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/h3/div[1]/a')
    Profile_Name_Redirect.click()
    time.sleep(3)
    ##username
    Username_Redirect = Driver.find_element(by=By.XPATH,value='/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/h3/div[1]/span/a')
    Username_Redirect.click()
    time.sleep(2)
    ##tweet settings
    Tweet_AdditionalSettings = Driver.find_element(by=By.XPATH,value='/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/h3/div[2]/button')
    Tweet_AdditionalSettings.click()
    time.sleep(2)
    Tweet_AdditionalSettings.click()
    ##like
    like = Driver.find_element(by=By.XPATH,value='/html/body/div/div/div/div[2]/div[2]/div[3]/span/button[3]')
    like.click()
    time.sleep(2)
    ##retweet
    retweet = Driver.find_element(by=By.XPATH,value='/html/body/div/div/div/div[2]/div[2]/div[3]/span/button[2]')
    retweet.click()
    time.sleep(2)
    ##bookmark
    bookmark = Driver.find_element(by=By.XPATH,value='/html/body/div/div/div/div[2]/div[2]/div[3]/span/button[4]')
    bookmark.click()
    time.sleep(2)


