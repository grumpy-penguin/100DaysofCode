##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import smtplib
import datetime
import random
import os

MY_EMAIL = os.environ.get("bootcamp_gmail_address")
MY_PASSWORD = os.environ.get("boootcamp_gmail_auth_key")
greeting = []

birthdays = pandas.read_csv("day32/birthday-wisher/birthdays.csv")
now = datetime.datetime.now()
for range in birthdays.index:
    if  birthdays["month"].loc[range] == now.month and birthdays["day"].loc[range] == now.day:
        choice = random.randint(1,3)
        with open(f"day32/birthday-wisher/letter_templates/letter_{ choice }.txt") as greetings:
            for line in greetings.readlines():
                greeting.append(line.replace("[NAME]", birthdays['name'].loc[range]))
        wishes = ''.join(map(str, greeting))
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthdays["email"].loc[range],
                msg=f"Subject: Birthday Greetings\n\n{ str(wishes) }"
            )
