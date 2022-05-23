from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from Utilities import ClickFnHttp

def Bookmarks(Driver):
    Driver.get('http://34.236.108.123/home')
    time.sleep(1)

    Bookmark = ClickFnHttp(Driver,'/html/body/div/div/div/div[2]/div[2]/div[2]/span/button[4]',1)
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

    Bookmark = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[4]/div[2]/span/button[4]', 1)
    # Bookmark = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[2]/div[4]/div[2]/span/button[4]')
    # time.sleep(1)
    # Bookmark.click()
    # time.sleep(1)

    Bookmark = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[4]/div[2]/span/button[4]', 1)
    # Bookmark = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[2]/div[4]/div[2]/span/button[4]')
    # time.sleep(1)
    # Bookmark.click()
    # time.sleep(1)

    Driver.get('http://34.236.108.123/bookmarks')
    time.sleep(1)

    Bookmark = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[2]/div[2]/span/button[4]', 1)
    # Bookmark = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[2]/div[2]/div[2]/span/button[4]')
    # time.sleep(1)
    # Bookmark.click()
    # time.sleep(1)

    Bookmark = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[2]/div[2]/span/button[4]', 1)
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


    Driver.get('http://34.236.108.123/bookmarks')
    time.sleep(1)
