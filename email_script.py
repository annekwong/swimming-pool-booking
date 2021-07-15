import smtplib
import json

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from glob import glob


def SimpleEmail(recipient, message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    j = json.load(open("emailc.json", "r"))
    login = j['email']
    passw = j['passw']
    s.login(login, passw)
    s.sendmail(login, recipient, message)
    s.quit()

def ContentEmail(toaddr, files):
    j = json.load(open("emailc.json", "r"))
    fromaddr = j['email']
    
    msg            = MIMEMultipart()
    msg['From']    = fromaddr
    msg['To']      = toaddr
    msg['Subject'] = 'Test subject'
    body           = 'Test body'
    msg.attach(MIMEText(body, 'plain'))
    
    for f in files:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(f, 'rb').read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment; filename={:s}".format(f))
        msg.attach(part)
    
    SimpleEmail(toaddr, msg.as_string())

# send the zip, and the log.
if __name__ == "__main__":
    toaddr = 'soslangm@gmail.com'
    zips = glob("*.zip")
    ContentEmail(toaddr, zips)