import requests
from datetime import datetime

USERNAME = "devindevn"
TOKEN = "abcdef2929292929"
GRAPH_ID = "graphdvn"

pixela_endpoint = "https://pixe.la/v1/users"

# user_parameters = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Habit Graph",
    "unit": "done",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()

pixel_post = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1"
}


# response = requests.post(url=pixel_post, json=pixel_data, headers=headers)
# print(response.text)