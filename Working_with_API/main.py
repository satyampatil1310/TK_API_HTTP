import requests
import os
APIKEY = os.environ.get("OWM_API_KEY")

parameters = {
                "lat": 43.138859,
                "lon": 12.340530,
                "appid": "6b300d9a922097ebef052cadcf8fbdeb",
                "exclude": "current,minutely,daily"
            }
response = requests.get("https://api.openweathermap.org/data/2.5/onecall?", params=parameters)
weather_data = response.json()
weather_data['hourly'][0]['weather'][0]['id']
for data in weather_data['hourly'][0:12]:
    if 600 > (data['weather'][0]['id']):
        print("it shall rain, carry your umbrella!!")
        break
