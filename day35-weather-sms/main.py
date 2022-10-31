import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
PHONE_NUMBER  = os.getenv("PHONE_NUMBER")
API_KEY = os.getenv('API_KEY')
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat":1.352083,
    "lon":103.819839,
    "appid":API_KEY,
    "exclude": "current,minutely,daily",
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

rain = False
for hour_data in weather_slice:
    condition_code= hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        rain = True
        
if rain:
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    print("Rain message sent")
    message = client.messages \
                .create(
                     body="It is going to rain today, my dudes",
                     from_=TWILIO_NUMBER,
                     to=PHONE_NUMBER
                 )

    print(message.sid)