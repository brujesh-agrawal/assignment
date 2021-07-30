import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:
    from_email = 'example@gmail.com'
    from_email_password = 'examplepassword'

    smtpObj = smtplib.SMTP(host='smtp.gmail.com', port=587)
    smtpObj.starttls()
    smtpObj.login(from_email, from_email_password)

    subject = input("Subject: ")
    body = input("Body: ")
    receipient = input("Receipient: ")

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = receipient
    msg['Subject'] = subject

    message = body
    msg.attach(MIMEText(message, 'plain'))

    smtpObj.send_message(msg)
    print("Email Sent!")

    del msg
except Exception as e:
    print(e)
