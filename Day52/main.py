from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

SIMILAR_ACCOUNT = "coding_dev_"
USERNAME = "sagar_shahriar_nobin"
PASSWORD = "SIP9670"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        user_name = self.driver.find_element(By.XPATH, "//*[@id=\"loginForm\"]/div/div[1]/div/label")
        user_name.click()
        user_name.send_keys(USERNAME)

        time.sleep(10)
        password = self.driver.find_element(By.XPATH, "//*[@id=\"loginForm\"]/div/div[2]/div/label")
        password.click()
        password.send_keys(PASSWORD)

        time.sleep(3)
        login = self.driver.find_element(By.XPATH, "//*[@id=\"loginForm\"]/div/div[3]/button")
        login.click()

    def find_followers(self):
        time.sleep(30)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(30)
        followers = self.driver.find_element(By.LINK_TEXT, "followers")

        while True:
            pass

    def follow(self):
        pass

    # while True:
    #     pass


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
