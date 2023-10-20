from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# user_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# user_count.click()
#
# privet_policy = driver.find_element(By.LINK_TEXT, "Privacy policy")
# privet_policy.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Bangladesh")
search.send_keys(Keys.ENTER)
driver.quit()


