#!/usr/bin/python
import sys
import time
from classes.myemail import MyEmail

def main():

    attachment = sys.argv[1]
    current_time = getTime()
    to_email = ['connor.runyan@aggiemail.usu.edu']
    content = ''
    subject = 'Daily XKCD Comic - {0}'.format(current_time)

    mail = MyEmail()
    mail.setEmail(to_email, content)
    mail.setSubject(subject)
    mail.addAttachment(attachment)
    mail.sendEmail()


def getTime():
    '''Return date and time now.'''
    return time.strftime('%c')

if __name__ == '__main__':
    main()
