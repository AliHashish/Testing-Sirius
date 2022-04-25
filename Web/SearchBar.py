from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

def SearchBar(Driver):
    SearchBarIcon = Driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]')
    time.sleep(3)
    SearchBarIcon.click()
    time.sleep(3)
    HomePageField = Driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[1]')
    time.sleep(3)
    HomePageField.click()
    time.sleep(3)
    SideSearchBar = Driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/section/div/div/div[8]/a')
    time.sleep(3)
    SideSearchBar.click()
    time.sleep(5)