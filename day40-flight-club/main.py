import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

load_dotenv()

### Ask user for info and update spreadsheet ###

SHEET_CODE  = os.getenv("SHEET_CODE")
TOKEN = os.getenv("TOKEN")
sheety_endpoint = f'https://api.sheety.co/{SHEET_CODE}/flightDeals/users'


print("Welcome to the Python Flight Club.\nWe find cheapo flights and email them to you.")
first_name = input("What is your first name?\n")
last_name =  input("What is your last name?\n")

email1 = ''
email2 = ''
while True:
    email1 = input("What is your email?\n")
    email2 = input("Enter your email again?\n")
    if email1 == email2:
        break

sheety_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

sheety_params = {
    'user': {
        'firstName': first_name,
        'lastName': last_name,
        'email': email1,
    }
}

sheety_res =  requests.post(url=sheety_endpoint, json=sheety_params, headers=sheety_headers)
print(sheety_res.text)    
print("You're in the club!")

### main loop for flight checking and emailing etc

data_manager = DataManager()
sheet_data = data_manager.get_destination_data(headers=sheety_headers)
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        
        users = data_manager.get_customer_emails(headers=sheety_headers)
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]
        
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)
        # notification_manager.send_sms(message)
         
        notification_manager.send_email(message, flight, emails)



