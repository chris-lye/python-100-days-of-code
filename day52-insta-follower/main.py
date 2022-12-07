import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import os
from dotenv import load_dotenv
from selenium.webdriver.common.action_chains import ActionChains
load_dotenv(override=True)

CHROME_DRIVER_PATH = r'C:\Users\ChrisLye\Documents\DevDependencies\chromedriver_win32\chromedriver'
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
SIMILAR_ACC = 'chefsteps'

class InstaFollower:
    def __init__(self, chrome_driver_path) -> None:
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        
    def login(self, user, passw):
        self.driver.get('https://www.instagram.com/login')
        time.sleep(5)
        username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        username.send_keys(user)
        password.send_keys(passw)
        password.send_keys(Keys.ENTER)
    
    def find_followers(self, user):
        time.sleep(5)
        self.driver.get('https://www.instagram.com/' + user)
        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
           self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", modal)
           time.sleep(2)
        
    
    def follow(self):
        # dont want to follow
        pass
    
follower_bot = InstaFollower(CHROME_DRIVER_PATH)
follower_bot.login(username, password)
follower_bot.find_followers(SIMILAR_ACC)
follower_bot.follow()