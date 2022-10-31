import os
import smtplib
from dotenv import load_dotenv
import datetime as dt
import random 
import pandas

load_dotenv()

my_email = os.getenv('MY_EMAIL')
password = os.getenv('MAILER_PASSWORD')

now = dt.datetime.now()
today = now.weekday()
# check birthdays
data = pandas.read_csv('./birthdays.csv', index_col=['month', 'day'])
birthday_dict = data.to_dict(orient='index')
month_day_tuple = (now.month, now.day)

if month_day_tuple in birthday_dict:
    birthday_person = birthday_dict[month_day_tuple]['name']
    birthday_email = birthday_dict[month_day_tuple]['email']
    rand_num = random.randint(1,3)
    letter_url = f"./letter_templates/letter_{rand_num}.txt"
    with open(letter_url) as file:
        letter = file.read()
        letter = letter.replace("[NAME]", birthday_person)
        smtp_address = ""
    if 'yahoo' in my_email:
        smtp_address = 'smtp.mail.yahoo.com'
    elif 'gmail' in my_email:
        smtp_address =  'smtp.gmail.com'
    elif 'live' in my_email:
        smtp_address =  'smtp.live.com'
    elif 'outlook' in my_email:
        smtp_address =  'smtp-mail.outlook.com'
    
    with smtplib.SMTP(smtp_address) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=birthday_email, 
            msg=f"Subject:Happy Birthday!\n\n{letter}"
        )
    
##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)





