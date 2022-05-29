from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from SignUp import SignUp
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
from Settings import Settings
from ForgotPassword import ForgotPassword
from Logout import Logout





Driver = webdriver.Chrome(ChromeDriverManager().install()) # uses google chrome
###### DriverF = webdriver.Firefox(executable_path=r'..\Gecko\geckodriver.exe') # uses firefox

###### Driver = DriverF  # el line dh nb2a nsheelo ba3d ma nzabat 7war el browser, w nt2kd en el functions kolaha
                  # btsht8l b chrome 3ady. w sa3etha nsheel el DriverF asln

##########Register(Driver)  # Registers using the default testing mode
######Register(Driver, 1)  # Registers using the default testing mode
######Register(Driver, 0)  # Registers using the focused testing mode


time.sleep(1)
Driver.get('http://mysirius.me/')

time.sleep(3)
SignUp(Driver)  # Signs up using the default testing mode
###### SignUp(Driver, 1)  # Signs up using the default testing mode
###### SignUp(Driver, 0)  # Signs up using the focused testing mode

time.sleep(1)
SignIn(Driver)  # Signs in using the default testing mode
###### SignIn(Driver, 1)  # Signs in using the default testing mode
###### SignIn(Driver, 0)  # Signs in using the focused testing mode
time.sleep(4)
Driver.get('http://mysirius.me/home')
time.sleep(4)
Driver.get('http://mysirius.me/home')

InfiniteScroll(Driver)

#### Driver = webdriver.Firefox(executable_path=r'..\..\..\gecko\geckodriver.exe')
#### Driver.get('http://34.236.108.123/adminView/dashboard')  # Goes to Admin page


time.sleep(1)
Driver.get('http://mysirius.me/signin')
time.sleep(1)
# Hard coded, so as not to mess up other people's accounts
EmailField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[1]', "rahmanezzat14@gmail.com")  # Writes the email in the email field
time.sleep(1)
PasswordField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[2]', "boody123")  # Writes the password in the password field
time.sleep(1)
LoginButton = ClickFnHttp(Driver, '/html/body/div/div/div/form/button[2]', 1)
# Hard coded, so as not to mess up other people's accounts

# ##### time.sleep(1)
# ##### AdminNavBar(Driver)
time.sleep(4)
Driver.get('http://mysirius.me/home')
time.sleep(4)
Driver.get('http://mysirius.me/home')

time.sleep(1)
AdminUserOptions(Driver)

time.sleep(1)
SignIn(Driver)  # Signs in using the default testing mode
time.sleep(4)
Driver.get('http://mysirius.me/home')
time.sleep(4)
Driver.get('http://mysirius.me/home')

time.sleep(1)
NavBar(Driver)             # Tests the Navigation Bar                                 #READY


time.sleep(1)
TweetAtweet(Driver)        # Tweets some tweets                                       #READY
##### TweetAtweet(Driver, 1)   # Tweets using the default testing mode
##### TweetAtweet(Driver, 0)   # Tweets using the focused testing mode

time.sleep(1)
Notifications(Driver)

time.sleep(1)
Bookmarks(Driver)

time.sleep(1)
ProfileTest(Driver, 1)         # Tests profile page

time.sleep(1)
TweetComp(Driver)           # Tests basic tweet components

##### time.sleep(3)
##### TweetCompPoll(Driver)  # Tests polls using the default testing mode
###### TweetCompPoll(Driver, 1)  # Tests polls using the default testing mode
###### TweetCompPoll(Driver, 0)  # Tests polls using the focused testing mode

##### time.sleep(3)
##### TweetCompSchedule(Driver)  # Tests the schedule

time.sleep(1)
InteractiveIcons(Driver)


##### SearchBar(Driver)           # Tests Search Bar
##### time.sleep(3)





# Hard coded part, to avoid changing settings of other users
Driver.get('http://mysirius.me/signin')  # Goes to sign in page
time.sleep(1)
# Hard coded, so as not to mess up other people's accounts
EmailField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[1]', "ultimatehacker925@yahoo.com")  # Writes the email in the email field
time.sleep(1)
PasswordField = SendKeysFnHttp(Driver, '/html/body/div/div/div/form/input[2]', "passwordsa3ba")  # Writes the password in the password field
time.sleep(1)
LoginButton = ClickFnHttp(Driver, '/html/body/div/div/div/form/button[2]', 1)
time.sleep(1)
Settings(Driver)

time.sleep(4)
Driver.get('http://mysirius.me/home')
time.sleep(4)
Driver.get('http://mysirius.me/home')

time.sleep(1)
ForgotPassword(Driver)
Logout(Driver)




print("\n\n\nDone")
time.sleep(7)