import smtplib, ssl, getpass

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = input("Your email ID")
receiver_email = input("Receiver's Email ID")
password = getpass.getpass("Type your password and press enter: ")
message = """\
Subject: Hi there
This message is sent from Python code."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
