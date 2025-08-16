from flask import Flask
from .routes import main

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app

import logging

def create_app():
    app = Flask(__name__)

    # Basic logging setup
    logging.basicConfig(level=logging.INFO)
    app.logger.info("App started")

    app.register_blueprint(main)
    return app
