from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from EnterEmail import EnterEmail

Driver = webdriver.Chrome(ChromeDriverManager().install()) # uses google chrome
Driver.get('https://twitter.com/i/flow/login')
time.sleep(3)


EnterEmail(Driver)  # Entes the email, using the default testing mode
# Email = "ultimatehacker925@yahoo.com"
#
# LoginField = Driver.find_element(by=By.XPATH, value=
#     '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
# NextButton = Driver.find_element(by=By.XPATH, value=
#     '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]')
# time.sleep(3)
# LoginField.send_keys(Email) # Writes the email in the loginField
# time.sleep(2)
# NextButton.click()
# time.sleep(3)

Username = 'ProHackarz'
UsernameField = Driver.find_element(by=By.XPATH, value=
    '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
NextButton = Driver.find_element(by=By.XPATH, value=
    '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')
time.sleep(3)
UsernameField.send_keys(Username)
time.sleep(2)
NextButton.click()
time.sleep(3)


Password = 'passwordsa3ba'
PasswordField = Driver.find_element(by=By.XPATH, value=
    '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
LoginButton = Driver.find_element(by=By.XPATH, value=
    '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div')
time.sleep(3)
PasswordField.send_keys(Password)
time.sleep(2)
LoginButton.click()
time.sleep(3)

Tweet = 'Big Brother Is Watching...'
TweetField = Driver.find_element(by=By.XPATH, value=
    '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div')
time.sleep(3)
TweetField.send_keys(Tweet)
time.sleep(2)
TweetButton = Driver.find_element(by=By.XPATH, value=
    '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
time.sleep(3)
TweetButton.click()




time.sleep(20)