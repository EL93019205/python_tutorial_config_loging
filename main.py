"""
main
"""
from email import message
import smtplib
import account


SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 587
FROM_EMAIL = account.from_email()
TO_EMAIL = account.to_email()
USERNAME = account.username()
PASSWORD = account.password()

MSG = message.EmailMessage()
MSG.set_content('Test email')
MSG['Subject'] = 'Test email sub'
MSG['From'] = FROM_EMAIL
MSG['To'] = TO_EMAIL

SERVER = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
SERVER.ehlo()
SERVER.starttls()
SERVER.ehlo()
SERVER.login(USERNAME, PASSWORD)
SERVER.send_message(MSG)
SERVER.quit()
