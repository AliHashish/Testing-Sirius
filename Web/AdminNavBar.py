from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from Utilities import *

def AdminNavBar(Driver):
    # Driver = webdriver.Firefox(executable_path=r'..\..\..\gecko\geckodriver.exe')
    # Driver.get('http://mysirius.me/admin/dashboard')  # Goes to Admin page
    # time.sleep(3)
    Driver.get('http://mysirius.me/home')  # Goes to home page
    time.sleep(1)
    SwitchToAdmin = ClickFnHttp(Driver, "/html/body/div/div/div/div[1]/div[1]/div/div[2]/a/button")

    Users = Driver.find_element(by=By.XPATH, value=
        '/html/body/div/div/div/div[1]/div[2]/a[2]/div/h4')
    time.sleep(1)
    Users.click()
    time.sleep(1)

    Dashboard = Driver.find_element(by=By.XPATH, value=
        '/html/body/div/div/div/div[1]/div[2]/a[1]/div/h4')
    time.sleep(1)
    Dashboard.click()
    time.sleep(1)

    Sirius = Driver.find_element(by=By.XPATH, value=
        '/html/body/div/div/div/div[1]/div[1]/a/h1')
    time.sleep(1)
    Sirius.click()
    time.sleep(1)

    Users = Driver.find_element(by=By.XPATH, value=
        '/html/body/div/div/div/div[1]/div[2]/a[2]/div/h4')
    time.sleep(1)
    Users.click()
    time.sleep(1)

    SearchField = Driver.find_element(by=By.XPATH, value=
        '/html/body/div/div/div/div[2]/div/div[1]/input')
    time.sleep(1)
    SearchField.send_keys('Sad People')
    time.sleep(3)

    Sirius = Driver.find_element(by=By.XPATH, value=
        '/html/body/div/div/div/div[1]/div[1]/a/h1')
    time.sleep(1)
    Sirius.click()
    time.sleep(1)
    # time.sleep(3)

    Dashboard = Driver.find_element(by=By.XPATH, value=
    '/html/body/div/div/div/div[1]/div[2]/a[1]/div/h4')
    time.sleep(1)
    Dashboard.click()
    time.sleep(1)

    Users = Driver.find_element(by=By.XPATH, value=
        '/html/body/div/div/div/div[1]/div[2]/a[2]/div/h4')
    time.sleep(1)
    Users.click()
    time.sleep(1)

    # Lists = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div/div/div/div[1]/div/a[7]/div/h4')
    # time.sleep(3)
    # Lists.click()

    # Settings = Driver.find_element(by=By.XPATH, value=
    #     '/html/body/div/div/div/div[1]/div/a[8]/div/h4')
    # time.sleep(1)
    # Settings.click()
    # time.sleep(1)
    #
    #
    # Home = Driver.find_element(by=By.XPATH, value=
    #     '/html/body/div/div/div/div[1]/div/a[2]/div/h4')
    # time.sleep(1)
    # Home.click()
    # time.sleep(1)

