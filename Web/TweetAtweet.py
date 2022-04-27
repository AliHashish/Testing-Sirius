from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

# this file is modified

def TweetAtweet(Driver, Mode= 1):
    #simillarly like Function of Enter emails 
    #but with no modes given text file containg cases of different tweets 
    #it is going to run them down
    i = 1
    if Mode == 0:
        F = open('../TestCases/TweetTestCases.txt' , 'r')
        Quotes = [tweet.rstrip('\n') for tweet in F.readlines()]
        F.close()
        time.sleep(2)
        for quote in Quotes:
            TweetField = Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[2]/div[1]/div[1]/div[2]/div/textarea')
            time.sleep(2)
            TweetField.send_keys(quote)
            time.sleep(3)
            if len(quote) > 0 and len(quote) <= 280:
                TweetButton = Driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[2]/div[1]/div[1]/div[2]/div/input')
                TweetButton.click()
                print("Tweeted: ", i)
                i=i+1
                time.sleep(2)
            else:
                print("cant tweet empty tweet nor larger than 281 char!! im the quote = ", quote)
            time.sleep(3)
    else:
        F = open('../TestCases/TweetTestCases.txt', 'r')
        Quotes = (F.readline()).rstrip('\n')
        F.close()
        time.sleep(2)
        TweetField = Driver.find_element(by=By.XPATH, value=
            '/html/body/div/div/div/div[2]/div[1]/div[1]/div[2]/div/textarea')
        time.sleep(2)
        TweetField.send_keys(Quotes)
        time.sleep(3)
        if len(Quotes) > 0 and len(Quotes) <= 280:
            TweetButton = Driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[2]/div[1]/div[1]/div[2]/div/input')
            TweetButton.click()
            time.sleep(3)
        else:
            print("cant tweet empty tweet nor larger than 281 char!! im the quote = ", Quotes)
        time.sleep(3)