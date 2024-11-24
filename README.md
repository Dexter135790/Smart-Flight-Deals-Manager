# Smart Flight Deals Manager

## Overview 
Flight Deal Finder is a Python-based application that helps users find and track the cheapest flight deals. It integrates with Google Sheets to manage city data and Amadeus APIs to fetch flight details. When a cheaper flight is available, the system sends SMS notifications using Twilio.

## Features
- Fetch city data and update it dynamically using Google Sheets.
- Retrieve IATA codes for cities using Amadeus API.
- Search for flights between origin and destination airports.
- Identify the cheapest flight available and compare prices.
- Notify users via SMS about deals using Twilio.

## Technologies Used 
- Programming Language: Python
- APIs:
   * Amadeus API for flight information.
   * Twilio API for SMS notifications.
   * Sheety for Google Sheets integration.
- Libraries: Requests, Python dotenv, Twilio
- Deployment: Environment variable management with dotenv.

## Prerequisites
* Python 3.9 or above.
* API keys:
    * Amadeus API
    * Sheety API
    * Twilio API
* A Google Sheet with the following columns:
  * city: Destination city names.
  * iataCode: (IATA airport codes - can be blank initially).
  * lowestPrice: The current known lowest price for that route.
 
Setup Instructions
1. Clone this repository:
   ```
   git clone https://github.com/Dexter135790/Smart-Flight-Deals-Manager.git
   cd Smart-Flight-Deals-Manager
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up environment variables in a `.env` file:
   ```
   AMADEUS_API_KEY=your_amadeus_api_key
   AMADEUS_SECRET_KEY=your_amadeus_secret_key
   AMADEUS_TOKEN_GRANTING_ENDPOINT=https://test.api.amadeus.com/v1/security/oauth2/token
   SHEETY_ENDPOINT=your_sheety_endpoint
   AUTHENTICATION_SHEETY=your_sheety_auth
   TWILLIO_ACCOUNT_SID=your_twilio_account_sid
   TWILLIO_AUTH_TOKEN=your_twilio_auth_token
   TWILLIO_VIRTUAL_NUMBER=your_twilio_virtual_number
   TWILLIO_RECEPENT_NUMBER=your_phone_number
   ```
4. Run the application:
```
python main.py
```

## Project Structure 

```
.
├── data_manager.py         # Handles interactions with Google Sheets
├── flight_data.py          # Contains the FlightData class
├── flight_search.py        # Handles flight searches and API requests
├── notification_manager.py # Sends SMS notifications
├── main.py                 # Entry point of the application
├── .env                    # Environment variables (not included in repo)
├── requirements.txt        # Dependencies
└── README.md               # Project documentation

```

## Future Enhancements 
- Add user authentication to personalize notifications.
- Expand notifications to include email support.
- Add a graphical user interface (GUI) for better usability.
- Enable support for multiple currencies.




