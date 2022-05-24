from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def TweetCompSchedule(Driver):
    Driver.get('http://mysirius.me/home')
    time.sleep(3)

    Schedule = Driver.find_element(by=By.XPATH, value=
    '/html/body/div/div/div/div[2]/div[1]/div[2]/div[4]/input')
    time.sleep(3)
    Schedule.click()
    time.sleep(3)

    Year = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[1]/div[3]/div/div/select'))
    time.sleep(1)
    Year.select_by_index(1)
    time.sleep(1)

    Month = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[1]/div[1]/div/div/select'))
    time.sleep(1)
    Month.select_by_index(8)
    time.sleep(1)

    Day = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[1]/div[2]/div/div/select'))
    time.sleep(1)
    Day.select_by_index(12)
    time.sleep(1)

    Hours = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[2]/div/div/select'))
    time.sleep(1)
    Hours.select_by_index(8)
    time.sleep(1)

    Minutes = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[3]/div/div/select'))
    time.sleep(1)
    Minutes.select_by_index(12)
    time.sleep(1)

    Am_Pm = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[4]/div/div/select'))
    time.sleep(1)
    Am_Pm.select_by_index(1)
    time.sleep(1)

    ConfirmSchedule = Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/button')
    time.sleep(3)
    ConfirmSchedule.click()
    time.sleep(1)










    Driver.get('http://mysirius.me/home')
    time.sleep(3)

    Schedule = Driver.find_element(by=By.XPATH, value=
    '/html/body/div/div/div/div[2]/div[1]/div[2]/div[4]/input')
    time.sleep(3)
    Schedule.click()
    time.sleep(3)

    Year = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[1]/div[3]/div/div/select'))
    time.sleep(1)
    Year.select_by_index(0)
    time.sleep(1)

    Month = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[1]/div[1]/div/div/select'))
    time.sleep(1)
    Month.select_by_index(0)
    time.sleep(1)

    Day = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[1]/div[2]/div/div/select'))
    time.sleep(1)
    Day.select_by_index(0)
    time.sleep(1)

    Hours = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[2]/div/div/select'))
    time.sleep(1)
    Hours.select_by_index(1)
    time.sleep(1)

    Minutes = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[3]/div/div/select'))
    time.sleep(1)
    Minutes.select_by_index(1)
    time.sleep(1)

    Am_Pm = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[4]/div/div/select'))
    time.sleep(1)
    Am_Pm.select_by_index(0)
    time.sleep(3)

    Driver.get('http://mysirius.me/home')
    time.sleep(3)

    Schedule = Driver.find_element(by=By.XPATH, value=
    '/html/body/div/div/div/div[2]/div[1]/div[2]/div[4]/input')
    time.sleep(3)
    Schedule.click()
    time.sleep(3)

    Year = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[1]/div[3]/div/div/select'))
    time.sleep(1)
    Year.select_by_index(0)
    time.sleep(1)

    Month = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[1]/div[1]/div/div/select'))
    time.sleep(1)
    Month.select_by_index(0)
    time.sleep(1)

    Day = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[1]/div[2]/div/div/select'))
    time.sleep(1)
    Day.select_by_index(0)
    time.sleep(1)

    Hours = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[2]/div/div/select'))
    time.sleep(1)
    Hours.select_by_index(1)
    time.sleep(1)

    Minutes = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[3]/div/div/select'))
    time.sleep(1)
    Minutes.select_by_index(1)
    time.sleep(1)

    Am_Pm = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[4]/div/div/select'))
    time.sleep(1)
    Am_Pm.select_by_index(0)
    time.sleep(3)




    Year = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[1]/div[3]/div/div/select'))
    time.sleep(1)
    Year.select_by_index(1)
    time.sleep(1)

    Month = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[1]/div[1]/div/div/select'))
    time.sleep(3)
    Month.select_by_index(6)
    time.sleep(1)

    Day = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[1]/div[2]/div/div/select'))
    time.sleep(1)
    Day.select_by_index(10)
    time.sleep(1)

    Hours = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[2]/div/div/select'))
    time.sleep(1)
    Hours.select_by_index(7)
    time.sleep(1)

    Minutes = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[3]/div/div/select'))
    time.sleep(1)
    Minutes.select_by_index(31)
    time.sleep(1)

    Am_Pm = Select(Driver.find_element(by=By.XPATH, value=
    '/html/body/div[2]/div[3]/div[4]/div/div/select'))
    time.sleep(1)
    Am_Pm.select_by_index(1)
    time.sleep(3)
