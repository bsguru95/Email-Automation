import smtplib
import ssl
import os
import openpyxl as xl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase

username = os.environ.get('EMAIL_USER')
password = os.environ.get('EMAIL_PASSWORD')
From = username
Subject = 'Resume'

wb = xl.load_workbook(r'emails.xlsx')
sheet1 = wb.get_sheet_by_name('Sheet1')
names = []
emails = []

for cell in sheet1['A']:
    emails.append(cell.value)

for cell in sheet1['B']:
    names.append(cell.value)


   


server = smtplib.SMTP_SSL('smtp.gmail.com', 1025)

server.login(username, password)

for i in range(len(emails)):
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = names[i]
    msg['Subject'] = Subject
    text = '''
Hello {},
PFA my resume in order to check if this mail is working.

'''.format(names[i])
    msg.attach(MIMEText(text, 'plain'))
    filename = "resume.pdf"
    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    encoders.encode_base64(part)

# Add header as key/value pair to attachment part
    part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
    )
    msg.attach(part)
    message = msg.as_string()
    server.sendmail(username, emails[i], message)
    print('Mail sent to', emails[i])

server.quit()
print('All emails sent successfully!')
