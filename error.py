from email.message import EmailMessage
import smtplib
import ssl
from password import *
import sys

email_sender = 'nandhureddy1310@gmail.com'
email_password = passcode


email = sys.argv[1]
email_receiver = email

subject = f"link error"
body = f"""
link is broken or not entered correctly
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())