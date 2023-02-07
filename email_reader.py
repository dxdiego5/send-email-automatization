from imbox import Imbox
from datetime import datetime

username = 'xxxxxxxx@gmail.com'
password = open('pass','r').read()
host = 'imap.gmail.com'

mail = Imbox(host, username=username, password=password, ssl=True)
messages = mail.messages()

for (uid, message) in messages:
    print(message.subject)
    print(message.date)

    if len(message.attachments) > 0:
        # print(message.attachments)
        for attachment in message.attachments:
            file = open('attachments/report.pdf', 'wb')
            attachment['content'].seek(0)
            file.write(attachment['content'].read())
            file.close()
        break
    print('-----------------------------------------')