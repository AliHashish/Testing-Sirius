from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from Utilities import *
from pyautogui import *
import pyautogui
def AdminUserOptions(Driver):
    # Driver = webdriver.Firefox(executable_path=r'..\..\..\gecko\geckodriver.exe')
    Driver.get('http://mysirius.me/home')  # Goes to home page
    time.sleep(1)
    SwitchToAdmin = ClickFnHttp(Driver, "/html/body/div/div/div/div[1]/div[1]/div/div[2]/a/button")
    for i in range(12):
        pyautogui.press("down")     # scrolling down a bit
    Users = ClickFnHttp(Driver, "/html/body/div/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/a/div")
    Search = SendKeysFnHttp(Driver, "/html/body/div/div/div/div[2]/div/div[1]/input", "TestingTeams")
    FirstUserStatistics= ClickFnHttp(Driver, "/html/body/div/div/div/div[2]/div/div[2]/div/button[1]")
    time.sleep(4)
    Driver.get('http://mysirius.me/admin/user')  # Goes to Admin user page
    time.sleep(1)

    FirstUserProfile = ClickFnHttp(Driver, "/html/body/div/div/div/div[2]/div/div[2]/div/div[3]/a")
    time.sleep(1)
    Driver.get('http://mysirius.me/admin/user')  # Goes to Admin user page
    time.sleep(1)
    SomeUserBan = ClickFnHttp(Driver, "/html/body/div/div/div/div[2]/div/div[28]/div/button[2]")
    Cancel = ClickFnHttp(Driver, "/html/body/div[2]/div[3]/button[2]")
    SomeUserBan = ClickFnHttp(Driver, "/html/body/div/div/div/div[2]/div/div[28]/div/button[2]")
    ###################################################### Ban = ClickFnHttp(Driver, "/html/body/div[2]/div[3]/button[1]")

    time.sleep(1)
    Driver.get('http://mysirius.me/admin/user')  # Goes to Admin user page
    time.sleep(1)
    SomeUserReport = ClickFnHttp(Driver, "/html/body/div/div/div/div[2]/div/div[27]/div/div[4]/a")

    ReturnToUser = ClickFnHttp(Driver, "/html/body/div/div/div/div[1]/div/div[3]/a/button")

    # Cancel = Driver.find_element(by=By.XPATH, value=
    #     '/html/body/div[2]/div[3]/button')
    # time.sleep(1)
    # Cancel.click()
    # time.sleep(1)
    #
    # SecondUserStatistics = Driver.find_element(by=By.XPATH, value=
    #     '/html/body/div/div/div/div[2]/div/div[3]/div/button[1]')
    #
    # time.sleep(1)
    # SecondUserStatistics.click()
    # time.sleep(1)
    #
    # Cancel = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div[2]/div[3]/button')
    # time.sleep(1)
    # Cancel.click()
    # time.sleep(1)
    #
    #
    #
    #
    #
    #
    #
    # FirstUserProfile = Driver.find_element(by=By.XPATH, value=
    #     '/html/body/div/div/div/div[2]/div/div[2]/div/div[3]/a')
    #
    # time.sleep(1)
    # FirstUserProfile.click()
    # time.sleep(3)
    #
    # Driver.get('http://34.236.108.123/adminView/User') # Returns to admin user page
    # time.sleep(1)
    #
    # SecondUserProfile = Driver.find_element(by=By.XPATH, value=
    #     '/html/body/div/div/div/div[2]/div/div[3]/div/div[3]/a')
    #
    # time.sleep(1)
    # SecondUserProfile.click()
    # time.sleep(3)
    #
    # Driver.get('http://34.236.108.123/adminView/User')  # Returns to admin user page
    # time.sleep(1)
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # FirstUserReport = Driver.find_element(by=By.XPATH, value=
    #     '/html/body/div/div/div/div[2]/div/div[2]/div/div[4]')
    #
    # time.sleep(1)
    # FirstUserReport.click()
    # time.sleep(3)
    #
    # Driver.get('http://34.236.108.123/adminView/User')  # Returns to admin user page
    # time.sleep(1)
    #
    # SecondUserReport = Driver.find_element(by=By.XPATH, value=
    #     '/html/body/div/div/div/div[2]/div/div[3]/div/div[4]')
    #
    # time.sleep(1)
    # SecondUserReport.click()
    # time.sleep(3)
    #
    # Driver.get('http://34.236.108.123/adminView/User')  # Returns to admin user page
    # time.sleep(1)
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # FirstUserBan = Driver.find_element(by=By.XPATH, value=
    #     '//*[@id="4"]')
    #
    # time.sleep(1)
    # FirstUserBan.click()
    # time.sleep(3)
    #
    # Cancel = Driver.find_element(by=By.XPATH,value=
    #     '/html/body/div[2]/div[3]/button[2]')
    # time.sleep(1)
    # Cancel.click()
    # time.sleep(3)
    #
    # FirstUserBan = Driver.find_element(by=By.XPATH, value=
    #     '//*[@id="4"]')
    #
    # time.sleep(1)
    # FirstUserBan.click()
    # time.sleep(3)
    #
    # Ban = Driver.find_element(by=By.XPATH, value=
    #     '/html/body/div[2]/div[3]/button[1]')
    #
    # time.sleep(1)
    # Ban.click()
    # time.sleep(3)
    #
    #
    #
    #
    #
    #
    # SecondUserBan = Driver.find_element(by=By.XPATH, value=
    # '//*[@id="6"]')
    #
    # time.sleep(1)
    # SecondUserBan.click()
    # time.sleep(3)
    #
    # Cancel = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div[2]/div[3]/button[2]')
    # time.sleep(1)
    # Cancel.click()
    # time.sleep(3)
    #
    # SecondUserBan = Driver.find_element(by=By.XPATH, value=
    # '//*[@id="6"]')
    #
    # time.sleep(1)
    # SecondUserBan.click()
    # time.sleep(3)
    #
    # Ban = Driver.find_element(by=By.XPATH, value=
    # '/html/body/div[2]/div[3]/button[1]')
    #
    # time.sleep(1)
    # Ban.click()
    # time.sleep(3)

