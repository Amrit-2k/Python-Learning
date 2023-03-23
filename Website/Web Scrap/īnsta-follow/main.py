from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException

SIMILAR_ACCOUNT = "9gag"
USERNAME = "python.bot123"
PASSWORD = "YM%'w<EW2C/?=^k"

class InstaFollower:
    def __init__(self):
        options = Options()
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("https://www.instagram.com/")
        sleep(2)
    
    def login(self, username, password):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        sleep(5)
    
    def find_followers(self):
        
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        sleep(5)
        followers = self.driver.find_element(By.XPATH,"//a[contains(.,'followers')]")
        followers.click()
        sleep(5)
        modal = self.driver.find_element(By.CLASS_NAME,'_ac78')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)
    
    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR,"li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

       
        

        
        
bot = InstaFollower()
bot.login(USERNAME, PASSWORD)
bot.find_followers()
bot.follow()



        


