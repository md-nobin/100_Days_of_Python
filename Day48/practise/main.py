from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.python.org/")
# search_bar = driver.find_element(By.ID,"id-search-field")
date_time = driver.find_elements(By.CSS_SELECTOR,".event-widget time")
event_name = driver.find_elements(By.CSS_SELECTOR,".event-widget li a")
event = {}
for n in range(len(date_time)):
    event[n] = {
        "Time": date_time[n].text,
        "Name": event_name[n].text
    }
print(event)