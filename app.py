import logging
import os
import secrets
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, session, url_for

from controllers.analytics import getLinkAnalytics,insertAgent
from controllers.helper import generateCode, generateHash
from controllers.links import getLinks, insertLink, readLongLink, updateLink
from controllers.mailer import emailCode
from controllers.user import insertUser, readUserWithId, readUserWithMail, updateUser


OTP_LENGTH = 6
HASH_LENGTH = 4
load_dotenv()


app = Flask(__name__)
app.secret_key = os.environ['SESSION_KEY']


app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)


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
        try:
            data = getLinks(session['_id'])
            result = readUserWithId(session['_id'])
            if result is None:
                session.clear()
                return render_template('index.html')
            return render_template('user.html', username = result[1].split('@')[0], host=request.host_url, data = data)
        except Exception as error:
            logging.error(error)


@app.route("/login", methods=['GET','POST'])
def login():
    try:
        if request.method == 'GET':
            code = generateCode(OTP_LENGTH)
            emailCode(request.args['email'], code)
            user = readUserWithMail(request.args['email'])
            if user is None:
                userId = insertUser(request.args['email'], code)
            else:
                userId = user[0]
                updateUser(userId, code)
            session['_id'] = userId
            return "Success", 200
        else:
            user = readUserWithId(session['_id'])
            if user is None:
                return "Unauthorized", 401
            if user[2] == request.json['code']:
                session['_w__c__A'] = secrets.token_hex(8)
                return "Success", 200
            return "Invalid Code", 400
    except Exception as error:
        logging.error(error)
        return "Internal Server Error", 500


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/shorten', methods=['POST'])
def shorten():
    try:
        long_url = request.json['long_url']
        hash = generateHash(HASH_LENGTH)
        insertLink(session['_id'],hash,long_url,datetime.utcnow().strftime('%s'))
        return "Success", 200
    except Exception as error:
        logging.error(error)
        return "Internal Server Error", 500


@app.route('/miniurl')
def linkInfo():
    try:
        linkId = request.args['id']
        result = getLinkAnalytics(linkId)
        return render_template('sidebar.html', info=result)
    except Exception as error:
        logging.error(error)
        return "Internal Server Error", 500


@app.route('/<string:hash>')
def returnOriginal(hash):
    try:
        result = readLongLink(hash)
        if result is None:
            return redirect(location=url_for('index'), code=404)
        updateLink(result[0], {'click': int(result[2]) + 1})
        insertAgent(result[0], str(request.user_agent), datetime.utcnow().strftime('%s'))
        return redirect(result[1])
    except Exception as error:
        logging.error(error)
        return redirect(location=url_for('index'),code=500)