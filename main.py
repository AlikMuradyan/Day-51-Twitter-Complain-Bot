import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PROMISED_DOWN = 10
PROMISED_UP = 5
MY_PASSWORD = os.environ.get("MY_PASSWORD")
CHROME_DRIVER_PATH = "C:\chromedriver_win32\chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
        self.up = 0
        self.down = 0

    def get_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)

        start_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        start_button.click()
        time.sleep(45)
        self.down = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(3)

        # email = self.driver.find_element(By.CSS_SELECTOR, "input[name='text']")
        # email.send_keys(MY_EMAIL)
        # time.sleep(3)

        # next_button = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Next')]")
        # next_button.click()
        # time.sleep(5)

        user_name = self.driver.find_element(By.CSS_SELECTOR, "input[name='text']")
        user_name.send_keys("JohnnyLock777")
        time.sleep(1)

        next_button = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Next')]")
        next_button.click()
        time.sleep(3)

        password = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password.send_keys(MY_PASSWORD)
        time.sleep(1)

        login_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        login_button.click()
        time.sleep(3)

        tweet_compose = self.driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Tweet text')]")
        tweet = f"Hey ByFly, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(2)
        add_tweet = self.driver.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]')
        add_tweet.click()
        time.sleep(300)


bot = InternetSpeedTwitterBot()
bot.get_speed()
bot.tweet_at_provider()
