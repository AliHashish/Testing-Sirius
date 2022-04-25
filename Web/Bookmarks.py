from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


def Bookmarks(Driver):
    Driver.get('http://34.236.108.123/bookmarks')
    time.sleep(1)
    Options = Driver.find_element(by=By.XPATH, value=
        '/html/body/div/div/div/div[2]/div[1]/button')
    time.sleep(1)
    Options.click()
    time.sleep(1)

    ClearAll = Driver.find_element(by=By.XPATH, value=
        '/html/body/div[2]/div[3]/button')
    time.sleep(1)
    ClearAll.click()
    time.sleep(1)

    Clear = Driver.find_element(by=By.XPATH, value=
        '/html/body/div[3]/div[3]/button[1]')
    time.sleep(1)
    Clear.click()
    time.sleep(1)

    Options = Driver.find_element(by=By.XPATH, value=
        '/html/body/div/div/div/div[2]/div[1]/button')
    time.sleep(1)
    Options.click()
    time.sleep(1)

    ClearAll = Driver.find_element(by=By.XPATH, value=
        '/html/body/div[2]/div[3]/button')
    time.sleep(1)
    ClearAll.click()
    time.sleep(1)

    Cancel = Driver.find_element(by=By.XPATH, value=
        '/html/body/div[3]/div[3]/button[2]')
    time.sleep(1)
    Cancel.click()
    time.sleep(1)



