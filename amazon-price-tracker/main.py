import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/dp/B08QDVFV2F/ref=syn_sd_onsite_desktop_0?ie=UTF8&psc=1&pd_rd_plhdr=t"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
try:
    price = soup.find(name="span", class_="a-offscreen").get_text()

except AttributeError:
    try:
        price = soup.find(name="span", id="price",
                        class_="a-size-medium a-color-price header-price a-text-normal").get_text()
    except AttributeError:
        price = soup.find(name="span", class_="a-size-medium a-color-price").get_text().strip()
        
#round price to 0 decimal place
price = float(price.split("$")[1])
print(price)
import smtplib

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200.00
YOUR_EMAIL = ""
YOUR_PASSWORD = ""

if price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )