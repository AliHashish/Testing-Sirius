from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome ( ChromeDriverManager().install() )

#this following proccess is ia a test on Logging in and tweeting a tweet 
#######==== start 
#their is alot of delays so you could see the process of Automations

time.sleep(3)
driver.get('https://twitter.com/i/flow/login')
time.sleep(3)

email = "abdoibrahim257@gmail.com" #Change Email here
password = "#0138415047" #Change password here

loginField = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
nextButton = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]')
time.sleep(3)
loginField.send_keys(email)
nextButton.click() #only available in real twitter they are two login screens

time.sleep(20) #for verification in case Enter manually in Real Twitter

passwordFeild= driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
LoginButtonFeild = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]')
time.sleep(3)
passwordFeild.send_keys(password)
time.sleep(3)
LoginButtonFeild.click() #press Login button

time.sleep(3)
tweet= "hi this is a test done using sellenium" #Change tweet Quote
ComposeTweetButton = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a') #available on real tweeter in order to do new tweet
time.sleep(6)
ComposeTweetButton.click()
time.sleep(3)


#this following path in real twitter changes acording to the window FullScreeen or Not 
TweetText= driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div') 
time.sleep(3)
TweetText.send_keys(tweet)
time.sleep(3)
tweetButton=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
time.sleep(10)
tweetButton.click()

time.sleep(15) #until the tweet is uploaded 

######=====END of logging in and tweeting test 



