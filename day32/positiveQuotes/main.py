import smtplib
import datetime
import random
import os

MY_EMAIL = os.environ.get("bootcamp_gmail_address")
TO_EMAIL = os.environ.get("bootcamp_myemail")
MY_PASSWORD = os.environ.get("boootcamp_gmail_auth_key")

motivation = []
now = datetime.datetime.now()

try:
    with open("day32/positiveQuotes/quotes.txt") as quotes:
        motivation = quotes.readlines()
except FileNotFoundError as error_message:
    print("File Not Found")

if now.weekday() == 5:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject: Monday Motivation\n\n {motivation[random.randint(0,101)]}"
        )
else:
    print("Today is not the day")
