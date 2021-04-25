import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "ssptl1999@gmail.com"
MY_PASSWORD = "Satyam@12345"
MY_LAT = 18.520430 # Your latitude
MY_LONG = 73.856743 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.




def is_iss_overhead():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    if (MY_LAT >= iss_latitude - 5 or MY_LAT <= iss_longitude + 5) and (MY_LONG <= iss_longitude +5 or MY_LONG >= iss_longitude - 5):
        # if time_now < sunset and time_now > sunrise:
        #     print("dark")
        return True


def is_night():
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
    time_now = datetime.now().hour
    if sunset <= time_now <= sunrise:
        return True

while True:
    if is_night() and is_iss_overhead():
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:Look up\n\nISS is above you in the sky.")
        connection.close()
        time.sleep(60)
    #If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.



