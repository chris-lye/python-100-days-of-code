#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from pprint import pprint
import requests
from dotenv import load_dotenv
import os
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
import notification_manager
from twilio.rest import Client

load_dotenv()
TOKEN = os.getenv("TOKEN")
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")

TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
PHONE_NUMBER  = os.getenv("PHONE_NUMBER")

SHEET_CODE  = os.getenv("SHEET_CODE")

sheety_endpoint = f'https://api.sheety.co/{SHEET_CODE}/flightDeals/prices'

sheety_headers = {
    "Authorization": f"Basic {TOKEN}"
}
tequila_headers = {
    'apikey': TEQUILA_API_KEY
}

flight_search = FlightSearch()
data_manager  = DataManager()

response = requests.get(url=sheety_endpoint, headers=sheety_headers)
sheet_data = response.json()["prices"]
# pprint(sheet_data)

flight_data_endpoint = "https://api.tequila.kiwi.com/v2/search"
for data_row in sheet_data:
    if data_row["iataCode"] == "":
       data_row["iataCode"] = flight_search.check_location( data_row['city'], headers=tequila_headers )
       new_data = {
            "price": data_row
       }
       data_manager.update_row(data_row['id'], new_data, sheety_headers)
       
    params = {
        'fly_from':'SIN',
        'fly_to':data_row['iataCode'],
        'date_from':datetime.now().strftime("%d/%m/%Y"),
        'date_to':(datetime.now()+  timedelta(days=30*6)).strftime("%d/%m/%Y"),
        "flight_type": "round",
        "nights_in_dst_from": 7,
        "nights_in_dst_to": 28,
        'curr': 'SGD'
    }
    response = requests.get(url=flight_data_endpoint, params=params, headers=tequila_headers)
    flight_data = response.json()['data'][0]
    flight_data = FlightData(flight_data['price'], flight_data['flyFrom'], flight_data['cityFrom'], flight_data['flyTo'], 
                             flight_data['cityTo'], flight_data['route'][0]['local_departure'].split("T")[0], flight_data['route'][1]['local_departure'].split("T")[0])
    print(flight_data)

# TO DO
# account_sid = os.getenv('TWILIO_ACCOUNT_SID')
# auth_token = os.getenv('TWILIO_AUTH_TOKEN')
# client = Client(account_sid, auth_token)

# print("Twilio MSG(s) sent")
# for message in messages:
#     message = client.messages \
#                 .create(
#                     body=f"""
#                       Cheap Flight Found: 
#                     """,
#                     from_=TWILIO_NUMBER,
#                     to=PHONE_NUMBER,
#                 )
#     print(message.sid)