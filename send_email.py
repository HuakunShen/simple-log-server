import os
import smtplib
from dotenv import load_dotenv


load_dotenv()
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
MAIL_SERVER = os.environ.get("MAIL_SERVER")
RECEIVER_ADDRESS = os.environ.get('RECEIVER_ADDRESS')
MAIL_SERVER_ADDR = MAIL_SERVER.split(':')[0]
MAIL_SERVER_PORT = int(MAIL_SERVER.split(':')[1])


def send_email(subject, msg, to_email=RECEIVER_ADDRESS):
    try:
        server = smtplib.SMTP(MAIL_SERVER_ADDR, MAIL_SERVER_PORT)
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = '{}\n\n{}'.format(subject, msg)
        server.sendmail(EMAIL_ADDRESS, to_email, message)
        server.quit()
        print("Success: Email sent!")
        return True
    except Exception as e:
        print(e)
        print("Email failed to send.")
        return False
