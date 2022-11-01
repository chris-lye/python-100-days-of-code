import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.endpoint = 'https://api.sheety.co/cd6f8fec29c8ae36d0e8d3015c735b54/flightDeals/prices'
        pass
    
    def update_row(self, id, data, headers):
        response = requests.put(url=f"{self.endpoint}/{id}", json=data, headers=headers)
        print(response.text)
    
    