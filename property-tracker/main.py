from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
\

response = requests.get(
    "https://www.trademe.co.nz/a/property/residential/sale/search?search_string=Auckland"
)

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_link_elements = soup.select(".list-card-top a")                 
all_links = []

for link in all_link_elements:
    href = link["href"]
    if "https" not in href:
        all_links.append(f"https://www.trademe.co.nz{href}")
    else:
        all_links.append(href)

all_address_elements = soup.select("list-card-info address")
all_addresses = [address.getText() for address in all_address_elements]

all_price_elements = soup.select(".list-card-heading")
all_prices = []

for element in all_price_elements:
    try:
        price = element.select_one(".list-card-price")[0].contents[0]
    except IndexError:
        price = ""
        price = element.select_one("..list-card-details li")[0].contents[0]
    finally:
        all_prices.append(price)
    
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

for n in range (len(all_links)):

    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfyb7Yyonvvky4CDmqbSR6EzMOcuKFsbG6N307g04CmiXesgA/viewform?usp=sf_link")
    sleep(2)

    address = driver.find_element(By.ID,"1678275313621-4031056750-premium-listing-card-subtitle")
    address.send_keys(all_addresses[n])
