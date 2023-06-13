import logging
from flask import Blueprint,jsonify,redirect,request,session,url_for

from database.user import insertUser,readUser
from utils.mail import emailVerificationCode
from utils.token import tokenEncode
from utils.verificationCode import generateVerificationCode,hashedVerificationCode,checkVerificationCode

auth_bp = Blueprint('auth_bp',__name__)

@auth_bp.route('/auth', methods=['POST'])
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

@auth_bp.route('/verify', methods=['POST'])
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

@auth_bp.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('index'))