import requests
from twilio.rest import Client

api_key = ""
endpoint= ""
account_sid = ""
auth_token = ""

parameters = {
    "lat": "",
    "lon": "",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(endpoint , params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["weather"][0]["main"]
will_rain = False
print(weather_slice)

if weather_slice == "Clouds":
    will_rain = True
    
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="It's going to rain today. Remember to bring an umbrella ☔",
                        from_='+1 385 832 7824',
                        to='+64220521226'
                    )
                         
else:
    print("No need for an umbrella.")
    

#install twilio using pip install twilio




