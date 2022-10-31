from datetime import datetime
from pydoc import resolve
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Note: for free pixela accounts they reject 1 in 4 requests, even if properly formatted
# Link: https://pixe.la/@johnsnow

USERNAME = 'johnsnow'
TOKEN = os.getenv('TOKEN')
GRAPH_ID = "graph1"

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# run this only once to create the user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":GRAPH_ID,
    "name":"Running Graph",
    "unit":"km",
    "type":"float",
    "color":"shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# run this only once to set-up the graph
# https://pixe.la/v1/users/johnsnow/graphs/graph1.html
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date":datetime.now().strftime("%Y%m%d"),
    "quantity":"5.07",
    "optionaData":"Tempo Run - First Upload",
}

# send data to the graph in the endpoint
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

date_to_change = datetime.now().strftime("%Y%m%d")
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_change}"

new_pixel_data = {
    "quantity":"5.5"
}

# send a PUT request to update the data
# response = requests.put(url=update_endpoint, json=new_pixel_data,headers=headers)
# print(response.text)

date_to_delete = datetime.now().strftime("%Y%m%d")
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_delete}"

# send a DELETE request to delete the data
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)