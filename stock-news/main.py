import requests
from twilio.rest import Client

VIRTUAL_TWILIO_NUMBER = ""
VERIFIED_NUMBER = ""
TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = ""
STOCK_API = ""

NEWS_API= ""
NEWS_ENDPOINT = ""


news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API
}

news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
articles = news_response.json()["articles"]

stock_parameters= {
    "function": "TIME_SERIES_DAILY_ADJUSTED",   
    "symbol": STOCK_NAME,
    "apikey": STOCK_API
}

url = requests.get(STOCK_ENDPOINT, params=stock_parameters)
data = url.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)


if abs(diff_percent) > 1:
    three_articles = articles[:3]
    print(three_articles)
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)
    #Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    #TODO 8. - Send each article as a separate message via Twilio.
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )

