import os
import requests
from datetime import datetime

NUTRITIONIX_APPID = os.environ.get("bootcamp_nutritionix_appid")
NUTRITIONIX_APIKEY = os.environ.get("bootcamp_nutritionix_apikey")
SHEETY_ENDPOINT = os.environ.get("bootcamp_sheety_workout_endpoint")

today = datetime.now()

exercise_query = input("What exercise did you do today?: ")

exercise_headers = {
    "x-app-id": NUTRITIONIX_APPID,
    "x-app-key": NUTRITIONIX_APIKEY
}

exercise_params = {
    "query": exercise_query
}
exercise_r = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=exercise_params, headers=exercise_headers)
exercise_r.raise_for_status()

for _ in exercise_r.json()["exercises"]:
    # print(_['duration_min'])
    # print(_['nf_calories'])
    # print(_['name'])
    date = today.strftime("%d/%m/%Y")
    time = today.strftime("%I:%M:%S")

    sheety_headers = {
        "Authorization": f"Bearer {os.environ.get('bootcamp_sheety_workout_bearer')}",
        "Content-Type": "application/json"
    }

    sheety_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": _["name"].title(),
            "duration": int(_["duration_min"]),
            "calories": int(_["nf_calories"])
        }
    }

    sheety_r = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=sheety_headers)
    sheety_r.raise_for_status()
    print(sheety_r.text)
