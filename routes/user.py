import logging
from flask import Blueprint,jsonify,request

from decorators.auth import session_auth

user_bp = Blueprint('user_bp',__name__)

@user_bp.route('/user', methods=['GET'])
@session_auth
def user():
    try:
        return jsonify({'type':'success', 'data': request.data}), 200
    except Exception as error:
        logging.error(error)
        return jsonify({'type': 'error', 'message': 'internal server error'}), 500