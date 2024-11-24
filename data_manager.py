# This class interacts with the google sheet data
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('AMADEUS_API_KEY')
SHEETY_ENDPOINT = os.getenv('SHEETY_ENDPOINT')
SHEETY_AUTHNTICATION = os.getenv('AUTHENTICATION_SHEETY')


header = {
    "Authorization": SHEETY_AUTHNTICATION,
}

class DataManager:
    def __init__(self):
        self.sheet_data = requests.get(url=SHEETY_ENDPOINT, headers=header).json()

    def get_data(self):
        # Function to get the data from the google sheet
        return self.sheet_data

    def update_data(self, row_id, json_data):
        # Update the data of the google sheet
        response = requests.put(url=f"{SHEETY_ENDPOINT}/{row_id}", json=json_data, headers=header)
        print(response.text)


