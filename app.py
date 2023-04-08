import secrets
from controllers.database import getLinks, insertLink, insertUser, readLink, readLongLink, readUserWithId, readUserWithMail, updateLink, updateUser
from controllers.helper import fetchTitle, generateHash
from controllers.mailer import emailCode
from datetime import datetime
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
        if not result:
            return render_template('index.html')
        else:
            return render_template('index.html', username = result[1].split('@')[0], host=request.host_url, data = data)


@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        code = ''.join(random.choices(string.digits, k=OTP_LENGTH))
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
                    session['_id'] = result
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
    result = insertLink(session['userID'],title,long_url,datetime.utcnow().date())
    if result is False:
        return "Unsuccessful", 500
    else:
        updateDict = {'hash': generateHash(result)}
        result = updateLink(result, updateDict)
        if result is False:
            return "Unsuccessful", 500
        else:
            return "Success", 200

@app.route('/get/<int:linkId>')
def getLinkInfo(linkId):
    result = readLink(linkId)
    if result is False:
        return 'Unsuccessful', 500
    else:
        return render_template('sidebar.html', data=result, host=request.host_url), 200
    
@app.route('/<string:hash>')
def returnOriginal(hash):
    result = readLongLink(hash)
    if result is False or result is None:
        return redirect(url_for('index'))
    else:
        return redirect(result[0])