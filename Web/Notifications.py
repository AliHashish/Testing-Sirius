from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


def Notifications(Driver):
    Driver.get('http://34.236.108.123/notifications')
    time.sleep(1)
    Options = Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[2]/div/div/a')
    time.sleep(1)
    Options.click()
    time.sleep(1)


