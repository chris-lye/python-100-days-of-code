import smtplib
from flight_data import FlightData
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_VIRTUAL_NUMBER = os.getenv('TWILIO_NUMBER')
TWILIO_VERIFIED_NUMBER = os.getenv('PHONE_NUMBER')
my_email = os.getenv('MY_EMAIL')
password = os.getenv('MAILER_PASSWORD')

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
        
    def send_email(self, message, flightdata: FlightData, emails):
        o_airport = flightdata.origin_airport
        d_airport = flightdata.destination_airport
        link = f'https://www.google.co.uk/flights?hl=en#flt={o_airport}.{d_airport}.{flightdata.out_date}*{d_airport}.{o_airport}.{flightdata.return_date}'
        final_message =f"""{message}
        {link}
        """
        for email in emails:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email, 
                    to_addrs=email, 
                    msg=final_message.encode('utf-8')
                )
        
