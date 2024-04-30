from flask import jsonify, request, session
from functools import wraps

def auth_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if session.get('address') is None or session.get('user') is None:
      return jsonify({'type': 'error', 'message': 'user not logged in'}), 401
    if session.get('address') != request.remote_addr:
      return jsonify({'type': 'error', 'message': 'unauthorized'}), 401
    request.data = session.get('user')
    return f(*args, **kwargs)
  return decorated_function
