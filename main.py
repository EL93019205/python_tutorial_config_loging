"""
main
"""
from email.mime import multipart
from email.mime import text
import smtplib


import account


SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 587
FROM_EMAIL = account.from_email()
TO_EMAIL = account.to_email()
USERNAME = account.username()
PASSWORD = account.password()

MSG = multipart.MIMEMultipart()
MSG['Subject'] = 'Test email sub'
MSG['From'] = FROM_EMAIL
MSG['To'] = TO_EMAIL
MSG.attach(text.MIMEText('Test email', 'plain'))

with open('main.py', 'r') as f:
    attachment = text.MIMEText(f.read(), 'plain')
    attachment.add_header(
        'Content-Disposition', 'attachment',
        filename='lesson.txt'
    )
    MSG.attach(attachment)

SERVER = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
SERVER.ehlo()
SERVER.starttls()
SERVER.ehlo()
SERVER.login(USERNAME, PASSWORD)
SERVER.send_message(MSG)
SERVER.quit()
