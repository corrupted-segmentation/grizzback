import smtplib

from email.mime.text import MIMEText

def sendEmail():
    msg = MIMEText('this is a test', 'plain')

    me = 'me@ryanprairie.com'
    you = 'auto@sportspizza.online'
    msg['Subject'] = 'test'
    msg['From'] = you
    msg['To'] = me

    s = smtplib.SMTP(host='localhost', port=25)
    s.sendmail(you, [me], msg.as_string())
    s.quit()
