import requests
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/be64346ee3d1115d4ff84148f53ae7c0/copyOfFlightDeals/prices"
SHEETY_USERS_API = "https://api.sheety.co/be64346ee3d1115d4ff84148f53ae7c0/copyOfFlightDeals/users"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]     
        return self.destination_data
                
   
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
    
    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_API
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
            
data= DataManager()