from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from EnterEmail import EnterEmail
from TweetAtweet import TweetAtweet
from Profile import ProfileTest
from SearchBar import SearchBar
from EnterUserName import EnterUserName
from EnterPassword import EnterPassword
from Register import Register
from NavBar import NavBar
from TweetComp import TweetComp

Driver = webdriver.Chrome(ChromeDriverManager().install()) # uses google chrome

##########Register(Driver)  # Registers using the default testing mode
#Register(Driver, 1)  # Registers using the default testing mode
#Register(Driver, 0)  # Registers using the focused testing mode



Driver.get('https://twitter.com/i/flow/login')
time.sleep(3)


EnterEmail(Driver)  # Enters the email, using the default testing mode
#EnterEmail(Driver, 1)  # Enters the email, using the default testing mode
#EnterEmail(Driver, 0)  # Enters the email, using the focused testing mode
time.sleep(3)

EnterUserName(Driver)       # Enters the username using the default testing mode
#EnterUserName(Driver, 1)  # Enters the UserName using the default testing mode
#EnterUserName(Driver, 0)  # Enters the UserName using the focused testing mode
time.sleep(3)


EnterPassword(Driver)       # Enters the password using the default testing mode
#EnterPassword(Driver, 1)  # Enters the Password using the default testing mode
#EnterPassword(Driver, 0)  # Enters the Password using the focused testing mode
time.sleep(3)

ProfileTest(Driver)        # Tests profile page
time.sleep(3)

SearchBar(Driver)           # Tests Search Bar
time.sleep(3)

NavBar(Driver)             # Tests the Navigation Bar
time.sleep(3)

TweetComp(Driver)           # Tests basic tweet components
time.sleep(3)

TweetAtweet(Driver)        # Tweets some tweets
time.sleep(5)







