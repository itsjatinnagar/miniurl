import os
import random
import secrets
from datetime import datetime
from dotenv import load_dotenv
from string import digits
from flask import Flask, redirect, render_template, request, session, url_for

from controllers.helper import fetchTitle, generateHash
from controllers.links import getLinks, insertLink, readLongLink
from controllers.mailer import emailCode
from controllers.user import insertUser, readUserWithId, readUserWithMail, updateUser


OTP_LENGTH = 6
HASH_LENGTH = 4
load_dotenv()


app = Flask(__name__)
app.secret_key = os.environ['SESSION_KEY']


@app.route("/")
def index():
    try:
        identifiers = session['_id']
        isAuthenticated = session['_w__c__A']
    except:
        identifiers = None
        isAuthenticated = None

    if identifiers is None or isAuthenticated is None:
        return render_template('index.html')
    else:
        data = getLinks(session['_id'])
        result = readUserWithId(session['_id'])
        if result and data is not False:
            return render_template('user.html', username = result[1].split('@')[0], host=request.host_url, data = data)
        else:
            return render_template('index.html', result = result, data = data), 500


@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        code = ''.join(random.choices(digits, k=OTP_LENGTH))
        isSent = emailCode(request.args['email'], code)
        if isSent:
            result = readUserWithMail(request.args['email'])
            if result is False:
                return "Unsuccessful", 500
            elif result is None:
                result = insertUser(request.args['email'], code)
                if result is False:
                    return "Unsuccessful", 500
                else:
                    session['_id'] = result[0]
                    return "Success", 200
            else:
                isUpdated = updateUser(result[0], code)
                if isUpdated:
                    session['_id'] = result[0]
                    return "Success", 200
                else:
                    return "Unsuccessful", 500
        else:
            return "Unsuccessful", 500
    else:
        result = readUserWithId(session['_id'])
        if result is False:
            return "Unsuccessful", 500
        elif result is None:
            return "Unauthorized", 401
        else:
            if result[2] == request.json['code']:
                session['_w__c__A'] = secrets.token_hex(8)
                return "Success", 200
            else:
                return "Invalid Code", 400


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.json['long_url']
    title = fetchTitle(long_url)
    hash = generateHash(HASH_LENGTH)
    if hash is False or title is None:
        return f"{hash} or {title}", 500
    else:
        result = insertLink(session['_id'],title,hash,long_url,datetime.utcnow().strftime('%s'))
        if result is False:
            return "Insert", 500
        else:
            return "Success", 200


@app.route('/<string:hash>')
def returnOriginal(hash):
    result = readLongLink(hash)
    if result is False or result is None:
        return redirect(location=url_for('index'),code=500)
    else:
        return redirect(result[0])