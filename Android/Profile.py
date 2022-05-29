from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from MobUtilities import *
def Profile(Driver):
    NavBar = ClickFnHttp(Driver, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]', 2)
    Profile = ClickFnHttp(Driver,'//android.view.View[@content-desc="Profile"]')

    Tweets = ClickFnHttp(Driver, '//android.view.View[@content-desc="Tweets Tab 1 of 4"]')
    TweetsandReplies = ClickFnHttp(Driver, '//android.view.View[@content-desc="Tweets Tab 2 of 4"]')
    Media = ClickFnHttp(Driver, '//android.view.View[@content-desc="Tweets Tab 3 of 4"]')
    Likes = ClickFnHttp(Driver, '//android.view.View[@content-desc="Tweets Tab 4 of 4"]')

    EditProfile = ClickFnHttp(Driver, '//android.widget.Button[@content-desc="Edit Profile"]')

    Name = SendKeysFnHttp(Driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]',"ProHackarz", 2)
    msg = "hiuwadhiwuadosojaowjdihiuwadhiwuadosojaowjdihiuwadhiwuadosojaowjdihiuwadhiwuadosojaowjdihiuwadhiwuadosojaowjdihiuwadhiwuadosojaowjdihiuwadhiwuadosojaowjdihiuwadhiwuadosojaowjdihiuwadhiwuadosojaowjdihiuwadhiwuadosojaowjdihiuwadhiwuadosojaowjdihiuwadhiwuadosojaowjdihiuwadhiwuadosojaowjdihiuwadhiwuadosojaowjdihiuwadhiwuadosojaowjdihiuwadhiwuadosojaowjdihiuwadhiwuadosojaowjdihiuwadhiwuadosojaowjdihiuwadhiwuadosojaowjdihiuwadhiwuadosojaowjdihiuwadhiwuadosojaowjdihiuwadhiwuadosojaowjdihiuwadhiwuadosojaowjdi"
    Bio = SendKeysFnHttp(Driver,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]',msg, 2)
    Save = ClickFnHttp(Driver, '//android.widget.Button[@content-desc="Save"]')