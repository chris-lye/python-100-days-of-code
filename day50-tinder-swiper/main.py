import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import os
from dotenv import load_dotenv
from selenium.webdriver.common.action_chains import ActionChains


load_dotenv(override=True)
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
URL = 'https://tinder.com/'

chrome_driver_path = r'C:\Users\ChrisLye\Documents\DevDependencies\chromedriver_win32\chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)
time.sleep(1)
# click on log in
sign_in_button = driver.find_element(By.XPATH, ('//*[@id="q-401777178"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')).click()
time.sleep(2)
# log in with facebook
log_in_button = driver.find_element(By.XPATH, ('//*[@id="q-2130158254"]/main/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]')).click()
time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
# key in user and pass
username_input = driver.find_element(By.XPATH, '//*[@id="email"]')
username_input.send_keys(username)
password_input = driver.find_element(By.XPATH, '//*[@id="pass"]')
password_input.send_keys(password)
# click on sign in
password_input.send_keys(Keys.ENTER)
time.sleep(30)
driver.switch_to.window(base_window)
#Allow location
allow_location_button = driver.find_element(By.XPATH, '//*[@id="q-2130158254"]/main/div/div/div/div[3]/button[1]')
allow_location_button.click()
time.sleep(3)
#Disallow notifications
notifications_button = driver.find_element(By.XPATH, '//*[@id="q-2130158254"]/main/div/div/div/div[3]/button[1]')
notifications_button.click()
time.sleep(3)
#Close dark mode
dark = driver.find_element(By.XPATH, '//*[@id="q-2130158254"]/main/div/div[2]/button')
dark.click()


actions = ActionChains(driver)

for n in range(100):

    #Add a 1 second delay between likes.
    time.sleep(1)

    try:
        print("called")
        # like_button = driver.find_element(By.XPATH, '//*[@id="q-401777178"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        # like_button.click()
        actions.send_keys(Keys.ARROW_RIGHT)
        actions.perform()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

    #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)
    except NoSuchElementException:
            time.sleep(2)
            
time.sleep(100)