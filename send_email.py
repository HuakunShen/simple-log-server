import os
import smtplib
from dotenv import load_dotenv


load_dotenv()
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
mail_server_address = 'smtp.gmail.com:587'


def send_email(subject, msg, to_email=EMAIL_ADDRESS):
    try:
        server = smtplib.SMTP(mail_server_address)
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(to_email, EMAIL_ADDRESS, message)
        server.quit()
        print("Success: Email sent!")
    except Exception as e:
        print(e)
        print("Email failed to send.")
