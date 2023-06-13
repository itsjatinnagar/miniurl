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
    message.add_alternative(Template("<body style='box-sizing:border-box;margin:0;padding:0;font-family:system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Oxygen,Ubuntu,Cantarell,'Open Sans','Helvetica Neue',sans-serif;font-size:16px;font-weight:400;line-height:1.5'><div style=background-color:#f7f7f7;padding:20px><div style=background-color:#fff><div style='border-bottom:1px solid #ccc;padding:20px'><img alt=MiniUrl src='https://drive.google.com/uc?export=view&id=1E2NpGLOCkJ_y_KFUqHuf-QF782Ux_gI4'style=display:block;max-height:30px;width:auto></div><div style='padding:20px 20px 0 20px'><p style=font-size:16px><span>Hi $username,</span><p style=font-size:16px><b>Your 6-Digit verification code is:</b><span style=display:block;color:#0bef79;padding-top:4px>$code</span><p style=font-size:16px><span>This code was sent to you to verify your login.</span><p style=margin-bottom:0;font-size:16px><span>If you didn\"t request this, you can ignore this email.</span></div><div style='padding:20px 20px 0 20px'><p style=margin:0;font-size:16px><span style=display:block>Thanks,</span><span style=display:block>The MiniUrl Team</span></div><div style=padding:20px;text-align:center;color:#9a9a9a><p><span>Copyright © 2023 MiniUrl</span></div></div></div>").substitute(username=userEmail.split('@')[0],code=code),subtype="html")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email, password)
        smtp.send_message(message)