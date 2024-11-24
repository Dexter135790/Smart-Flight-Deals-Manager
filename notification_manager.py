# This class handles the notification to the phone when cheaper flights are detected
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(os.getenv("TWILLIO_ACCOUNT_SID"), os.getenv('TWILLIO_AUTH_TOKEN'))

    def send_sms(self, message_body):
        message = self.client.messages.create(
            body=message_body,
            from_=os.getenv('TWILLIO_VIRTUAL_NUMBER'),
            to=os.getenv('TWILLIO_RECEPENT_NUMBER'),
        )
        print(message.status)

