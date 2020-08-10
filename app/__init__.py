from flask import Flask
from flask_wtf.csrf import CSRFProtect
from .config import Config


def create_app():
    app = Flask(__name__)
    CSRFProtect(app)
    app.config.from_object(Config)

    return app
