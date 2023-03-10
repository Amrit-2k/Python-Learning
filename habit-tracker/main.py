import requests
import datetime
USERNAME = ""
TOKEN = ""

pixela_endpoint = "https://pixe.la/v1/users"
users_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


graph_endpoint = f"{pixela_endpoint}/amaan/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"
#today = datetime.now()

pixel_data = {
    "date": "2",
    "quantity": input("How many hours did you code today? "),
}

response = requests.get(url = pixel_creation_endpoint, json = pixel_data, headers = headers)
print(response.text)
