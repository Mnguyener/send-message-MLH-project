from twilio.rest import Client
from dotenv import load_dotenv
import os # gives commands to find the env vars

load_dotenv() # loads.env file

# Your Account SID from twilio.com/console
    # environment variables
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
# Your Auth Token from twilio.com/console
AUTH_TOKEN  = os.getenv("AUTH_TOKEN")
# created variables
TO_NUMBER = os.getenv("TO_NUMBER")
FROM_NUMBER = os.getenv("FROM_NUMBER")
client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    to=TO_NUMBER, 
    from_=FROM_NUMBER,
    body="This is a test to send a text message :D")

print(message.sid)
