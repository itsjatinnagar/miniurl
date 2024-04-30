import logging
from flask import Blueprint, jsonify, request
from time import time

from database.links import readLongLink, updateLink
from database.analytics import insertAnalytic

misc_bp = Blueprint('misc_bp',__name__)

@misc_bp.route('/<string:hash>')
def redirect(hash):
  try:
    result = readLongLink(hash)
    if result is None:
      return jsonify({'type': 'error', 'message': 'link does not exists'}), 404
    updateLink(result['id'], int(result['clicks'])+1)
    insertAnalytic(result['id'], str(request.user_agent), int(time()))
    return redirect(result['long_link'])
  except Exception as error:
    logging.error(error)
    return jsonify({'type': 'error', 'message': 'something went wrong'}), 500