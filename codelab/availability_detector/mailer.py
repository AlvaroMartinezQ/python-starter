# Script sends a mail using smtplib, SSL and gmail SMTP

import smtplib, ssl

# Local
import config_reader

def send_email(receiver, subject, text):
    data = config_reader.read_properties()

    port = data['port']
    smtp_server = data['smtp']
    sender_email = data['email']
    password = data['passw']
    receiver_email = receiver
    message = 'Subject: {}\n\n{}'.format(subject, text)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

if __name__ == '__main__':
    send_email()
