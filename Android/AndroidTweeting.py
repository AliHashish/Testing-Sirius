from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

def AndroidTweeting(Driver, Mode = 1):
    if Mode == 0:
        F = open('../TestCases/TweetTestCases.txt', 'r')
        Quotes = [tweet.rstrip('\n') for tweet in F.readlines()]
        F.close()
        # Quotes = "Testing team test 01"
        i=1
        for quote in Quotes:
            NewTweet = Driver.find_element(by=By.XPATH, value= '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button')
            time.sleep(2)
            NewTweet.click()
            time.sleep(2)
            WhatsHappening = Driver.find_element(by=By.XPATH, value= '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText')
            WhatsHappening.click()
            time.sleep(1)
            WhatsHappening.send_keys(quote)  # Doesnt tweet
            ##instead of tweeting this phase click on close
            time.sleep(2)
            CancelButton = Driver.find_element(by=By.XPATH, value='//android.widget.Button[@content-desc="Cancel"]')
            if len(quote) > 0 and len(quote) <= 280:
                TweetButton = Driver.find_element(by=By.XPATH, value='//android.widget.Button[@content-desc="Tweet"]')
                TweetButton.click()
                print("Tweeted: ", i)
                i=i+1
                time.sleep(2)
                CancelButton.click()
                time.sleep(2)
            else:
                CancelButton.click()
                time.sleep(2)
                print("cant tweet empty tweet nor larger than 281 char!! im the quote = ", quote)
    else:
        F = open('../TestCases/TweetTestCases.txt', 'r')
        Quotes = (F.readline()).rstrip('\n')
        F.close()
        # Quotes = "Testing team test 01"
        NewTweet = Driver.find_element(by=By.XPATH, value=
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button')
        time.sleep(2)
        NewTweet.click()
        time.sleep(2)
        WhatsHappening = Driver.find_element(by=By.XPATH,value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText')
        WhatsHappening.click()
        time.sleep(2)
        WhatsHappening.send_keys(Quotes) #Doesnt_tweet #bug #in sending long tweets it doesnt increment on to the next line
        time.sleep(2)
        CancelButton = Driver.find_element(by=By.XPATH, value='//android.widget.Button[@content-desc="Cancel"]')
        if len(Quotes) > 0 and len(Quotes) <= 280:
            TweetButton = Driver.find_element(by=By.XPATH, value='//android.widget.Button[@content-desc="Tweet"]')
            TweetButton.click()
            print("tweeted :) !")
            time.sleep(2)
            CancelButton.click()
            time.sleep(2)
        else: #doesnt prevent me from tweeting anyways nor increments the extra line
            print("cant tweet empty tweet nor larger than 281 char!! im the quote = ", Quotes)
        time.sleep(2)