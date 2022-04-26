from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from SignIn import SignIn
from NavBar import NavBar
from Notifications import Notifications
from Bookmarks import Bookmarks
from Profile import ProfileTest


from TweetAtweet import TweetAtweet
from SearchBar import SearchBar
from Register import Register
from TweetComp import TweetComp

Driver = webdriver.Chrome(ChromeDriverManager().install()) # uses google chrome

##########Register(Driver)  # Registers using the default testing mode
#Register(Driver, 1)  # Registers using the default testing mode
#Register(Driver, 0)  # Registers using the focused testing mode



Driver.get('http://34.236.108.123/')

time.sleep(3)
SignIn(Driver)  # Signs in using the default testing mode
# SignIn(Driver, 1)  # Signs in using the default testing mode
# SignIn(Driver, 0)  # Signs in using the focused testing mode


time.sleep(3)
Driver.get('http://34.236.108.123/profile')
time.sleep(1)
NavBar(Driver)             # Tests the Navigation Bar




time.sleep(1)
Notifications(Driver)

time.sleep(1)
Bookmarks(Driver)

time.sleep(1)
ProfileTest(Driver)


#
#
# time.sleep(3)
# ProfileTest(Driver)        # Tests profile page
# time.sleep(3)
#
# SearchBar(Driver)           # Tests Search Bar
# time.sleep(3)
#
#
# TweetComp(Driver)           # Tests basic tweet components
# time.sleep(3)
#
# TweetAtweet(Driver)        # Tweets some tweets
# time.sleep(5)







