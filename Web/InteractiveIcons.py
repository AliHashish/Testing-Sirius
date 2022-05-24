from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from Utilities import ClickFnHttp

def InteractiveIcons(Driver):
    Driver.get('http://mysirius.me/home')
    time.sleep(3)

    Bookmark =ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[2]/div[2]/span/button[4]',1)
    # Bookmark = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[2]/div[2]/div[2]/span/button[4]')
    # time.sleep(1)
    # Bookmark.click()
    # time.sleep(1)

    Bookmark = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[3]/div[2]/span/button[4]', 1)
    # Bookmark = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[2]/div[3]/div[2]/span/button[4]')
    # time.sleep(1)
    # Bookmark.click()
    # time.sleep(1)

    Comment = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[2]/div[2]/span/button[1]', 1)
    # Comment = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[2]/div[2]/div[2]/span/button[1]')
    # time.sleep(1)
    # Comment.click()
    # time.sleep(1)

    Retweet = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[2]/div[2]/span/button[2]', 1)
    # Retweet = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[2]/div[2]/div[2]/span/button[2]')
    # time.sleep(1)
    # Retweet.click()
    # time.sleep(1)

    Like = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[2]/div[2]/span/button[3]', 1)
    # Like = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[2]/div[2]/div[2]/span/button[3]')
    # time.sleep(1)
    # Like.click()
    # time.sleep(1)

    Bookmark = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[2]/div[2]/span/button[4]', 1)
    # Bookmark = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[2]/div[2]/div[2]/span/button[4]')
    # time.sleep(1)
    # Bookmark.click()
    # time.sleep(1)

    Comment = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[4]/div[2]/span/button[1]', 1)
    # Comment = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[2]/div[4]/div[2]/span/button[1]')
    # time.sleep(1)
    # Comment.click()
    # time.sleep(1)

    Retweet = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[4]/div[2]/span/button[2]', 1)
    # Retweet = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[2]/div[4]/div[2]/span/button[2]')
    # time.sleep(1)
    # Retweet.click()
    # time.sleep(1)

    Like = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[4]/div[2]/span/button[3]', 1)
    # Like = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[2]/div[4]/div[2]/span/button[3]')
    # time.sleep(1)
    # Like.click()
    # time.sleep(1)

    Boo0kmark = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[4]/div[2]/span/button[4]', 1)
    # Bookmark = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[2]/div[4]/div[2]/span/button[4]')
    # time.sleep(1)
    # Bookmark.click()
    # time.sleep(1)

    Comment = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[4]/div[2]/span/button[1]', 1)
    # Comment = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[2]/div[4]/div[2]/span/button[1]')
    # time.sleep(1)
    # Comment.click()
    # time.sleep(1)

    Rwtweet = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[4]/div[2]/span/button[2]', 1)
    # Retweet = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[2]/div[4]/div[2]/span/button[2]')
    # time.sleep(1)
    # Retweet.click()
    # time.sleep(1)

    Like = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[4]/div[2]/span/button[3]', 1)
    # Like = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[2]/div[4]/div[2]/span/button[3]')
    # time.sleep(1)
    # Like.click()
    # time.sleep(1)

    Bookmark = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[4]/div[2]/span/button[4]', 1)
    # Bookmark = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[2]/div[4]/div[2]/span/button[4]')
    # time.sleep(1)
    # Bookmark.click()
    # time.sleep(1)

    Options = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/h3/div[2]/button', 1)
    # Options = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/h3/div[2]/button')
    # time.sleep(1)
    # Options.click()
    # time.sleep(1)

    Delete = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div/p[1]', 1)
    # Delete = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div[2]/div[3]/div/p[1]')
    # #/html/body/div[2]/div[3]/div/p[1]/div
    # time.sleep(1)
    # Delete.click()
    # time.sleep(1)

    Pin = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div/p[2]', 1)
    # Pin = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div[2]/div[3]/div/p[2]')
    # time.sleep(1)
    # Pin.click()
    # time.sleep(1)

    # Report = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div/p[3]', 1)
    # Report = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div[2]/div[3]/div/p[3]')
    # time.sleep(1)
    # Report.click()
    # time.sleep(1)

    # Mute = ClickFnHttp(Driver,'/html/body/div[2]/div[3]/div/p[4]', 1)
    # Mute = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div[2]/div[3]/div/p[4]')
    # time.sleep(1)
    # Mute.click()
    # time.sleep(1)

    Driver.get('http://mysirius.me/home')
    time.sleep(3)

    Tweet = ClickFnHttp(Driver, '/html/body/div/div/div/div[1]/div/button', 1)
    # Tweet = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[1]/div/button')
    # time.sleep(1)
    # Tweet.click()
    # time.sleep(1)

    Account = ClickFnHttp(Driver, '/html/body/div/div/div/div[1]/div/footer/button/div[2]/div[1]', 1)
    # Account = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[1]/div/footer/button/div[2]/div[1]')
    # # '/html/body/div/div/div/div[1]/div/footer/button/div[3]/svg'
    # time.sleep(1)
    # Account.click()
    # time.sleep(1)

    AddAccount = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div/p[1]', 1)
    # AddAccount = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div[2]/div[3]/div/p[1]')
    # time.sleep(1)
    # AddAccount.click()
    # time.sleep(1)

    Logout = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div/p[2]', 1)
    # Logout = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div[2]/div[3]/div/p[2]')
    # time.sleep(1)
    # Logout.click()
    # time.sleep(1)

    Driver.get('http://mysirius.me/home')
    time.sleep(3)

    SearchField = ClickFnHttp(Driver, '/html/body/div/div/div/div[3]/div[1]/a/div/input', 1)
    # SearchField = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[3]/div[1]/a/div/input')
    # time.sleep(1)
    # SearchField.click()
    # time.sleep(1)

    Back = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div/div[1]/div[1]/a', 1)
    #aw '/html/body/div/div/div/div[2]/div/div[1]/div[1]/a'
    # Back = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[2]/div/div[1]/div[1]/a')
    # time.sleep(1)
    # Back.click()
    # time.sleep(1)

    WhatHappeneing = ClickFnHttp(Driver, '/html/body/div/div/div/div[3]/a/div', 1)
    # WhatHappening = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[3]/a/div')
    # time.sleep(1)
    # WhatHappening.click()
    # time.sleep(1)
