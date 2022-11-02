from pprint import pprint
import requests
import os 
from dotenv import load_dotenv

load_dotenv()

SHEET_CODE = os.getenv('SHEET_CODE')
SHEETY_PRICES_ENDPOINT = f'https://api.sheety.co/{SHEET_CODE}/flightDeals/prices'
SHEETY_USERS_ENDPOINT = f'https://api.sheety.co/{SHEET_CODE}/flightDeals/users'


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self, headers):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        print(data)
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
            
    
    def get_customer_emails(self, headers):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(customers_endpoint, headers=headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
