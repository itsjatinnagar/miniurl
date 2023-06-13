import logging
from datetime import datetime
from flask import Blueprint,jsonify,request

from database.links import insertLink,readAllLinks
from decorators.auth import session_auth
from utils.verificationCode import generateLinkHash

link_bp = Blueprint('link_bp',__name__)

@link_bp.route('/shorten', methods=['POST'])
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

@link_bp.route('/links', methods=['GET'])
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