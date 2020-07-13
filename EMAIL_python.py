import smtplib
import getpass
from email.mime.text import MIMEText
def send_email():
    sender_address='stuteepradhan3004@gmail.com'
    password=getpass.getpass()
    subject='Learn.Inspire.Grow'
    msg='Hello this is a test mail which I am sending through python!!'
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_address,password)
    msg=MIMEText(msg)
    msg['Subject']=subject
    msg['From']=sender_address
    msg['To']='stuteepradhan3004@gmail.com'
    msg.set_param('importance','high value')
    recipients='stuteepradhan3004@gmail.com'
    server.sendmail(sender_address,recipients,msg.as_string())
send_email()











