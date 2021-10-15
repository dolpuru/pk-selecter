"""
Application Factory Module
"""
from flask import Flask

# from PKSelecter import config

# from app.api.controller_api import controller_bp
from .api.views_api import views_bp

from .api.controller_api import controller_bp

# production : debug = False, Testing = False,
# Testing : ENV로 구분 후 테스트.py 실행
# Develope : debug = True, 개발


def create_app(config):

    app = Flask(__name__, static_folder="./templates/", template_folder="./templates/")
    app.config.from_object(config)
    print(app.config["ENV"])
    app.register_blueprint(views_bp, url_prefix="/")
    app.register_blueprint(controller_bp, url_prefix="/")
    return app
