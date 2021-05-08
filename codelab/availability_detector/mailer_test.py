# Script sends a mail using smtplib and SSL

import smtplib, ssl

port = 465
sender_email = input("Type your sernder email and press enter: ")
password = input("Type your password and press enter: ")
receiver_email = input("Type your receiver email and press enter: ")
message = """\
    Subject: Hello there

    This is a message send with python."""

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
