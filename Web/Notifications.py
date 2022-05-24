from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from Utilities import ClickFnHttp

def Notifications(Driver):
    Driver.get('http://mysirius.me/notifications')
    time.sleep(1)
    Options = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div/div/a', 2)
    # Options = Driver.find_element(by=By.XPATH, value=
    #             '/html/body/div/div/div/div[2]/div/div/a')
    # time.sleep(1)
    # Options.click()
    # time.sleep(1)
    Driver.get('http://mysirius.me/home)')


