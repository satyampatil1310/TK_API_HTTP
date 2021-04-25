##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# birthdays = {
#                 "name": ,
#                 "email": ,
#                 "year": ,
#                 "month": ,
#                 "day": ,
#             }
import pandas as pd
import datetime as dt
import random
from smtplib import SMTP

df = pd.read_csv("birthdays.csv")
dict = df.to_dict()

date = str(dt.datetime.now().strftime("%Y%m%d"))
month = int(date[4:6])
day = int(date[6:8])
try:
    for i in range(0, 100):
        if int(dict["month"][i]) == month and int(dict["day"][i]) == day:
            file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
            with open(file_path) as file:
                content = file.read()
                content.replace("[NAME]", dict['name'][i])
            with SMTP("smtp.google.com") as connection:
                connection.starttls()
                connection.login("vivra.buldhana@gmail.com", "Satyam@12345")
                connection.sendmail(from_addr="vivra.buldhana@gmail.com", to_addrs=f"{dict['email'][i]}", msg=f"Subject:Happy Birthday\n\n{content}")
except KeyError:
    pass







