from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


def NavBar(Driver):

    Explore = Driver.find_element(by=By.XPATH, value=
                '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]/div')
    time.sleep(3)
    Explore.click()
    time.sleep(3)

    Notifications = Driver.find_element(by=By.XPATH, value=
                '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[3]/div')
    time.sleep(3)
    Notifications.click()
    time.sleep(3)

    Messages = Driver.find_element(by=By.XPATH, value=
                '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[4]/div')
    time.sleep(3)
    Messages.click()
    time.sleep(3)

    Bookmarks = Driver.find_element(by=By.XPATH, value=
    '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[5]/div')
    time.sleep(3)
    Bookmarks.click()
    time.sleep(3)

    Lists = Driver.find_element(by=By.XPATH, value=
    '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[6]/div')
    time.sleep(3)
    Lists.click()
    time.sleep(3)

    Profile = Driver.find_element(by=By.XPATH, value=
    '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]/div')
    time.sleep(3)
    Profile.click()
    time.sleep(3)

    Home = Driver.find_element(by=By.XPATH, value=
    '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[1]/div')
    time.sleep(3)
    Home.click()
    time.sleep(3)

