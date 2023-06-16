import logging
import os
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, request, redirect, url_for

from database.links import readRedirectLink, updateLinkClicks
from database.analytics import insertAgent
from routes.auth import auth_bp
from routes.links import link_bp
from routes.user import user_bp

load_dotenv()

app = Flask(__name__, static_folder='app', static_url_path="/")
app.config['SECRET_KEY'] = os.environ['SESSION_KEY']
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_SAMESITE='Strict'
)
app.register_blueprint(auth_bp)
app.register_blueprint(link_bp)
app.register_blueprint(user_bp)

@app.route('/')
def index():
    return app.send_static_file("index.html")

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.route('/manifest.json')
def manifest():
    return app.send_static_file('manifest.json')
    
@app.route('/icon192.png')
def icon192():
    return app.send_static_file('icon192.png')
    
@app.route('/icon512.png')
def icon512():
    return app.send_static_file('icon512.png')

@app.route('/<string:hash>', methods=['GET'])
def redirectOriginal(hash):
    try:
        result = readRedirectLink(hash)
        if result is None:
            return redirect(url_for('index'),404)

        updateLinkClicks(result[0], int(result[2]) + 1)
        insertAgent(result[0], str(request.user_agent), int(datetime.now().timestamp()))
        return redirect(result[1])
    except Exception as error:
        logging.error(error)
        return redirect(url_for('index'),500)