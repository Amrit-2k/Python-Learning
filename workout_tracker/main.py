
import requests
from datetime import datetime



GENDER = "Male"
WEIGHT_KG = 75
HEIGHT_CM = 175
AGE = 23

APP_ID = "fe996a15"
API_ID = "1ac1ed2d1fae2a74ac2115022a4f6320"

parameter = {
    "query": input("Which exercise you did? "),
    "gender" : GENDER,
    "weight_kg" : WEIGHT_KG,
    "height_cm" : HEIGHT_CM,
    "age" : AGE,

}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_ID,
}

end_point = {
    "url": "https://trackapi.nutritionix.com/v2/natural/exercise",
}

response = requests.post(url = end_point["url"], json = parameter, headers = headers)
result = response.json()


#sheety+

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
sheet_url = "https://api.sheety.co/be64346ee3d1115d4ff84148f53ae7c0/myWorkouts/workouts"

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_url, json=sheet_inputs)
#Basic Authentication
sheet_response = requests.post(
  sheet_url, 
  json=sheet_inputs, 
  auth=(
      "amrit", 
      "asdsamd123",
  )
)

