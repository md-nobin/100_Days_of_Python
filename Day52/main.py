from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os
load_dotenv()

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")

# Login into account
time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label').send_keys(os.getenv('USERID'))
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label').send_keys(os.getenv('PASSWORD'))
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()

# Get the target account
time.sleep(20)
driver.get(f"https://www.instagram.com/{os.getenv('SIMILAR_ACCOUNT')}")

# Follow account
time.sleep(10)
follower_accounts = driver.find_element(By.CSS_SELECTOR, 'div._aano')

while True:
    pass

# account locked for repeatedly login , wait for a day, if account doesn't unlocked then use another account.
