from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import run
from run import InternetSpeedTwitterBot

PROMISED_DOWN = run.PROMISED_DOWN
PROMISED_UP = run.PROMISED_UP
TWITTER_EMAIL = run.TWITTER_EMAIL
TWITTER_PASSWORD = run.TWITTER_PASSWORD


#get self.down and self.up from run.py
bot = InternetSpeedTwitterBot()


down = int(bot.down.split('.')[0])


up = int(bot.up.split('.')[0])


#compare self.down and self.up to PROMISED_DOWN and PROMISED_UP
if down < PROMISED_DOWN or up < PROMISED_UP:
    print("Internet speed is too slow")
    bot.tweet_at_provider
    
else:
    print("Internet speed is good")

