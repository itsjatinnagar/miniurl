from functools import wraps
from flask import jsonify, request, session

from utils.token import tokenDecode

def session_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('address') is None or session.get('token') is None:
            return jsonify({'type': 'error', 'message': 'unauthorized'}), 401
        if session.get('address') != request.remote_addr:
            return jsonify({'type': 'error', 'message': 'unauthorized'}), 401
        request.data = tokenDecode(session.get('token'))
        return f(*args, **kwargs)
    return decorated_function