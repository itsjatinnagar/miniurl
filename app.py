import logging
import os
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, request, session, jsonify, redirect, url_for

from database.links import insertLink, readAllLinks, readRedirectLink, updateLinkClicks
from database.analytics import insertAgent
from database.user import insertUser, readUser
from decorators.auth import session_auth
from utils.mail import emailVerificationCode
from utils.token import tokenEncode
from utils.verificationCode import generateVerificationCode, hashedVerificationCode, checkVerificationCode, generateLinkHash

load_dotenv()

app = Flask(__name__, static_folder='app', static_url_path="/")
app.config['SECRET_KEY'] = os.environ['SESSION_KEY']
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_SAMESITE='Strict'
)

@app.route('/')
def index():
    return app.send_static_file("index.html")

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file("favicon.ico")

@app.route('/manifest.json')
def manifest():
    return app.send_static_file("manifest.json")

@app.route('/icon192.png')
def icon192():
    return app.send_static_file("icon192.png")

@app.route('/icon512.png')
def icon512():
    return app.send_static_file("icon512.png")

@app.route('/auth', methods=['POST'])
def auth():
    try:
        userEmail = request.json['email']
        verificationCode = generateVerificationCode()
        hashedCode = hashedVerificationCode(verificationCode)
        emailVerificationCode(userEmail,verificationCode)
        session['email'] = userEmail
        session['code'] = hashedCode
        return jsonify({'type': 'success', 'message': 'verification code sent', 'email': userEmail}), 200
    except Exception as error:
        logging.error(error)
        return jsonify({'type': 'error', 'message': 'internal server error'}), 500

@app.route('/verify', methods=['POST'])
def verify():
    try:
        userCode = request.json['code']
        if not checkVerificationCode(userCode,session['code']):
            return jsonify({'type':'error', 'message':'incorrect code'}), 403
    
        user = readUser(session['email'])
        if user is None:
            id = insertUser(session['email'])
            user = (id, session['email'])

        session.clear()
        session['token'] = tokenEncode({"id": user[0], "email": user[1]})
        session['address'] = request.remote_addr
        session.permanent = True
        return jsonify({'type':'success', 'message': 'user verified'}), 200
    except Exception as error:
        logging.error(error)
        return jsonify({'type': 'error', 'message': 'internal server error'}), 500

@app.route('/user', methods=['GET'])
@session_auth
def user():
    try:
        return jsonify({'type':'success', 'data': request.data}), 200
    except Exception as error:
        logging.error(error)
        return jsonify({'type': 'error', 'message': 'internal server error'}), 500

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/shorten', methods=['POST'])
@session_auth
def shorten():
    try:
        userId = request.data['id']
        userLink = request.json['link']
        hash = generateLinkHash()
        created_at = int(datetime.now().timestamp())
        linkId = insertLink(userId,hash,userLink,created_at)
        return jsonify({'type':'success','data':{'id': linkId,'long_link':userLink,'hash':hash,'clicks':0,'created_at': created_at}}),200
    except Exception as error:
        logging.error(error)
        return jsonify({'type': 'error', 'message': 'internal server error'}), 500

@app.route('/links', methods=['GET'])
@session_auth
def links():
    try:
        userId = request.data['id']
        result = readAllLinks(userId)
        data = [{'id':item[0],'long_link':item[3],'hash':item[2],'clicks':item[5],'created_at':item[4]} for item in result]
        return jsonify({'type':'success','data':{'links':data}}),200
    except Exception as error:
        logging.error(error)
        return jsonify({'type': 'error', 'message': 'internal server error'}), 500

@app.route('/<string:hash>', methods=['GET'])
def redirectOriginal(hash):
    try:
        result = readRedirectLink(hash)
        if result is None:
            return redirect(url_for('index'),404)
            
        updateLinkClicks(result[0], int(result[2]) + 1)
        insertAgent(result[0], str(request.user_agent), int(datetime.now().timestamp()))
        return redirect(result[1])
    except Exception as error:
        logging.error(error)
        return redirect(url_for('index'),500)