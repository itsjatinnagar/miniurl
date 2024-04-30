from email.message import EmailMessage
import os
import smtplib

def sendMail(receiver_mail, code):
  message = EmailMessage()
  message['From'] = os.environ['EMAIL_USER']
  message['To'] = receiver_mail
  message['Subject'] = "Here's the code you requested"
  message.set_content(f"""\
Your sign in code is: {code}
This code is valid for the next 15 minutes only.
Remember, do not share this code with anyone.
The MiniUrl Team
""")
  message.add_alternative("""\
<html>
  <head></head>
  <body style="font-family:system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Oxygen,Ubuntu,Cantarell,'Open Sans','Helvetica Neue',sans-serif;font-size:16px;font-weight:400;line-height:1.5">
    <p>Your sign in code is: <b>{code}</b></p>
    <p>This code is valid for the next <b>15 minutes</b> only.</p>
    <p>Remember, do not share this code with anyone.</p>
    <p><b>The MiniUrl Team</b></p>
  </body>
</html>
""".format(code=code),subtype="html")
  with smtplib.SMTP_SSL(os.environ['EMAIL_HOST'], os.environ['EMAIL_PORT']) as smtp:
    smtp.login(os.environ['EMAIL_USER'], os.environ['EMAIL_PASS'])
    smtp.send_message(message)