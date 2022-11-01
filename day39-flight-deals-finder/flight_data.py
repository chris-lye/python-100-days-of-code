from re import S
from unittest.case import doModuleCleanups


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, dac, dc, ddac, ddc, outbound, inbound) -> None:
        self.price = price
        self.departure_airport_code = dac
        self.departure_city  =   dc     
        self.destination_airport_code = ddac
        self.destination_city = ddc
        self.outbound = outbound
        self.inbound  = inbound
        
    def __str__(self) -> str:
        return f"Price: {self.price} From:{self.departure_airport_code}, {self.departure_city} | To: {self.destination_airport_code}, {self.destination_city} | Leave:{self.outbound} Back:{self.inbound}"    
    