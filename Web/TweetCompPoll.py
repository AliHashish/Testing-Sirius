from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def TweetCompPoll(Driver, Mode = 1):
    # if Mode = 0, then we will focus on testing various test cases for polls
    # if Mode = 1, then we will test the whole process with a specific element
    # namely, the first element

    time.sleep(1)
    Driver.get('http://34.236.108.123/home')
    time.sleep(3)
    # The default is testing the whole process

    if Mode == 0:  # Mainly focuses on testing email and password combinations
        F = open('../TestCases/ChoicesTestCases.txt', 'r')
        Choices = [Choice.rstrip('\n') for Choice in F.readlines()]  # Makes a list containing all Choice test cases
        F.close()

        F = open('../TestCases/TweetTestCases.txt', 'r')
        Tweets = [Tweet.rstrip('\n') for Tweet in F.readlines()]    # Makes a list containing all tweet test cases
        F.close()


        Counter = 0
        ChoiceLimit = 26  # Choice must be smaller than 26 in length
        TweetLimit = 281  # Choice must be smaller than 281 in length
        Choice2Text = 'Previous Choice 1'

        # First Case: 2 choices
        for Tweet in Tweets:
            for Choice1Text in Choices:
                Counter +=1
                print("\nCase number: ", Counter)
                print("Tweet: ", Tweet)
                print("Choice 1: ", Choice1Text)
                print("Choice 2: ", Choice2Text)

                time.sleep(1)
                Driver.get('http://34.236.108.123/home')
                time.sleep(1)

                Poll = Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[2]/div[1]/div[2]/div[2]/input')
                time.sleep(1)
                Poll.click()
                time.sleep(1)

                Days = Select(Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[2]/div[2]/div[1]/select'))
                time.sleep(1)
                Days.select_by_index(Counter%len(Days.options))
                time.sleep(1)

                Hours = Select(Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[2]/div[2]/div[2]/select'))
                time.sleep(1)
                Hours.select_by_index(Counter%len(Hours.options))
                time.sleep(1)

                Minutes = Select(Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[2]/div[2]/div[3]/select'))
                time.sleep(1)
                Minutes.select_by_index(Counter%len(Minutes.options))
                time.sleep(1)

                TweetField = Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[1]/textarea')
                time.sleep(1)
                TweetField.send_keys(Tweet)
                if (len(Tweet) < 1 or len(Tweet) > TweetLimit):
                    continue # This choice is invalid
                time.sleep(1)

                Choice1 = Driver.find_element(by=By.XPATH, value=
                '//*[@id="mui-1"]')
                time.sleep(1)
                Choice1.send_keys(Choice1Text)
                if (len(Choice1Text) < 1 or len(Choice1Text) > ChoiceLimit):
                    continue # This choice is invalid, so skip the iteration
                time.sleep(1)

                Choice2 = Driver.find_element(by=By.XPATH, value=
                '//*[@id="mui-2"]')
                time.sleep(1)
                Choice2.send_keys(Choice2Text)
                if (len(Choice2Text) < 1 or len(Choice2Text) > ChoiceLimit):
                    Choice2Text = Choice1Text # updates the value of choice 2
                    continue # This choice is invalid, so skip the iteration
                time.sleep(1)

                Confirm = Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/input[1]')
                time.sleep(1)
                Confirm.click()
                time.sleep(1)

                Choice2Text = Choice1Text





        Choice2Text = 'Previous Choice 1'
        Choice3Text = 'Previous Choice 2'
        # Second case: 3 choices
        for Tweet in Tweets:
            for Choice1Text in Choices:
                Counter +=1
                print("\nCase number: ", Counter)
                print("Tweet: ", Tweet)
                print("Choice 1: ", Choice1Text)
                print("Choice 2: ", Choice2Text)
                print("Choice 3: ", Choice3Text)

                time.sleep(1)
                Driver.get('http://34.236.108.123/home')
                time.sleep(1)



                Poll = Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[2]/div[1]/div[2]/div[2]/input')
                time.sleep(1)
                Poll.click()
                time.sleep(1)

                Days = Select(Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[2]/div[2]/div[1]/select'))
                time.sleep(1)
                Days.select_by_index(Counter % len(Days.options))
                time.sleep(1)

                Hours = Select(Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[2]/div[2]/div[2]/select'))
                time.sleep(1)
                Hours.select_by_index(Counter % len(Hours.options))
                time.sleep(1)

                Minutes = Select(Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[2]/div[2]/div[3]/select'))
                time.sleep(1)
                Minutes.select_by_index(Counter % len(Minutes.options))
                time.sleep(1)


                TweetField = Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[1]/textarea')
                time.sleep(1)
                TweetField.send_keys(Tweet)
                if (len(Tweet) < 1 or len(Tweet) > TweetLimit):
                    continue # This choice is invalid
                time.sleep(1)

                Choice1 = Driver.find_element(by=By.XPATH, value=
                '//*[@id="mui-1"]')
                time.sleep(1)
                Choice1.send_keys(Choice1Text)
                if (len(Choice1Text) < 1 or len(Choice1Text) > ChoiceLimit):
                    continue # This choice is invalid, so skip the iteration
                time.sleep(1)

                Choice2 = Driver.find_element(by=By.XPATH, value=
                '//*[@id="mui-2"]')
                time.sleep(1)
                Choice2.send_keys(Choice2Text)
                if (len(Choice2Text) < 1 or len(Choice2Text) > ChoiceLimit):
                    Choice2Text = Choice1Text # updates the value of choice 2
                    continue # This choice is invalid, so skip the iteration
                time.sleep(1)

                AddIcon = Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/input[2]')
                time.sleep(1)
                AddIcon.click()
                time.sleep(1)

                Choice3 = Driver.find_element(by=By.XPATH, value=
                '//*[@id="mui-3"]')
                time.sleep(1)
                Choice3.send_keys(Choice3Text)
                if (len(Choice3Text) < 1 or len(Choice3Text) > ChoiceLimit):
                    Choice3Text = Choice2Text # updates the value of choice 3
                    Choice2Text = Choice1Text # updates the value of choice 2
                    continue # This choice is invalid, so skip the iteration
                time.sleep(1)


                Confirm = Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/input[1]')
                time.sleep(1)
                Confirm.click()
                time.sleep(1)


                Choice3Text = Choice2Text
                Choice2Text = Choice1Text



        Choice2Text = 'Previous Choice 1'
        Choice3Text = 'Previous Choice 2'
        Choice4Text = 'Previous Choice 3'
        # Third case: 4 choices
        for Tweet in Tweets:
            for Choice1Text in Choices:
                Counter += 1
                print("\nCase number: ", Counter)
                print("Tweet: ", Tweet)
                print("Choice 1: ", Choice1Text)
                print("Choice 2: ", Choice2Text)
                print("Choice 3: ", Choice3Text)
                print("Choice 4: ", Choice4Text)

                time.sleep(1)
                Driver.get('http://34.236.108.123/home')
                time.sleep(1)

                Poll = Driver.find_element(by=By.XPATH, value=
                    '/html/body/div/div/div/div[2]/div[1]/div[2]/div[2]/input')
                time.sleep(1)
                Poll.click()
                time.sleep(1)

                Days = Select(Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[2]/div[2]/div[1]/select'))
                time.sleep(1)
                Days.select_by_index(Counter % len(Days.options))
                time.sleep(1)

                Hours = Select(Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[2]/div[2]/div[2]/select'))
                time.sleep(1)
                Hours.select_by_index(Counter % len(Hours.options))
                time.sleep(1)

                Minutes = Select(Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[2]/div[2]/div[3]/select'))
                time.sleep(1)
                Minutes.select_by_index(Counter % len(Minutes.options))
                time.sleep(1)


                TweetField = Driver.find_element(by=By.XPATH, value=
                    '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[1]/textarea')
                time.sleep(1)
                TweetField.send_keys(Tweet)
                if (len(Tweet) < 1 or len(Tweet) > TweetLimit):
                    continue # This choice is invalid
                time.sleep(1)


                Choice1 = Driver.find_element(by=By.XPATH, value=
                    '//*[@id="mui-1"]')
                time.sleep(1)
                Choice1.send_keys(Choice1Text)
                if (len(Choice1Text) < 1 or len(Choice1Text) > ChoiceLimit):
                    continue  # This choice is invalid, so skip the iteration

                time.sleep(1)


                Choice2 = Driver.find_element(by=By.XPATH, value=
                    '//*[@id="mui-2"]')
                time.sleep(1)
                Choice2.send_keys(Choice2Text)
                if (len(Choice2Text) < 1 or len(Choice2Text) > ChoiceLimit):
                    Choice2Text = Choice1Text  # updates the value of choice 2
                    continue  # This choice is invalid, so skip the iteration

                time.sleep(1)

                AddIcon = Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/input[2]')
                time.sleep(1)
                AddIcon.click()
                time.sleep(1)

                AddIcon = Driver.find_element(by=By.XPATH, value=
                '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/input[2]')
                time.sleep(1)
                AddIcon.click()
                time.sleep(1)

                SecondChoice3 = Driver.find_element(by=By.XPATH, value=
                '//*[@id="mui-4"]')
                time.sleep(1)
                SecondChoice3.send_keys(Choice3Text)
                if (len(Choice3Text) < 1 or len(Choice3Text) > ChoiceLimit):
                    Choice3Text = Choice2Text  # updates the value of choice 3
                    Choice2Text = Choice1Text  # updates the value of choice 2
                    continue  # This choice is invalid, so skip the iteration

                time.sleep(1)

                Choice4 = Driver.find_element(by=By.XPATH, value=
                '//*[@id="mui-5"]')
                time.sleep(1)
                Choice4.send_keys(Choice4Text)
                if (len(Choice4Text) < 1 or len(Choice4Text) > ChoiceLimit):
                    Choice4Text = Choice3Text  # updates the value of choice 4
                    Choice3Text = Choice2Text  # updates the value of choice 3
                    Choice2Text = Choice1Text  # updates the value of choice 2
                    continue  # This choice is invalid, so skip the iteration
                time.sleep(1)


                Choice4Text = Choice3Text  # updates the value of choice 4
                Choice3Text = Choice2Text  # updates the value of choice 3
                Choice2Text = Choice1Text  # updates the value of choice 2





    else:  # Mainly focuses on testing the whole process
        F = open('../TestCases/ChoicesTestCases.txt', 'r')
        Choice1Text = (F.readline()).rstrip('\n')  # Choice1 now equals the first element in the file
        Choice2Text = (F.readline()).rstrip('\n')  # Choice2 now equals the second element in the file
        F.close()

        F = open('../TestCases/TweetTestCases.txt', 'r')
        Tweet = (F.readline()).rstrip('\n')  # Tweet now equals the first element in the file
        F.close()

        Poll = Driver.find_element(by=By.XPATH, value=
        '/html/body/div/div/div/div[2]/div[1]/div[2]/div[2]/input')
        time.sleep(1)
        Poll.click()
        time.sleep(1)

        TweetField = Driver.find_element(by=By.XPATH, value=
        '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[1]/textarea')
        time.sleep(1)
        TweetField.send_keys(Tweet)
        time.sleep(1)

        Choice1 = Driver.find_element(by=By.XPATH, value=
        '//*[@id="mui-1"]')
        time.sleep(1)
        Choice1.send_keys(Choice1Text)
        time.sleep(1)

        Choice2 = Driver.find_element(by=By.XPATH, value=
        '//*[@id="mui-2"]')
        time.sleep(1)
        Choice2.send_keys(Choice2Text)
        time.sleep(1)

        Days = Select(Driver.find_element(by=By.XPATH, value=
            '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[2]/div[2]/div[1]/select'))
        time.sleep(1)
        Days.select_by_index(1)
        time.sleep(1)

        Hours = Select(Driver.find_element(by=By.XPATH, value=
        '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[2]/div[2]/div[2]/select'))
        time.sleep(1)
        Hours.select_by_index(1)
        time.sleep(1)

        Minutes = Select(Driver.find_element(by=By.XPATH, value=
        '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[2]/div[2]/div[3]/select'))
        time.sleep(1)
        Minutes.select_by_index(1)
        time.sleep(1)


        Confirm = Driver.find_element(by=By.XPATH, value=
        '/html/body/div/div/div/div[2]/div[1]/div/div[3]/div/div/input[1]')
        time.sleep(1)
        Confirm.click()
        time.sleep(1)








