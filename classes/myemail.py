#!/usr/bin/python
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import time

class MyEmail():
    '''Generic email class, can be used to send an email.'''
    def __init__(self):
        self.msg = MIMEMultipart()

    def __str__(self):
        return 'Contents: {0}'.format(self.msg.as_string())
   
    def addAttachment(self, att_path):
        '''Attaches a file to current email object.'''
        with open(att_path, 'rb') as IMG_FH:
            img = MIMEImage(IMG_FH.read())
        self.msg.attach(img)

    def sendEmail(self):
        '''Send email with configured contents'''
        smtp = smtplib.SMTP('smtp.gmail.com:587')
        smtp.starttls()
        smtp.login(<EMAIL_HERE>, <PASSWORD_HERE>)
        mail_to = self.msg['To']
        mail_from = self.msg['From']
        message = self.msg.as_string()
        smtp.sendmail(mail_from, mail_to, message)
        smtp.quit()

    def setEmail(self, mail_to, content):
        '''Set contents of an email message'''
        #self.msg['From'] = mail_from
        self.msg['To'] = ', '.join(mail_to)
        self.msg.preamble = content

    def setSubject(self, subject):
        '''Sets the subject of the message'''
        self.msg['Subject'] = subject


