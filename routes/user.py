import logging
from flask import Blueprint, jsonify, request

from decorators.auth import auth_required

user_bp = Blueprint('user_bp',__name__)

@user_bp.route('/user')
@auth_required
def getUser():
  try:
    return jsonify({'type': 'success', 'data': request.data}), 200
  except Exception as error:
    logging.error(error)
    return jsonify({'type': 'error', 'message': 'something went wrong'}), 500