import os
import requests
from datetime import datetime

USERNAME = "grumpy-penguin"
TOKEN = os.environ.get("bootcamp_pixelaapi")
URL = "https://pixe.la/v1"
GRAPH = "water"
date = datetime.now()
today = date.strftime('%Y%m%d')

headers = {
    "X-USER-TOKEN": TOKEN
}
user_endpoint = f"{URL}/users"
graph_endpoint = f"{user_endpoint}/{USERNAME}/graphs"
mygraph_endpoint = f"{graph_endpoint}/{GRAPH}"
pixel_endpoint = f"{mygraph_endpoint}/increment"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# user_r = requests.post(url=user_endpoint, json=user_params)
# user_r.raise_for_status
# print(user_r.text)

graph_params = {
    "id": GRAPH,
    "name": "Water consumption",
    "unit": "cups",
    "type": "int",
    "color": "sora"
}

# graph_r = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# graph_r.raise_for_status()
# print(graph_r.text)

# pixel_headers = {
#     "X-USER-TOKEN": TOKEN,
#     "Content-Length": "0"
# }

# pixel_r = requests.put(url=pixel_endpoint, headers=pixel_headers)
# pixel_r.raise_for_status()
# print(pixel_r.text)

pixel_params = {
    "date": today,
    "quantity": "1"
}

pixel_r = requests.post(url=mygraph_endpoint, json=pixel_params, headers=headers)
pixel_r.raise_for_status()
print(pixel_r.text)
