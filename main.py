from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from flight_data import find_cheapest_flights
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
today = datetime.now() + timedelta(days=1)
return_date = datetime.now() + timedelta(days=(6*30))
ORIGIN_AIRPORT = 'LON'

sheet_data = data_manager.get_data()['prices']

for record in sheet_data:
    codes = record['iataCode']
    data = flight_search.search_flight(ORIGIN_AIRPORT, codes, today, return_date)
    flight = find_cheapest_flights(data)
    print(f"Getting flights for {record['city']}")
    print(f"Paris {flight.price}")
    if flight.price == 'N/A':
        continue
    if float(flight.price) < record['lowestPrice']:
        # If cheaper flight is available send sms to the phone
        notification_manager.send_sms(
            message_body=f"Low price alert! Only £{flight.price} to fly "
                         f"from {flight.origin_airport} to {flight.destination_airport}, "
                         f"on {flight.out_date} until {flight.return_date}."
        )






