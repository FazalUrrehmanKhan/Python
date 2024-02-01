import pandas
import datetime as dt
import random
import smtplib

my_email = "<your email>"
password = "<your app password>"

data = pandas.read_csv("birthdays.csv")
today = dt.datetime.now()
month = today.month
day = today.day

lis = data.to_dict(orient="records")

for record in lis:
    if record["month"] == month and record["day"] == day:
        number = random.randint(1, 3)
        with open(f"letter_templates/letter_{number}.txt") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", record["name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=record["email"],
                                msg=f"Subject : Happy\n\n{letter}")
