"""
main
"""
import logging
import logging.handlers


import account


SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 587
FROM_EMAIL = account.from_email()
TO_EMAIL = account.to_email()
USERNAME = account.username()
PASSWORD = account.password()

LOGGER = logging.getLogger('email')
LOGGER.setLevel(logging.CRITICAL)

LOGGER.addHandler(logging.handlers.SMTPHandler(
    (SMTP_HOST, SMTP_PORT), FROM_EMAIL, TO_EMAIL,
    subject='Admin test log', credentials=(USERNAME, PASSWORD),
    secure=(None, None, None),
    timeout=20
))

LOGGER.info('test')
LOGGER.critical('critical')
