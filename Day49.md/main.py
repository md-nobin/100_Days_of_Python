from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test ():

    driver = webdriver.Chrome()
    driver.get(
            "https://www.linkedin.com/jobs/search/?currentJobId=3734699895&f_AL=true&geoId=106215326&keywords=Python%20"
            "developer&location=Bangladesh&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")
    sign_in_btn = driver.find_element(By.LINK_TEXT, "Sign in")
    sign_in_btn.click()
    time.sleep(5)

    gmail = driver.find_element(By.ID, "username")
    gmail.send_keys("farhanahmednobin@gmail.com")

    password = driver.find_element(By.ID, "password")
    password.send_keys("RMHSSIP9670")
    password.send_keys(Keys.ENTER)

    time.sleep(10)
    job_apply_btn = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
    job_apply_btn.click()

    time.sleep(10)
    number = driver.find_element(By.CLASS_NAME, "artdeco-text-input--input")
    number.click()
    number.send_keys("+8801880251409")

    next_btn = driver.find_element(By.CSS_SELECTOR, "footer button")
    next_btn.click()
    next_btn.click()

    input_box = driver.find_elements(By.CSS_SELECTOR, "artdeco-text-input--input")
    for inputs in input_box:
        inputs.click()
        inputs.send_keys("3")

    while True:
        pass


test()
