from flask import jsonify, request, session
from functools import wraps

def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print("🐍 File: decorators/auth_decorator.py | Line: 7 | decorated_function ~ session",session)
        if session.get('address') is None or session.get('user') is None:
            return jsonify({'type': 'error', 'message': 'user not logged in', 'status': 401})
        if session.get('address') != request.remote_addr:
            return jsonify({'type': 'error', 'message': 'unauthorized', 'status': 401})
        setattr(request, "user", session['user'])
        return f(*args, **kwargs)
    return decorated_function