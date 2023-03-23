#Building a twitter bot 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

PROMISED_DOWN= 400
PROMISED_UP = 400

TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""

class InternetSpeedTwitterBot:
    def __init__(self):
        options = Options()
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver = driver
        self.down = 0
        self.up = 0
        self.get_internet_speed()
        

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net')
        start = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        start.click()
        sleep(45)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        sleep(2)

        email = self.driver.find_element(By.XPATH, '//input[@autocomplete = "username"]')       
        email.send_keys(TWITTER_EMAIL)    
        email.send_keys(Keys.ENTER)
        sleep(2)       

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(5)

        click_tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/'
                                                         'div[1]/div[3]/a/div/span/div/div/span/span')
        click_tweet.click()        
        sleep(3)
        
        enter_tweet_message = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        enter_tweet_message.click()
        sleep(2)
        
        # include your download and upload speed using self.down and self.up
        enter_tweet_message.send_keys(f'Hey, why is my internet speed {self.down}down/{self.up}up when i pay for'
                                      f'{PROMISED_DOWN}down/{PROMISED_UP}up ?')
        # lastly post your tweet
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div'
                                           '[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]'
                                           '/div/span/span').click()
        sleep(2)
        

