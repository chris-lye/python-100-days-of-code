from datetime import datetime
from dotenv import load_dotenv
import os

from requests import request
import requests

load_dotenv()
# for nutritionix
API_KEY = os.getenv('API_KEY')
APP_ID  = os.getenv('APP_ID')
# for sheety
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
SHEET_ENDPOINT = os.getenv('SHEET_ENDPOINT')

exercise = input("What exercise(s) did you do today?")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_params = {
 "query":exercise,
 "gender":"male",
 "weight_kg":70,
 "height_cm":170,
 "age":23
}

nutri_headers = {
    "x-app-id":APP_ID,
    'x-app-key':API_KEY,
    'x-remote-user-id': "0",
}
# get data from Nutritionix API  
exercise_response = requests.post(url=exercise_endpoint, json=exercise_params, headers=nutri_headers)
print(exercise_response.text)
data = exercise_response.json()["exercises"]
# send data to spreadsheet via sheety API
sheets_endpoint = SHEET_ENDPOINT
sheets_headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}


date = datetime.now().strftime("%m/%d/%Y")
time = datetime.now().strftime("%H:%M:%S")
for exercise in data:
    sheets_params = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise['name'].title(),
        "duration": exercise['duration_min'],
        "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(url=sheets_endpoint, json=sheets_params, headers=sheets_headers)
    print(sheet_response.text)
    
