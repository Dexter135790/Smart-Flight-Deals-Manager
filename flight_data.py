# This class deals with the flight information that we get from AMADEUS server

class FlightData:

    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

def find_cheapest_flights(data):
    """
    Function to find the cheapest flight from all
    :param flight data
    :return: cheapest flight
    """
    if not data or not data["data"]:
        print('No flight date')
        return FlightData("N/A","N/A","N/A","N/A","N/A")
    cheapest_flight = data["data"][0]
    price = cheapest_flight['price']['grandTotal']
    lowest_price = price

    for flight in data["data"]:
        current_flight_price = flight['price']['grandTotal']
        if current_flight_price < lowest_price:
            cheapest_flight = flight
            lowest_price = current_flight_price

    flight_price = cheapest_flight["price"]["grandTotal"]
    flight_origin_airport = cheapest_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    flight_destination_airport = cheapest_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    flight_out_date = cheapest_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    flight_return_date = cheapest_flight["itineraries"][0]["segments"][0]["arrival"]["at"].split("T")[0]

    return FlightData(flight_price, flight_origin_airport, flight_destination_airport, flight_out_date, flight_return_date)






