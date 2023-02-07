from email.message import EmailMessage
import smtplib
import ssl
import os
import mimetypes

email_password = open('pass','r').read()

email_origin = 'diego.ads.freelancer@gmail.com'
email_destination = ('dxdiegofelipe@hotmail.com')

subject = 'ORÇAMENTO'

# body = open('body_email.txt','r').read()
body = open('body_email.html','r').read()

message_data = EmailMessage()
message_data['From'] = email_origin
message_data['To'] = email_destination
message_data['Subject'] = subject

message_data.set_content(body, subtype='html')
safe = ssl.create_default_context()


with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as server:
    
    server.login(email_origin, email_password)
    server.sendmail(email_origin, email_destination, message_data.as_string())