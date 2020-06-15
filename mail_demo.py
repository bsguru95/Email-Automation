import pandas as pd
import os
import smtplib
# import imghdr
from email.message import EmailMessage


#Read data from excel using pandas
e = pd.read_excel("emails.xlsx")

#fetch email address
emailsend = e['Emails'].values

#User name and password from environment variables
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

msg = EmailMessage()
msg['Subject'] = 'MAIL by Python script'
msg['From'] = EMAIL_ADDRESS
msg['To'] = e['Emails'].values
msg.set_content('Automated message by python script')

files = ['resume.pdf']

for file in files:
   with open(file,'rb') as f:
      file_data = f.read()
      file_name = f.name
      
msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com',1025) as smtp:
# # with smtplib.SMTP('smtp.gmail.com',1025) as smtp:
#      smtp.ehlo()
      smtp.starttls()
#      smtp.ehlo()

      smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    
#      body = 'Automated mail by python'

#      msg = f'Subject: {subject}\n\n{body}'

      smtp.send_message(msg)
