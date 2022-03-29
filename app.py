from decouple import config
from turtle import down, up
from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class InternetSpeedTwitterBot:

    def __init__(self,driver):
        self.driver = driver
        self.down = down,
        self.up = up
    
    def open_speed_test(self):
        delay = 30
        try:
            go_speed = WebDriverWait(self.driver,delay). \
                until(EC.presence_of_element_located((By.XPATH,
            "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]")))
            go_speed.click()
        except:
            print("Fallo en click de speed")
    def get_down_speed(self):
        delay_down = 20
        self.down = WebDriverWait(driver,delay_down). \
                until(EC.presence_of_element_located((By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span') \
            )).text
        return down
    def get_up_speed(self):
        delay_up = 20
        self.up = WebDriverWait(driver,delay_up). \
        until(EC.presence_of_element_located((By.XPATH,
        '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span') \
        )).text
        
    # def tweet_at_provider(self):



chrome_driver_path = config('CHROME_DRIVER_PATH')
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=chrome_driver_path,chrome_options=options)

twitter_bot = InternetSpeedTwitterBot(driver)
driver.get("https://www.speedtest.net/")
sleep(20)
twitter_bot.open_speed_test()
sleep(60)
twitter_bot.get_down_speed()
twitter_bot.get_up_speed()

print(twitter_bot.down,twitter_bot.up)








