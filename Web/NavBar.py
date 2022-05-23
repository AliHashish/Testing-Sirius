from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from Utilities import ClickFnHttp

def NavBar(Driver):

    Explore = ClickFnHttp(Driver, '/html/body/div/div/div/div[1]/div/a[3]/div', 1)
    # Explore = Driver.find_element(by=By.XPATH, value=
    #             '/html/body/div/div/div/div[1]/div/a[3]/div')
    # time.sleep(1)
    # Explore.click()
    # time.sleep(1)

    Notification = ClickFnHttp(Driver, '/html/body/div/div/div/div[1]/div/a[4]/div/h4', 1)
    # Notifications = Driver.find_element(by=By.XPATH, value=
    #             '/html/body/div/div/div/div[1]/div/a[4]/div/h4')
    # time.sleep(1)
    # Notifications.click()
    # time.sleep(1)

    Messages = ClickFnHttp(Driver, '/html/body/div/div/div/div[1]/div/a[5]/div/h4', 1)
    # Messages = Driver.find_element(by=By.XPATH, value=
    #             '/html/body/div/div/div/div[1]/div/a[5]/div/h4')
    # time.sleep(1)
    # Messages.click()
    # time.sleep(1)

    Bookmarks = ClickFnHttp(Driver, 'html/body/div/div/div/div[1]/div/a[6]/div/h4', 1)
    # Bookmarks = Driver.find_element(by=By.XPATH, value=
    #     '/html/body/div/div/div/div[1]/div/a[6]/div/h4')
    # time.sleep(1)
    # Bookmarks.click()
    # time.sleep(1)

    # Lists = ClickFnHttp(Driver, '/html/body/div/div/div/div[1]/div/a[7]/div/h4', 1)
    # Lists = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[1]/div/a[7]/div/h4')
    # time.sleep(3)
    # Lists.click()
    # time.sleep(3)

    Profile = ClickFnHttp(Driver, '/html/body/div/div/div/div[1]/div/a[7]/div/h4', 1)
    # Profile = Driver.find_element(by=By.XPATH, value=
    #     '/html/body/div/div/div/div[1]/div/a[7]/div/h4')
    # time.sleep(1)
    # Profile.click()
    # time.sleep(1)

    Settings = ClickFnHttp(Driver, '/html/body/div/div/div/div[1]/div/a[8]/div/h4', 1)
    # Settings = Driver.find_element(by=By.XPATH, value=
    #     '/html/body/div/div/div/div[1]/div/a[8]/div/h4')
    # time.sleep(1)
    # Settings.click()
    # time.sleep(1)

    Home = ClickFnHttp(Driver, '/html/body/div/div/div/div[1]/div/a[2]/div/h4', 1)
    # Home = Driver.find_element(by=By.XPATH, value=
    #     '/html/body/div/div/div/div[1]/div/a[2]/div/h4')
    # time.sleep(1)
    # Home.click()
    # time.sleep(1)

