import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def ClickFnHttp(Driver,http,T): #should pass http as string parameter
    try:
        button = Driver.find_element(by=By.XPATH,value=http)
        time.sleep(T)
        button.click()
        time.sleep(T)
    except:
        print("Element not found.")

def ClickFnID(Driver,ID,T): #pass ID of button
    try:
        button = Driver.find_element(by=By.ID, value=ID)
        time.sleep(T)
        button.click()
        time.sleep(T)
    except:
        print("Element not found.")

def SendKeysFnHttp(Driver,http,value,T):
    try:
        button = Driver.find_element(by=By.XPATH, value=http)
        time.sleep(T)
        button.send_keys(value)
        time.sleep(T)
    except:
        print("Element not found.")

def SendKeysFnID(Driver,ID,value,T):
    try:
        button = Driver.find_element(by=By.ID, value=ID)
        time.sleep(T)
        button.send_keys(value)
        time.sleep(T)
    except:
        print("Element not found.")

def SelectFnHttp(Driver,http,index,T):
    try:
        Field = Select(Driver.find_element(by=By.XPATH, value=http))
        time.sleep(T)
        Field.select_by_index(index)
        time.sleep(T)
    except:
        print("Element not found.")

def SelectFnHttp(Driver,ID,index,T):
    try:
        Field = Select(Driver.find_element(by=By.ID, value=ID))
        time.sleep(T)
        Field.select_by_index(index)
        time.sleep(T)
    except:
        print("Element not found.")