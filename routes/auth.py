import logging
from flask import Blueprint, jsonify, request, session
from random import randint
from time import time

from database.users import createUser, readUser
from utils.mailer import sendMail
from utils.security import checkHash, createHash

auth_bp = Blueprint('auth_bp',__name__)

@auth_bp.route('/login', methods=['POST'])
def login():
  try:
    user_mail = request.json['email']
    code = randint(1000, 9999)
    sendMail(user_mail, code)
    session['email'] = user_mail
    session['code'] = createHash(str(code))
    session['code_created_at'] = int(time())
    session['code_attempts'] = 0
    return jsonify({'type': 'success', 'message': 'verification code sent successfully', 'email': user_mail}), 200
  except Exception as error:
    logging.error(error)
    return jsonify({'type': 'error', 'message': 'something went wrong'}), 500

@auth_bp.route('/verify', methods=['POST'])
def verify():
  try:
    user_mail = session['email']
    code = request.json['code']
    if 'code' not in session or int(time()) - session['code_created_at'] > 900:
      session.pop('code',None)
      return jsonify({'type': 'error', 'message': 'OTP expired. Generate a new OTP'}), 400
    session['code_attempts'] += 1
    if session['code_attempts'] > 5:
      session.pop('code',None)
      return jsonify({'type': 'error', 'message': 'Too many incorrect OTP attempts'}), 400
    if checkHash(code, session['code']):
      user = readUser(user_mail)
      if user is None:
        created_at = int(time())
        uid = createUser(user_mail,created_at)
        user = {'id': uid, 'email': user_mail, 'created_at': created_at}
      session.clear()
      user = {'id': user['id'], 'email': user['email'], 'created_at': user['created_at']}
      session['user'] = user
      session['address'] = request.remote_addr
      session.permanent = True
      return jsonify({'type': 'success', 'message': 'verification done', 'data': user}), 200
    else:
      return jsonify({'type': 'error', 'message': 'Incorrect OTP'}), 400
  except Exception as error:
    logging.error(error)
    return jsonify({'type': 'error', 'message': 'something went wrong'}), 500
  
@auth_bp.route('/resend')
def resend():
  try:
    user_mail = session['email']
    code = randint(1000, 9999)
    sendMail(user_mail, code)
    session['code'] = createHash(str(code))
    session['code_created_at'] = int(time())
    session['code_attempts'] = 0
    return jsonify({'type': 'success', 'message': 'code resent successfully'}), 200
  except Exception as error:
    logging.error(error)
    return jsonify({'type': 'error', 'message': 'something went wrong'}), 500
  
@auth_bp.route('/logout')
def logout():
  try:
    session.clear()
    return jsonify({'type': 'success', 'message': 'user logged out'}), 200
  except Exception as error:
    logging.error(error)
    return jsonify({'type': 'error', 'message': 'something went wrong'}), 500