import logging
from flask import Blueprint, jsonify, request
from time import time

from database.links import createLink, readLinks
from decorators.auth import auth_required
from utils.generator import generateHash

link_bp = Blueprint('link_bp',__name__)

@link_bp.route('/shorten', methods=['POST'])
@auth_required
def shorten():
  try:
    uid = request.data['id']
    long_url = request.json['link']
    short_link = generateHash()
    created_at = int(time())
    lid = createLink(uid,short_link,long_url,created_at)
    return jsonify({'type': 'success', 'data': [{'id':lid,'long_url':long_url,'hash':short_link,'clicks':0,'created_at':created_at}]}), 200
  except Exception as error:
    logging.error(error)
    return jsonify({'type': 'error', 'message': 'something went wrong'}), 500

@link_bp.route('/links')
@auth_required
def fetchLinks():
  try:
    uid = request.data['id']
    links = readLinks(uid)
    data = [{'id':link['id'],'long_url':link['long_url'],'hash':link['hash'],'clicks':link['clicks'],'created_at':link['created_at']} for link in links]
    return jsonify({'type': 'success', 'data': data}), 200
  except Exception as error:
    logging.error(error)
    return jsonify({'type': 'error', 'message': 'something went wrong'}), 500
