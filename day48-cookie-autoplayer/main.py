import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = r'C:\Users\ChrisLye\Documents\DevDependencies\chromedriver_win32\chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, 'cookie')

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]


timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes



while True:
    cookie.click()
    
    if time.time() > five_min:
            cookie_per_s = driver.find_element(By.ID, "cps").text
            print(cookie_per_s)
            break
    
    if time.time() > timeout:
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)
        mine_price    = int(driver.find_element(By.XPATH, '//*[@id="buyMine"]/b').text.split("-")[1].strip().replace(",", ""))
        factory_price = int(driver.find_element(By.XPATH, '//*[@id="buyFactory"]/b').text.split("-")[1].strip().replace(",", ""))
        grandma_price = int(driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b').text.split("-")[1].strip().replace(",", ""))
        cursor_price  = int(driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b').text.split("-")[1].strip().replace(",", ""))
        if cookie_count >= mine_price:
            driver.find_element(By.XPATH, '//*[@id="buyMine"]').click() # click on mine
        elif cookie_count >= factory_price:   
            driver.find_element(By.XPATH, '//*[@id="buyFactory"]').click() # click on mine
        elif cookie_count >= grandma_price:   
            driver.find_element(By.XPATH, '//*[@id="buyGrandma"]').click() # click on mine
        elif cookie_count >= cursor_price:   
            driver.find_element(By.XPATH, '//*[@id="buyCursor"]').click() # click on mine
        
            
        timeout = time.time() + 5