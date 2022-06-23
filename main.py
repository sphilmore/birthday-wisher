import smtplib
import random
from email.mime.text import MIMEText
import datetime as dt
import pandas as pd
now = dt.datetime.now()
today = (now.month, now.day)
data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row['month'],data_row['day']): data_row for (index, data_row) in data.iterrows()}
birthday_person = birthdays_dict[today]
my_email = ""
send_to = birthday_person["email"]
if today in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
     contents = file.read()
    msg = MIMEText(f'{(contents.replace("[NAME]",birthday_person["name"]))}')
    msg['Subject'] = 'Happy Birthday'
    msg['From'] = my_email
    msg['To'] = send_to
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, "vecjkbgzfbsufymx")
        connection.sendmail(my_email,send_to, msg.as_string())







