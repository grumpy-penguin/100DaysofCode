import os
import requests
from twilio.rest import Client

long = os.environ.get("bootcamp_longitude")
lat = os.environ.get("bootcamp_latitude")
apikey = os.environ.get("bootcamp_opeweatherapikey")
account_sid = os.environ.get("bootcamp_twilio_sid")
auth_token = os.environ.get("bootcamp_twilio_auth")
from_phone = os.environ.get("bootcamp_twilio_phone")
to_phone = os.environ.get("bootcamp_myphone")
client = Client(account_sid, auth_token)

# https://api.openweathermap.org/data/2.5/weather?lat=53.021530&lon=-2.209430&appid=72d4a6b0f5f32e54ceb28df5a5eaf0d1

parameters = {
    "lat": lat,
    "lon": long,
    "appid": apikey,
    "exclude": "current,minutely,daily",
}

will_rain = False

response = requests.get(
    url="https://api.openweathermap.org/data/3.0/onecall", params=parameters
)
response.raise_for_status()
for _ in range(12):
    if 200 <= response.json()["hourly"][_]["weather"][0]["id"] <= 531:
        will_rain = True

if will_rain:
    message = client.messages.create(
        body="You will need an umbrella today",
        from_=from_phone,
        to=to_phone,
    )
    print(message.status)
