""" Simple module which will email the member who just enrolled by taking the email address from enrollment_info """

import enrollment_user_interface as enrollment_info
import smtplib
import ssl
import os
from dotenv import load_dotenv

load_dotenv()  # loads the encapsulated values from the .env file

port = 465  # Establishes localhost for SSL

smtp_server = "smtp.gmail.com"
crypto_ledger_email = "cryptocurrencyledger380@gmail.com"  # Enter your address
new_member_email = enrollment_info.return_user_information()  # Enter receiver address
_PASSWORD = os.getenv('EMAIL_PASSWORD')  # Encapsulated/private variable
_CRYPTO_LEDGER_PASS = _PASSWORD


message_to_send = """\
Subject: Thanks for registering!

Your account has successfully been created! 

"""

establish_secure_connection = ssl.create_default_context()

# Declaration of logic to send email to user
with smtplib.SMTP_SSL(smtp_server, port, context=establish_secure_connection) as server:
    server.login(crypto_ledger_email, _CRYPTO_LEDGER_PASS)
    server.sendmail(crypto_ledger_email, new_member_email, message_to_send)
