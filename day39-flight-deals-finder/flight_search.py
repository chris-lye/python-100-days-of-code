from mimetypes import init
from flight_data import FlightData

import requests


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.locations = []
    
        
    def add_location(self, location):
        self.locations.append(location)
        
    def check_location(self, location, headers):
        params = {
            'term': location,
            'location_types':'city'
        }
        response = requests.get(url=self.endpoint, params=params, headers=headers)
        print(response.json())
        return response.json()['locations'][0]['code']