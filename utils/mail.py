from email.message import EmailMessage
from string import Template
import os
import smtplib

def emailVerificationCode(userEmail, code):
    email = os.environ['EMAIL_ADDR']
    password = os.environ['EMAIL_PASS']
    message = EmailMessage()
    message['From'] = email
    message['To'] = userEmail
    message['Subject'] = "Here's the code you requested"
    message.set_content(f"Your sign in code is: {code}\n\nThanks,\nTeam MiniUrl")
    message.add_alternative(Template('<!DOCTYPE html><html lang="en"> <head> <meta charset="UTF-8"/> <meta name="viewport" content="width=device-width, initial-scale=1.0"/> <style>.container{padding-top: 20px; padding-bottom: 20px; max-width: 500px; background-color: #eeeeee;}.image{margin-bottom: 30px; text-align: center;}.code{width: 100%; padding-top: 6px; padding-bottom: 6px; background-color: #f9f9f9; color: #8a88ef; font-size: 30px; text-align: center; letter-spacing: 4px;}</style> </head> <body> <div class="container"> <div> <div class="image"> <img src="https://miniurl.onrender.com/static/images/logo.svg" alt="MiniUrl"/> </div><div> <p class="code">$code</p></div></div></div></body></html>').substitute(code=code),subtype="html")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email, password)
        smtp.send_message(message)