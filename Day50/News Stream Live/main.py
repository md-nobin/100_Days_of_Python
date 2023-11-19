from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)
driver.set_window_size(1300, 1100)

time.sleep(5)
driver.get(url="http://10.16.100.244/index.php?category=12")

time.sleep(5)
driver.find_element(By.CLASS_NAME, "close").click()

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="navbar"]/ul/li[1]/a').click()

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="Bangla"]/div/div[7]/div/div[2]').click()

time.sleep(2)
full_screen = driver.find_element(By.XPATH, '//*[@id="tvplayer"]')

action = ActionChains(driver)
action.double_click(full_screen).perform()

while True:
    pass
