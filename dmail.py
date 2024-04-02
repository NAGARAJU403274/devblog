import smtplib
from email.message import EmailMessage

def sendmail(to,subject,body):
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('pulligaddanaga12@gmail.com','dcbc dfjf kyea ktkp')
    msg = EmailMessage()
    msg['From']='pulligaddanaga12@gmail.com'
    msg['To'] = to
    msg['Subject'] = subject
    msg.set_content(body)
    server.send_message(msg)
    server.quit()


#sendmail('mkumbalamohan@gmail.com','hi this is codegnan','Ur are from GEC how was the class going?')
# sendmail('manishankarupputholla@gmail.com','hi this is codegnan','Ur are from GEC how was the class going?')
# sendmail('shaik.nazeerbhasha7@gmail.com','hi this is codegnan','Ur are from GEC how was the class going?')
# print('mailsended')