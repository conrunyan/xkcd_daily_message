#!/usr/bin/python
import sys
import time
from classes.myemail import MyEmail

def main():

    attachment = sys.argv[1]
    to_email = ['connor.runyan@aggiemail.usu.edu']
    content = 'THIS IS A TEST'

    mail = MyEmail()
    mail.setEmail(to_email, content)
    mail.sendEmail()

if __name__ == '__main__':
    main()
