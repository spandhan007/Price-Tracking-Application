from email.message import EmailMessage
import smtplib
import ssl
from password import *
import sys

email_sender = 'nandhureddy1310@gmail.com'
email_password = passcode

link = sys.argv[1]
email = sys.argv[2]
app = sys.argv[3]
price = sys.argv[4]
email_receiver = email

subject = f"Price Has Been Dropped for the Product from {app}"
body = f"""
The Price of the product you wanted has gone down since you last seen.
Updated price is {price}
Here is the link for the product 
{link}
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

