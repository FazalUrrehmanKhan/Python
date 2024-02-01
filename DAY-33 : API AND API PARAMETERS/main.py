# TO SEND A MAIL WHEN A ISS IS ABOVE YOU DURING THE NIGHT TIME 
import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 25.204849
MY_LNG = 55.270782

my_email = "fazal20022002@gmail.com"
password = "shfm ucsn ewyx owyz"


def is_iss_overhead():
    response_2 = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_2.raise_for_status()

    latitude = float(response_2.json()["iss_position"]["latitude"])
    longitude = float(response_2.json()["iss_position"]["latitude"])

    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LNG - 5 <= longitude <= MY_LNG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response_1 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response_1.raise_for_status()

    sunrise = int(response_1.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(response_1.json()["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject : LOOK UP\n\nISS is above you")

    time.sleep(60)
