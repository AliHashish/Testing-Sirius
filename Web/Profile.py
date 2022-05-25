from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
# import keyboard
from pyautogui import *
import pyautogui
from Utilities import *

#this file has been modified

def ProfileTest(Driver, Mode = 1):
    #after login click on profile icon
    # time.sleep(3)
    # ProfileIcon = Driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]')
    # time.sleep(3)
    # ProfileIcon.click()
    # time.sleep(3)

    ###NEW
    Driver.get('http://mysirius.me/home')
    time.sleep(1)
    ProfileIcon = ClickFnHttp(Driver, '/html/body/div/div/div/div[1]/div[1]/div/a[6]/div', 2)

    # Driver.get('http://mysirius.me/home')
    # time.sleep(1)
    # ProfileIcon = ClickFnHttp(Driver, '/html/body/div/div/div/div[1]/div[1]/div/a[6]/div', 2)
    # time.sleep(2)

    # Uncomment this part when you're visiting another user's profile, not your own
    # FollowButton = Driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button[3]') #FOR SIRIUS FOLLOW BUTTON
    # time.sleep(1)
    # FollowButton.click()
    # time.sleep(1)
    # ### for unfollow
    # FollowButton.click()
    # time.sleep(1)
    # UnFollowButton = Driver.find_element(by=By.XPATH, value= '/html/body/div[2]/div[3]/button[1]') #confirms the unfollow
    # UnFollowButton.click()
    # time.sleep(1)
    # ## for cancelling the confirmation
    # FollowButton.click()
    # time.sleep(1)
    # FollowButton.click()
    # time.sleep(1)
    # CancelButton = Driver.find_element(by=By.XPATH, value = '/html/body/div[2]/div[3]/button[2]') #cancels the unollow
    # CancelButton.click()
    # time.sleep(3) #Should Be following the user after this step
    ###END

    # TweetAndRetweetField = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[4]/div/div/div/a[2]/button', 1)
    # # TweetsAndRetweetsField = Driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[4]/div/div/div/a[2]/button') #MODIFIED FOR SIRIUS
    # # time.sleep(1)
    # # TweetsAndRetweetsField.click()
    #
    # MediaField = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[4]/div/div/div/a[3]/button', 1)
    # # MediaFeild = Driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[4]/div/div/div/a[3]/button') #MODIFIED FOR SIRIUS
    # # time.sleep(1)
    # # MediaFeild.click()
    #
    # LikesField = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[4]/div/div/div/a[4]/button', 1)
    # # LikesField = Driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[4]/div/div/div/a[4]/button')  #MODIFIED FOR SIRIUS
    # # time.sleep(1)
    # # LikesField.click()
    # # time.sleep(1)
    #
    # TweetsField = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[4]/div/div/div/a[1]/button', 1)
    # # TweetsFields = Driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[4]/div/div/div/a[1]/button') #MODIFIED FOR SIRIUS
    # # time.sleep(1)
    # # TweetsFields.click()
    # # time.sleep(1)
    # # ####
    #
    # #Followers list
    # Followings = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[3]/div[3]/a[1]', 1)
    # # Followings = Driver.find_element(by=By.XPATH, value = '/html/body/div/div/div/div[2]/div[1]/div[3]/div[3]/a[1]/span')
    # # Followings.click()
    # # time.sleep(1)
    #
    # pyautogui.press("down")
    # time.sleep(2)
    # pyautogui.press("up")
    # time.sleep(2)
    # # Backbutton = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[1]/div/a', 2)
    # # Backbutton = Driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[2]/div[1]/div[1]/div/a')
    # # time.sleep(2)
    #
    # FollowerTab = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div/div/a[1]/button', 2)
    # # FollowersTab = Driver.find_element(by=By.XPATH,value='/html/body/div/div/div/div[2]/div[1]/div[2]/div/div/a[1]/button')
    # # time.sleep(2)
    # # FollowersTab.click()
    # # time.sleep(3)
    #
    # FollowingTab = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div/div/a[2]/button', 2)
    # # FollowingTab = Driver.find_element(by=By.XPATH,value='/html/body/div/div/div/div[2]/div[1]/div[2]/div/div/a[2]/button')
    # # FollowingTab.click()
    # # time.sleep(3)
    #
    # BackButton = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[1]/div/a', 2)
    # # Backbutton.click()
    # # Driver.get('http://mysirius.me/profile') #doesnt want to click on back button even though it is implemented correctly by FT
    # # time.sleep(3)
    #
    # Followers = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[3]/div[3]/a[2]/span', 2)
    # # Followers = Driver.find_element(by=By.XPATH,value = '/html/body/div/div/div/div[2]/div[1]/div[3]/div[3]/a[2]/span')
    # # Followers.click()
    # # time.sleep(2)
    #
    # FollowingTab = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div/div/a[2]/button', 2)
    # # FollowingTab2 = Driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[2]/div[1]/div[2]/div/div/a[2]/button') #New Variable because
    # # FollowingTab2.click()
    # # time.sleep(2)
    #
    # FollowerTab = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div/div/a[1]/button', 2)
    # # FollowersTab2 = Driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[2]/div[1]/div[2]/div/div/a[1]/button')
    # # time.sleep(2)
    # # FollowersTab2.click()
    # # time.sleep(2)
    #
    # BackButton = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[1]/div/a', 1)
    # # Backbutton.click()
    # # Driver.get('http://mysirius.me/profile')  # doesnt want to click on back button even though it is implemented correctly by FT
    # time.sleep(4)
    #
    # #test unfollow and follow
    # Followers = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[3]/div[3]/a[2]/span', 2)
    #
    # FollowButton = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[2]/button', 2)
    #
    # FollowingTab = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div/div/a[2]/button', 2)
    #
    # FollowerTab = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div/div/a[1]/button', 2)
    #
    # UnfollowButton = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[2]/button', 2)
    #
    # Cancel = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/button[2]', 2)
    #
    # UnfollowButton = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[2]/button', 2)
    #
    # UnfollowConfirmation = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/button[1]', 2)
    #
    # FollowingTab = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div/div/a[2]/button', 2)
    #
    # FollowerTab = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div/div/a[1]/button', 2)
    #
    # BackButton = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[1]/div/a', 1)
    #
    # ##Notification Bell
    # #NotificationBell = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button[2]', 1)
    #
    # # NotificationBell = Driver.find_element(by=By.XPATH,value = '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button[2]')
    # # NotificationBell.click()
    # # time.sleep(2)
    # #####
    #
    # # MoreSettingsButton = ClickFnHttp(Driver, '//*[@id="root"]/div/div/div[2]/div[1]/div[2]/div[3]/div/button[1]', 2)
    # # MoreSettingsButton = Driver.find_element(by=By.XPATH,value = '//*[@id="root"]/div/div/div[2]/div[1]/div[2]/div[3]/div/button[1]')
    # # MoreSettingsButton.click()
    # # time.sleep(2)

    EditProfile = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button', 2)
    pyautogui.press("down")
    time.sleep(2)
    pyautogui.press("up")
    time.sleep(2)

    try:
        achain = ActionChains(Driver)
        profilePhoto = Driver.find_element(by=By.XPATH,value='/html/body/div[2]/div[3]/div[2]/div[2]/div')
        achain.context_click(profilePhoto).perform()
        time.sleep(5)
        Edit = Driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[3]/ul/li[1]/input')
        # Edit.send_keys('D:/GAM3A/3-Junior/JUNIOR-2/Software/TESTING GITGUB/Testing-Sirius/Image/test.jpg')
        Edit.send_keys('../Image/test.jpg')
        Save = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[1]/button', 2)
        Driver.get('http://mysirius.me/user7')
        time.sleep(2)
    except:
        print("Element not found.")

    # Driver.get('http://mysirius.me/profile')
    # time.sleep(2)

    # ProfileNames(Driver, Mode)

    # ProfileBio(Driver, Mode)

    # ProfileCountry(Driver, Mode)

    # ProfileCity(Driver, Mode)

    # ##Make big window

    # follow = ClickFnHttp(Driver, '/html/body/div/div/div/div[3]/div[3]/div/div[1]/div/button', 2)
    #
    # follow = ClickFnHttp(Driver, '/html/body/div/div/div/div[3]/div[3]/div/div[2]/div/button', 2)
    #
    # follow = ClickFnHttp(Driver, '/html/body/div/div/div/div[3]/div[3]/div/div[3]/div/button', 2)
    #
    # follow = ClickFnHttp(Driver, '/html/body/div/div/div/div[3]/div[3]/div/div[1]/div/button', 2)
    #
    # unfollow = ClickFnHttp(Driver, '/html/body/div/div/div/div[3]/div[3]/div/div[1]/div/button', 2)
    #
    # Cancel = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/button[2]', 2)
    #
    # Confirm = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/button[1]', 2)
    #
    # #check following
    # Followings = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[3]/div[3]/a[1]', 2)
    #
    # BackButton = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[1]/div/a', 1)
    #
    # # tweet from profile
    # ProfileTweet(Driver)

def ProfileNames(Driver, Mode = 1):
    if Mode==0:
        F = open('../TestCases/Names.txt', 'r')
        names = [Name.rstrip('\n') for Name in F.readlines()]
        F.close()
        time.sleep(2)

        for name in names:
            i = 2
            EditProfile = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button', 2)
            while(i>=0):
                pyautogui.press("down")
                i-=1

            # NameField = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[1]/input', 1)
            try:
                NameField = Driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div[3]/div[1]/input').clear()
                NameField = SendKeysFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[1]/input', name, 2)

                Save = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[1]/button', 2)
            except:
                print("Element not found.")
            Driver.get('http://mysirius.me/user7')
            time.sleep(1)
    else:
        F = open('../TestCases/Names.txt', 'r')
        Name = (F.readline()).rstrip('\n')
        F.close()
        time.sleep(2)

        i = 2
        EditProfile = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button', 2)
        while (i >= 0):
            pyautogui.press("down")
            i -= 1
        try:
            # NameField = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[1]/input', 1)
            NameField = Driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div[3]/div[1]/input').clear()
            NameField = SendKeysFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[1]/input', Name, 2)

            Save = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[1]/button', 2)
        except:
            print("Element not found.")

        Driver.get('http://mysirius.me/user7')
        time.sleep(1)

def ProfileBio(Driver, Mode = 1):
    if Mode==0:
        F = open('../TestCases/Bios.txt', 'r')
        Bios = [Bio.rstrip('\n') for Bio in F.readlines()]
        F.close()
        time.sleep(2)

        for Bio in Bios:
            i = 3
            EditProfile = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button', 2)
            while(i>=0):
                pyautogui.press("down")
                i-=1
            time.sleep(1)
            try:
                # NameField = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[1]/input', 1)
                BioField = Driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div[3]/div[2]/input').clear()
                BioField = SendKeysFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[2]/input', Bio, 2)

                Save = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[1]/button', 2)
            except:
                print("Element not found.")

            Driver.get('http://mysirius.me/user7')
            time.sleep(1)
    else:
        F = open('../TestCases/Bios.txt', 'r')
        Bio = (F.readline()).rstrip('\n')
        F.close()
        time.sleep(2)
        i=3
        EditProfile = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button', 2)

        EditProfile = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button', 2)
        while (i >= 0):
            pyautogui.press("down")
            i -= 1
        time.sleep(2)
        # NameField = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[1]/input', 1)
        try:
            BioField = Driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div[3]/div[2]/input').clear()
            BioField = SendKeysFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[2]/input', Bio, 2)

            Save = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[1]/button', 2)
        except:
            print("Element not found.")

        Driver.get('http://mysirius.me/user7')
        time.sleep(2)

def ProfileCountry(Driver, Mode = 1):
    if Mode==0:
        F = open('../TestCases/Country.txt', 'r')
        Countries = [Country.rstrip('\n') for Country in F.readlines()]
        F.close()
        time.sleep(2)

        for Country in Countries:
            i = 3
            EditProfile = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button', 2)
            while(i>=0):
                pyautogui.press("down")
                i-=1
            time.sleep(1)
            try:
                CountryField = Driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div[3]/div[3]/input').clear()
                CountryField = SendKeysFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[3]/input', Country, 2)
                time.sleep(2)
                Save = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[1]/button', 2)
            except:
                print("Element not found.")

            Driver.get('http://mysirius.me/user7')
            time.sleep(2)
    else:
        F = open('../TestCases/Country.txt', 'r')
        Country = (F.readline()).rstrip('\n')
        F.close()
        time.sleep(2)
        i = 3
        EditProfile = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button', 2)
        while (i >= 0):
            pyautogui.press("down")
            i -= 1
        time.sleep(1)
        try:
            CountryField = Driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div[3]/div[3]/input').clear()
            CountryField = SendKeysFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[3]/input', Country, 2)

            Save = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[1]/button', 2)
        except:
            print("Element not found.")

        Driver.get('http://mysirius.me/user7')
        time.sleep(2)

def ProfileCity(Driver, Mode = 1):
    if Mode==0:
        F = open('../TestCases/City.txt', 'r')
        Cities = [City.rstrip('\n') for City in F.readlines()]
        F.close()
        time.sleep(2)

        for City in Cities:
            i = 4
            EditProfile = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button', 2)
            while(i>=0):
                pyautogui.press("down")
                i-=1
            time.sleep(1)
            try:
                CityField = Driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div[3]/div[4]/input').clear()
                CityField = SendKeysFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[4]/input', City, 2)
                Save = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[1]/button', 2)
            except:
                print("Element not found.")

            Driver.get('http://mysirius.me/user7')
            time.sleep(2)
    else:
        F = open('../TestCases/City.txt', 'r')
        City = (F.readline()).rstrip('\n')
        F.close()
        time.sleep(2)

        i = 4
        EditProfile = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[3]/div/button', 2)
        while (i >= 0):
            pyautogui.press("down")
            i -= 1
        time.sleep(1)
        try:
            CityField = Driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div[3]/div[4]/input').clear()
            CityField = SendKeysFnHttp(Driver, '/html/body/div[2]/div[3]/div[3]/div[4]/input', City, 2)
            Save = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div[1]/button', 2)
        except:
            print("Element not found.")

        Driver.get('http://mysirius.me/user7')
        time.sleep(2)

def ProfileTweet(Driver, Mode = 1):
    i = 1
    if Mode == 0:
        F = open('../TestCases/TweetTestCases.txt', 'r')
        Quotes = [tweet.rstrip('\n') for tweet in F.readlines()]
        F.close()
        time.sleep(2)
        for quote in Quotes:
            Tweet = ClickFnHttp(Driver, '/html/body/div/div/div/div[1]/div[1]/div/button', 2)
            TweetField = SendKeysFnHttp(Driver, '/html/body/div[2]/div[3]/div/div/div[3]/div[1]/div/textarea[1]', quote, 2)
            if len(quote) > 0 and len(quote) <= 280:
                TweetButton = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div/div/div[3]/div[2]/div[3]/div/button', 2)
                print("Tweeted: ", i)
                i += 1
                time.sleep(2)
                Close = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div/div/div[1]', 2)
            else:
                print("cant tweet empty tweet nor larger than 281 char!! im the quote = ", quote)
            time.sleep(2)
        Driver.get('http://mysirius.me/user7')
        time.sleep(2)
        TweetAndRetweetField = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[4]/div/div/div/a[2]/button', 1)
        TweetsField = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[4]/div/div/div/a[1]/button', 1)
        Driver.get('http://mysirius.me/home')
        time.sleep(2)
        Driver.get('http://mysirius.me/user7')
        time.sleep(2)
    else:
        F = open('../TestCases/TweetTestCases.txt', 'r')
        Quotes = (F.readline()).rstrip('\n')
        F.close()
        time.sleep(2)

    Tweet = ClickFnHttp(Driver, '/html/body/div/div/div/div[1]/div[1]/div/button', 2)
    TweetField = SendKeysFnHttp(Driver, '/html/body/div[2]/div[3]/div/div/div[3]/div[1]/div/textarea[1]', Quotes, 2)
    if len(Quotes) > 0 and len(Quotes) <= 280:
        TweetButton = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div/div/div[3]/div[2]/div[3]/div/button', 2)
        print("Tweeted: ", i)
        i += 1
        time.sleep(2)
        Close = ClickFnHttp(Driver, '/html/body/div[2]/div[3]/div/div/div[1]', 2)
    else:
        print("cant tweet empty tweet nor larger than 281 char!! im the quote = ", Quotes)
    time.sleep(1)
    Driver.get('http://mysirius.me/user7')
    time.sleep(2)
    TweetAndRetweetField = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[4]/div/div/div/a[2]/button', 1)
    TweetsField = ClickFnHttp(Driver, '/html/body/div/div/div/div[2]/div[1]/div[4]/div/div/div/a[1]/button', 1)
    Driver.get('http://mysirius.me/home')
    time.sleep(2)
    Driver.get('http://mysirius.me/user7')
    time.sleep(2)