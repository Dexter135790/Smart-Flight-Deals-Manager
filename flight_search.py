# This class mainly deals with searching for appropriate flights
import os

from dotenv import load_dotenv
import requests


load_dotenv()

AMADEUS_SEARCH_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
AMADEUS_FLIGHT_OFFERS_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:

    def __init__(self):
        """
            This constructire initializes the apikey, secret and token to variables
        """
        self._api_key = os.getenv('AMADEUS_API_KEY')
        self._api_secret = os.getenv('AMADEUS_SECRET_KEY')
        self._token = self._get_new_token()

    def getCodes(self, city_name):
        """
            This function provides the IATA code using city name by requesting from amadeus endpoint
            :param city_name
            :return:IATA code
        """
        headers = {"Authorization": f"Bearer {self._token}"}
        params = {
            'keyword': city_name,
        }
        response = requests.get(url=f"{AMADEUS_SEARCH_ENDPOINT}", params=params, headers=headers)
        data = response.json()

        try:
            code = data["data"][0]["iataCode"]
        except IndexError:
            return 'N/A'
        except KeyError:
            return 'Not found'

        return code

    def  _get_new_token(self):
        """
            This function generates one time access token to interact with amadeus server
        :return:Access token
        """

        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        params = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret,
        }
        response = requests.post(url=os.getenv('AMADEUS_TOKEN_GRANTING_ENDPOINT'), data=params, headers=header)
        return response.json()['access_token']

    def search_flight(self, origin_code, city_code, from_time, to_time):
        """
            This function searches flight offers from sorce to destination location
            :param city_code, departure time, return time
        """

        headers = {"Authorization": f"Bearer {self._token}"}

        params = {
            'originLocationCode': origin_code,
            'destinationLocationCode': city_code,
            'adults': 1,
            'departureDate': from_time.strftime('%Y-%m-%d'),
            'returnDate': to_time.strftime('%Y-%m-%d'),
            'nonStop': 'true',
            'currencyCode': 'GBP',
            'max': '10',
        }

        response = requests.get(url=AMADEUS_FLIGHT_OFFERS_ENDPOINT, params=params, headers=headers)

        if response.status_code != 200:
            print("There was a mistake with flight search!!!")
            print(f"Response body {response.text}")

        return response.json()



