import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def ClickFnHttp(Driver,http): #should pass http as string parameter
    try:
        button = Driver.find_element(by=By.XPATH,value=http)
        time.sleep(2)
        button.click()
        time.sleep(2)
    except:
        print("Element not found.")

def ClickFnID(Driver,ID): #pass ID of button
    try:
        button = Driver.find_element(by=By.ID, value=ID)
        time.sleep(2)
        button.click()
        time.sleep(2)
    except:
        print("Element not found.")

def SendKeysFnHttp(Driver,http,value):
    try:
        button = Driver.find_element(by=By.XPATH, value=http)
        time.sleep(2)
        button.send_keys(value)
        time.sleep(2)
    except:
        print("Element not found.")

def SendKeysFnID(Driver,ID,value):
    try:
        button = Driver.find_element(by=By.ID, value=ID)
        time.sleep(2)
        button.send_keys(value)
        time.sleep(2)
    except:
        print("Element not found.")

def SelectFnHttp(Driver,http,index):
    try:
        Field = Select(Driver.find_element(by=By.XPATH, value=http))
        time.sleep(1)
        Field.select_by_index(index)
        time.sleep(1)
    except:
        print("Element not found.")

def SelectFnHttp(Driver,ID,index):
    try:
        Field = Select(Driver.find_element(by=By.ID, value=ID))
        time.sleep(1)
        Field.select_by_index(index)
        time.sleep(1)
    except:
        print("Element not found.")