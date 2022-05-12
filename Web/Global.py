import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def ClickFnHttp(Driver,http): #should pass http as string parameter
    button = Driver.find_element(by=By.XPATH,value=http)
    time.sleep(2)
    button.click()
    time.sleep(2)

def ClickFnID(Driver,ID): #pass ID of button
    button = Driver.find_element(by=By.ID, value=ID)
    time.sleep(2)
    button.click()
    time.sleep(2)

def SendKeysFnHttp(Driver,http,value):
    button = Driver.find_element(by=By.XPATH, value=http)
    time.sleep(2)
    button.send_keys(value)
    time.sleep(2)

def SendKeysFnID(Driver,ID,value):
    button = Driver.find_element(by=By.ID, value=ID)
    time.sleep(2)
    button.send_keys(value)
    time.sleep(2)

def SelectFnHttp(Driver,http,index):
    Field = Select(Driver.find_element(by=By.XPATH, value=http))
    time.sleep(1)
    Field.select_by_index(index)
    time.sleep(1)

def SelectFnHttp(Driver,ID,index):
    Field = Select(Driver.find_element(by=By.ID, value=ID))
    time.sleep(1)
    Field.select_by_index(index)
    time.sleep(1)