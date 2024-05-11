import os
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from routes.auth import auth_bp
from routes.link import link_bp
from routes.misc import misc_bp
from routes.user import user_bp

app = Flask(__name__, static_folder='app', static_url_path='/')
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=3)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

app.config.update(
  SESSION_COOKIE_SECURE=True,
  SESSION_COOKIE_SAMESITE='Strict'
)

app.register_blueprint(auth_bp)
app.register_blueprint(link_bp)
app.register_blueprint(misc_bp)
app.register_blueprint(user_bp)

@app.route('/')
def index():
  return app.send_static_file("index.html")

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')