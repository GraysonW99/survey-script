# ttweetcli.py
# Grayson Whiteley
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Retrieve and parse list file
print("Please specify file containing list of potential recipients. Example: testList.txt")
emailList = input()
file1 = open(emailList, 'r')
lines = file1.readlines()
print("Retrieved %s emails!"% len(lines))

# Select n random participants in O(n) time
print("Please specify how many recipients to be randomly selected. Example: 2")
numRecipients = int(input())
recipients = []
size = len(lines)
for i in range(numRecipients):
    index = random.randrange(size)
    recipients.append(lines[index].strip())
    lines[index] = lines[size - 1]
    size -= 1
print("Retrieved %s random recipients!"% len(recipients))

# Send the email
s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
s.starttls()
print("Please enter your sender address.")
MY_ADDRESS = input()
print("Please enter your password.")
PASSWORD = input()
s.login(MY_ADDRESS, PASSWORD)
print("Please specify file containing email content.")
emailContent = input()
file2 = open(emailContent, 'r')
message = file2.read()
print("Please enter the subject line of your email.")
subjectLine = input()
for recipient in recipients:
    msg = MIMEMultipart()
    msg['From'] = MY_ADDRESS
    msg['To'] = recipient
    msg['Subject'] = subjectLine
    msg.attach(MIMEText(message, 'plain'))
    s.send_message(msg)
    del msg
