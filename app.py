from controllers.database import insertUser, readUser
from controllers.mailer import emailCode
from dotenv import load_dotenv
from flask import Flask, render_template, request, session, redirect, url_for
import os
import random
import string

OTP_LENGTH = 6
load_dotenv()


app = Flask(__name__)
app.secret_key = os.environ['SESSION_KEY']


@app.route("/")
def index():
    try:
        identifiers = session['userID']
    except:
        identifiers = None

    if identifiers is None:
        return render_template('index.html')
    else:
        return render_template('index.html', username = session['user_email'].split('@')[0])


@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        code = ''.join(random.choices(string.digits, k=OTP_LENGTH))
        isSent = emailCode(request.args['email'], code)
        if isSent:
            session['user_email'] = request.args['email']
            session['auth_code'] = code
            return "Success", 200
        else:
            return "Unsuccessful", 500
    else:
        if session['auth_code'] == request.json['code']:
            result = readUser(session['user_email'])
            if result is False:
                return "Unsuccessful", 500
            elif result is None:
                result = insertUser(session['user_email'])
                if result is False:
                    return "Unsuccessful", 500
                else:
                    session.pop('auth_code')
                    session['userID'] = result
                    return "Success", 200
            else:
                session.pop('auth_code')
                session['userID'] = '1'
                return "Success", 200
        else:
            return "Invalid Code", 401

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))