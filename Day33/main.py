# import requests
# # response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response)
# MY_LAT = 23.718786
# MT_LONG = 90.387603
# from datetime import datetime
# parameters = {
#     "lat": MY_LAT,
#     "lng": MT_LONG,
#     "formatted": 0
# }
# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()
# sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
# sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
# print(sunrise)
# print(sunset)
# time_now = datetime.now()
# print(time_now.hour)