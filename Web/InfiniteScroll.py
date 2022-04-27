from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import keyboard
from pyautogui import *
import pyautogui

#this file has been modified

def InfiniteScroll(Driver):
    Driver.get('http://34.236.108.123/home')
    time.sleep(1)

    while keyboard.is_pressed('q') == False:  # 3lshan a2dar awa2af el code
        pyautogui.press("down")
        time.sleep(2)

    while keyboard.is_pressed('s') == False:  # 3lshan a2dar awa2af el code
        pyautogui.press("up")
        time.sleep(2)
