import pandas
import datetime as dt
import random
import smtplib

my_email = "rehabviking@gmail.com"
password = "fspswohpgrxymdix"
birthdays_obj = pandas.read_csv(r"birthdays.csv")
birthdays_dict = birthdays_obj.to_dict("records")

now = dt.datetime.now()
current_month = now.month
current_day = now.day

for birthdays in birthdays_dict:
    if birthdays['month'] == current_month and birthdays['day'] == current_day:
        text_file_no = random.randint(1, 3)
        text_file = f"letter_templates/letter_{text_file_no}.txt"
        with open(text_file) as birthday_letter_file:
            birthday_letter = birthday_letter_file.read()
        new_letter = birthday_letter.replace("[NAME]", birthdays["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=birthdays["email"], msg=f"Subject:Happy "
                                                                                     f"Birthday\n\n{new_letter}")
            connection.close()










