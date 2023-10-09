import requests
from datetime import datetime
USER_NAME = "nobin9670"
TOKEN = "asldkfjuiebsdfDhfk"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

user_prams = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
# response = requests.post(url=pixela_endpoint, json=user_prams)
# # print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# # print(response.text)

dot_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
today = datetime.now()
DATE = today.strftime("%Y%m%d")
dot_config = {
    "date": DATE,
    "quantity": input("How many Km did you cycle you today?")
}

# response = requests.post(url=dot_endpoint, json=dot_config, headers=headers)
# # print(response.text)

update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{DATE}"
update_config = {
    "quantity": "10"
}
# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# # print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{DATE}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)