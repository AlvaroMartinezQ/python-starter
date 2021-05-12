# Script sends a mail using smtplib, SSL and gmail SMTP

import smtplib, ssl

# Local
import config_reader

def send_email():
    data = config_reader.read_properties()
    print(data)

    port = data['port']
    sender_email = data['email']
    password = data['passw']
    receiver_email = input("Type your receiver email and press enter: ")
    message = """\
        Subject: Hello there

        This is a message send with python."""

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

if __name__ == '__main__':
    send_email()
