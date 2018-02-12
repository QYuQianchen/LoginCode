from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, time, date, timedelta
from time import sleep
import time as TM

# Replace the two following inputs with your personal information 
# Replace the link according to the class you'd register
# Replace the time with the time starts the registration
usernameStr = 'username'
passwordStr = 'ETH-password'
urlStr = 'https://schalter.asvz.ch/tn-mvc/Event/Lesson/Detail/581508'
timeStr = '21:18'               # TM.strptime(timeStr, '%H:%M')


def wait_before_start(runTime, preparation_time):
    duration = datetime.combine(date.min, runTime) - datetime.combine(date.min, datetime.today().time())
    m, s = divmod(duration.seconds, 60)
    print("Time difference is " + str(m) + " minutes and " + str(s) + " seconds")

    if runTime > datetime.today().time():
        # Only start logging-in (preparation_time) seconds before the start
        print("Code on pause, resume in " + str(duration.seconds - preparation_time) + " seconds")
        sleep(duration.seconds - preparation_time)

    print("Code resumed at " + TM.asctime())    # example format: Sat Feb 10 18:41:13 2018


def start_login(usernameInput, passwordInput, urlInput):

    browser = webdriver.Chrome()
    browser.get(urlInput)

    redirect_button = browser.find_element_by_xpath(".//*[@class='btn btn-default']")
    redirect_button.click()

    AAI_button = browser.find_elements_by_xpath("//button[@class='btn btn-warning btn-block' and @type='button']")[0]
    AAI_button.click()

    session_memory = browser.find_element_by_xpath(".//*[@id='rememberForSession']")
    session_memory.click()

    Uni_list = browser.find_element_by_xpath(".//*[@id='userIdPSelection_iddwrap']")
    Uni_list.click()

    ETH_optoin = browser.find_element_by_xpath(".//*[@class='idd_listItem idd_listItem_Nested' and @title='Universities: ETHZ - ETH Zurich']")
    ETH_optoin.click()

    username = browser.find_element_by_id('username')
    username.send_keys(usernameInput)

    password = browser.find_element_by_id('password')
    password.send_keys(passwordInput)

    Login_button = browser.find_element_by_xpath(".//*[@type='submit' and @name='_eventId_proceed']")
    Login_button.click()


# @param, timeout(in seconds) to wait for button appears when loading the page
def wait_till_activate(runTime, action_timeout):

    while runTime > datetime.today().time():
        sleep(1)
        print("Now is " + TM.asctime())
        
    try:
        print("-> here about to look for login button")
        div_element = WebDriverWait(browser, action_timeout * 2).until(EC.presence_of_element_located((By.XPATH, ".//*[@class='hidden-print']")))
        hover = ActionChains(browser).move_to_element(div_element)
        hover.perform()

        submit_button = WebDriverWait(browser, action_timeout).until(EC.presence_of_element_located((By.XPATH, "//div[@class='hidden-print']//button[@class='btn btn-primary']")))
        hover = ActionChains(browser).move_to_element(submit_button)
        hover.perform()

        submit_button.click()
    except:
        print("-> failed")
    finally:
        print("-> end")

    return action_timeout


startTime = time(*(map(int, timeStr.split(':'))))
wait_before_start(startTime, 30)
start_login(usernameStr, passwordStr, urlStr)
wait_till_activate(startTime, 60)
print("Code end at" + TM.ctime()) # format example: Sat Feb 10 18:41:13 2018