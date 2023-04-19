from email.message import EmailMessage
import os
import smtplib


def emailCode(userEmail, code):
    email = os.environ['EMAIL_ADDR']
    password = os.environ['EMAIL_PASS']
    message = EmailMessage()
    message['From'] = email
    message['To'] = userEmail
    message['Subject'] = 'Login Code for MiniUrl'
    # Fallback Content
    message.set_content(
        f"Hey {userEmail.split('@')[0]}!\n\nYour sign in code is: {code}\n\nThanks,\nMiniUrl")
    # HTML Content
    message.add_alternative(f"""\
    <!DOCTYPE html>
    <html lang="en">
    <body>
        <p style="font-size:18px;font-weight:bold;">Hey {userEmail.split('@')[0]}!</p>
        <p style="font-size:20px;text-align:center;">Your sign in code is: <strong style="color:#2acfcf;">{code}</strong></h2>
        <p>Thanks,<br>MiniUrl</p>
    </body>
    </html>
    """, subtype='html')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email, password)
        smtp.send_message(message)