import os
from datetime import date
from datetime import timedelta
from twilio.rest import Client

import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API=os.environ.get("bootcamp_stockapi")
NEWS_API=os.environ.get("bootcamp_newsapi")

account_sid = os.environ.get("bootcamp_twilio_sid")
auth_token = os.environ.get("bootcamp_twilio_auth")
from_phone = os.environ.get("bootcamp_twilio_phone")
to_phone = os.environ.get("bootcamp_myphone")

TODAY=date.today()
# If Monday then yesterday is Friday, so today - 3 and day before is thursday so today - 4
# If Tuesday then yesterday is today -1, but day before is Friday so today - 4
# If Sunday then yesterday is today -2 and day before is Thursday so today -3
if  6 < TODAY.weekday() > 1:
    YESTERDAY=TODAY - timedelta(days=1)
    DAYBEFORE=TODAY - timedelta(days=2)
elif TODAY.weekday() == 6:
    YESTERDAY=TODAY - timedelta(days=2)
    DAYBEFORE=TODAY - timedelta(days=3)
elif TODAY.weekday() == 0:
    YESTERDAY=TODAY - timedelta(days=3)
    DAYBEFORE=TODAY - timedelta(days=4)
else:
    YESTERDAY=TODAY - timedelta(days=1)
    DAYBEFORE=TODAY - timedelta(days=4)

STOCK_PARAMS = {
    "apikey":STOCK_API,
    "symbol": STOCK,
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "outputsize": "compact"
}
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_r=requests.get(url="https://www.alphavantage.co/query", params=STOCK_PARAMS)
stock_r.raise_for_status()

stock_yesterday = float(stock_r.json()["Time Series (Daily)"][str(YESTERDAY)]["4. close"])
stock_daybefore = float(stock_r.json()["Time Series (Daily)"][str(DAYBEFORE)]["4. close"])

if stock_daybefore > stock_yesterday:
    stock_diff = ((stock_daybefore - stock_yesterday)/stock_daybefore)*100
    stock_movement = "down"
else:
    stock_diff = ((stock_yesterday - stock_daybefore)/stock_daybefore)*100
    stock_movement = "up"

if stock_diff >= 5:
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    NEWS_PARAMS = {
        "apiKey": NEWS_API,
        "q": COMPANY_NAME,
        "from": DAYBEFORE,
        "to": YESTERDAY,
        "language": "en",
        "sortBy": "relevancy"
    }

    news_r = requests.get(url="https://newsapi.org/v2/everything", params=NEWS_PARAMS)
    news_r.raise_for_status()

    stock_news = news_r.json()["articles"][:3]

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    if stock_movement == "up":
        direction = "🔺"
    else:
        direction = "🔻"

    for _ in news_r.json()["articles"][:3]:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"TSLA: {direction} {stock_diff:.2f}%\n Headline: {_['title']}",
            from_=from_phone,
            to=to_phone,
        )
else:
    print("Stock movement less than 5%")

#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
