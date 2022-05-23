import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def ClickFnHttp(Driver,http,time): #should pass http as string parameter
    try:
        button = Driver.find_element(by=By.XPATH,value=http)
        time.sleep(time)
        button.click()
        time.sleep(time)
    except:
        print("Element not found.")

def ClickFnID(Driver,ID,time): #pass ID of button
    try:
        button = Driver.find_element(by=By.ID, value=ID)
        time.sleep(time)
        button.click()
        time.sleep(time)
    except:
        print("Element not found.")

def SendKeysFnHttp(Driver,http,value,time):
    try:
        button = Driver.find_element(by=By.XPATH, value=http)
        time.sleep(time)
        button.send_keys(value)
        time.sleep(time)
    except:
        print("Element not found.")

def SendKeysFnID(Driver,ID,value,time):
    try:
        button = Driver.find_element(by=By.ID, value=ID)
        time.sleep(time)
        button.send_keys(value)
        time.sleep(time)
    except:
        print("Element not found.")

def SelectFnHttp(Driver,http,index,time):
    try:
        Field = Select(Driver.find_element(by=By.XPATH, value=http))
        time.sleep(time)
        Field.select_by_index(index)
        time.sleep(time)
    except:
        print("Element not found.")

def SelectFnHttp(Driver,ID,index,time):
    try:
        Field = Select(Driver.find_element(by=By.ID, value=ID))
        time.sleep(time)
        Field.select_by_index(index)
        time.sleep(time)
    except:
        print("Element not found.")