from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


def ProfileTest(Driver):
    #after login click on profile icon
    time.sleep(3)
    ProfileIcon = Driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]')
    time.sleep(3)
    ProfileIcon.click()
    time.sleep(3)
    TweetsAndRetweetsField = Driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/nav/div/div[2]/div/div[2]/a')
    time.sleep(3)
    TweetsAndRetweetsField.click()
    MediaFeild = Driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/nav/div/div[2]/div/div[3]/a')
    time.sleep(3)
    MediaFeild.click()
    LikesField = Driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/nav/div/div[2]/div/div[4]/a')
    time.sleep(3)
    LikesField.click()
    time.sleep(3)
    TweetsFields = Driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/nav/div/div[2]/div/div[1]/a')
    time.sleep(3)
    TweetsFields.click()
    time.sleep(3)
    EditProfileButton = Driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/a')
    time.sleep(3)
    EditProfileButton.click()
    time.sleep(3)
    CloseButton = Driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[1]/div')
    time.sleep(3)
    CloseButton.click()
    time.sleep(3)










# # Entered Profile successfully 
# #now to check on "Edit Profile"
# ## PUT CONDITION  HERE TO CHECK PATH

#EditProfileButton = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/a')
# time.sleep(3)
# EditProfileButton.click()
# time.sleep(3)

# #now we test various name combinations of the user 
# #enter small lettered name
# #enter Captial "   "
# #Enter special charater (! @ # $ % ^ * ( ) _ " : ' ? / | \)  apparently real twitter doesnt accept only $ sign else it is cool 
# #enter numbers
# #in real twitter the MAX IS 50 Characters lets enter > 50 & empty name (should give warning if empty so as it exceeds)

# #lets first start by entering the name normally
# Name = "NickName To Be Here" #withing range SHOULD CHANGE LATER FOR CHECK PASS AS AN ARRAY 
# Name2 = "NickName To Be Here2" #withing range SHOULD CHANGE LATER FOR CHECK PASS AS AN ARRAY 
# time.sleep(3)
# NameField = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/label/div/div[2]/div/input')
# time.sleep(5) 
# NameField.clear()
# time.sleep(4)
# NameField.send_keys(Name)
# time.sleep(4)

# #click save and check without clicking save what will happen 
# SaveButton = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[3]/div')
# BackButton = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div[1]/div/div/div/div/div[1]/div')
# CloseButton = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[1]/div') #iff full Screen in Original tweeter
# #saving
# time.sleep(3)
# SaveButton.click()
# time.sleep(3)
# ProfileName = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div/span[1]/span')
# Name= "lol"
# if ProfileName.text != Name:
#     raise AssertionError('Profile Name doesnot Match')
#     time.sleep(15)
# time.sleep(15)

#not saving
#time.sleep(5)
#EditProfileButton.click()
#time.sleep(6)
#NameField.clear()
#time.sleep(6)
#NameField.send_keys(Name2)
#time.sleep(6)
#CloseButton.click()
#time.sleep(6)
#DiscardButton = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]')
#time.sleep(6)
#CancelButton01 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div[2]/div[2]')
#time.sleep(6)
#DiscardButton.click()
#if ProfileName.text != Name:
#    raise AssertionError("Discard process didnt work well Please check your code")
#    time.sleep(5)
#Cancel button plus change in bio 
#time.sleep(5)
#bio = " Man im Cool"
#BioField = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[4]/label/div/div[2]/div/textarea')
#time.sleep(3)
#EditProfileButton.click()
#time.sleep(3)
#NameField.clear()
#time.sleep(3)
#NameField.send_keys(Name2)
#time.sleep(3)
#CloseButton.click()
#time.sleep(3)
#CancelButton01.click()
#time.sleep(3)
#BioField.clear()
#time.sleep(3)
#BioField.send_keys(bio)
#time.sleep(3)
#SaveButton.click()
#time.sleep(15)













