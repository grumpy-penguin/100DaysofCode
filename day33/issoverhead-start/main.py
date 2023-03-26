import smtplib
import requests
from datetime import datetime
import os

MY_LAT = os.environ.get("bootcamp_latitude")  # Your latitude
MY_LONG = os.environ.get("bootcamp_longitude") # Your longitude

MY_EMAIL = os.environ.get("bootcamp_gmail_address")
MY_PASSWORD = os.environ.get("boootcamp_gmail_auth_key")
TO_EMAIL = os.environ.get("bootcamp_myemail")

def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.
    if (iss_latitude >= MY_LAT - 5 and iss_latitude <= MY_LAT + 5) and (
        iss_longitude >= MY_LONG - 5 or iss_longitude <= MY_LONG + 5
    ):
        return True
    else:
        return False

print(is_iss_close())
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
if is_iss_close() and time_now.hour >= sunset or time_now.hour <= sunrise:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg="Subject: ISS Overhead\n\nLookup and see if you can spot the ISS"
        )
