#!/usr/bin/python
import sys
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import time

def main():
    msg = MIMEMultipart()
    msg['Subject'] = 'Today\'s XKCD Comic!'


def getTime():
    return time.strftime('%A, %B %d %Y')


if __name__ == '__main__':
    main()
