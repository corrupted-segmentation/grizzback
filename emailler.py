import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail():
    f = open('../grizzfront/email.html', 'r')

    me = 'me@ryanprairie.com'
    you = 'auto@sportspizza.online'

    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'better'
    msg['From'] = you
    msg['To'] = me
    
    body = str(f.read()) 


    message = "there was a problem"

    msg.attach(MIMEText(message, 'plain'))
    msg.attach(MIMEText(body, 'html'))

    s = smtplib.SMTP(host='localhost', port=25)
    s.sendmail(you, [me], msg.as_string())
    s.quit()

sendEmail()
