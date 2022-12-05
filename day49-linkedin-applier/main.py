import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

load_dotenv(override=True)
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3312205122&f_AL=true&f_JT=I&geoId=102454443&keywords=full%20stack&location=Singapore&refresh=true&sortBy=R'

chrome_driver_path = r'C:\Users\ChrisLye\Documents\DevDependencies\chromedriver_win32\chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)
time.sleep(5)
# click on sign in
sign_in_button = driver.find_element(By.LINK_TEXT, ("Sign in"))
sign_in_button.click()
# key in user and pass
username_input = driver.find_element(By.ID, "username")
username_input.send_keys(username)
password_input = driver.find_element(By.ID, "password")
password_input.send_keys(password)
# click on sign in
sign_in_button = driver.find_element(By.XPATH,  "//*[contains(@aria-label, 'Sign in')]")
sign_in_button.click()
# save the job
save_button = driver.find_element(By.CLASS_NAME, 'jobs-save-button')
save_button.click()

time.sleep(100)