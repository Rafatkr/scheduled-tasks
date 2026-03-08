import os
import requests
from twilio.rest import Client

SP_LAT = -23.550520
SP_LON = -46.633308

MI_LAT = 25.761681
MI_LON = -80.191788

OW_URL = "https://api.openweathermap.org/data/2.5/forecast"
OW_PARAMETERS = {
    "lat" : SP_LAT,
    "lon" : SP_LON,
    "appid" : os.environ.get("OWM_API_KEY"),
    "cnt" : 4
}

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)



response = requests.get(url=OW_URL, params=OW_PARAMETERS)
response.raise_for_status()

obj = response.json()
next_id_conditions = []

will_rain = False
for hour_data in obj["list"]:
   id_condition = hour_data["weather"][0]["id"]
   next_id_conditions.append(id_condition)
   if id_condition < 700:
       will_rain = True


if will_rain:
    msg = "Bring an Umbrella!!!"
    print(msg)
else:
    msg = "No rain today!!"
    print(msg)

message = client.messages.create(
  from_="whatsapp:+14155238886",
  body=msg,
  to="whatsapp:+5511971464020"
)

print(message.status)
print(message.sid)

print(next_id_conditions)
# print(response.status_code)
# print(response.json())
