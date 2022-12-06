import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import os
from dotenv import load_dotenv
from selenium.webdriver.common.action_chains import ActionChains
load_dotenv(override=True)

PROMISED_DOWN = 150
PROMISED_UP = 10
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
CHROME_DRIVER_PATH = r'C:\Users\ChrisLye\Documents\DevDependencies\chromedriver_win32\chromedriver'


class InternetSpeedTwitterBot:
    def __init__(self, chrome_driver_path) -> None:
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.up = 0
        self.down = 0
        
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        time.sleep(90)
        
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        ## insert selenium code for twitter here
        print(self.up, self.down)
        
    
bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()