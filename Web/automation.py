from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from SignIn import SignIn
from NavBar import NavBar
from Notifications import Notifications
from Bookmarks import Bookmarks
from Profile import ProfileTest
from AdminNavBar import AdminNavBar
from AdminUserOptions import AdminUserOptions
from TweetComp import TweetComp
from TweetCompPoll import TweetCompPoll
from TweetCompSchedule import TweetCompSchedule
from InteractiveIcons import InteractiveIcons
from TweetAtweet import TweetAtweet
from InfiniteScroll import InfiniteScroll
from Utilities import *     # imports all utility functions
from SearchBar import SearchBar
from Register import Register






Driver = webdriver.Chrome(ChromeDriverManager().install()) # uses google chrome
# DriverF = webdriver.Firefox(executable_path=r'..\Gecko\geckodriver.exe') # uses firefox

# Driver = DriverF  # el line dh nb2a nsheelo ba3d ma nzabat 7war el browser, w nt2kd en el functions kolaha
                  # btsht8l b chrome 3ady. w sa3etha nsheel el DriverF asln

##########Register(Driver)  # Registers using the default testing mode
#Register(Driver, 1)  # Registers using the default testing mode
#Register(Driver, 0)  # Registers using the focused testing mode



Driver.get('http://mysirius.me/')

# time.sleep(3)
SignIn(Driver)  # Signs in using the default testing mode                       #SIGING IN READY
# SignIn(Driver, 1)  # Signs in using the default testing mode
# SignIn(Driver, 0)  # Signs in using the focused testing mode

# InfiniteScroll(Driver)

# Driver = webdriver.Firefox(executable_path=r'..\..\..\gecko\geckodriver.exe')
# Driver.get('http://34.236.108.123/adminView/dashboard')  # Goes to Admin page


# time.sleep(3)
# AdminNavBar(Driver)

# time.sleep(3)
# AdminUserOptions(Driver)


# time.sleep(3)
# time.sleep(1)
# NavBar(Driver)             # Tests the Navigation Bar                                 #READY


# time.sleep(1)
# TweetAtweet(Driver)        # Tweets some tweets                                       #READY
# TweetAtweet(Driver, 1)   # Tweets using the default testing mode
# TweetAtweet(Driver, 0)   # Tweets using the focused testing mode

# time.sleep(1)
# Notifications(Driver)

# time.sleep(1)
# Bookmarks(Driver)

# time.sleep(1)
ProfileTest(Driver, 1)         # Tests profile page

# time.sleep(3)
# TweetComp(Driver)           # Tests basic tweet components

# time.sleep(3)
# TweetCompPoll(Driver)  # Tests polls using the default testing mode
# TweetCompPoll(Driver, 1)  # Tests polls using the default testing mode
# TweetCompPoll(Driver, 0)  # Tests polls using the focused testing mode

# time.sleep(3)
# TweetCompSchedule(Driver)  # Tests the schedule

# time.sleep(1)
# InteractiveIcons(Driver)
































# SearchBar(Driver)           # Tests Search Bar
# time.sleep(3)
#
#






print("Done")
time.sleep(7)