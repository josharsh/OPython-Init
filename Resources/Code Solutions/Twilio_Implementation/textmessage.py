
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "USE YOUR OWN"
# Your Auth Token from twilio.com/console
auth_token  = "USER YOUR OWN"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="USE THE NUMBER WHICH IS VERIFIED BY TWILIO", 
    from_="USER YOUR TWLIO PROVIDED NUMBER",
    body="MESSAGE HERE")

print(message.sid)
