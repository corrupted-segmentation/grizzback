import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from jinja2 import Environment, FileSystemLoader

def sendEmail(userId):

    env = Environment(loader=FileSystemLoader('templates'))
    

    me = 'me@ryanprairie.com'
    you = 'auto@sportspizza.online'

    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'better'
    msg['From'] = you
    msg['To'] = me
    
    template = env.get_template('email.html')
    body = str(template.render(uid=userId))

    message = "there was a problem"

    msg.attach(MIMEText(message, 'plain'))
    msg.attach(MIMEText(body, 'html'))

    s = smtplib.SMTP(host='localhost', port=25)
    s.sendmail(you, [me], msg.as_string())
    s.quit()

sendEmail()
