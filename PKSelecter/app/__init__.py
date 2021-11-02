"""
Application Factory Module
"""
from logging import DEBUG, debug
from flask import Flask

# from PKSelecter import config

# from app.api.controller_api import controller_bp
from .api.views_api import views_bp

from .api.controller_api import controller_bp

# production : debug = False, Testing = False,
# Testing : ENV로 구분 후 테스트.py 실행
# Develope : debug = True, 개발


def create_app(config):

    app = Flask(
        import_name=__name__, static_folder="./static/", template_folder="./static/"
    )
    # a = (DEBUG=true)
    app.config.update(DEBUG=True, TESTING=False)
    # config.init_app(app)

    print("app.config in __init__.py", app.config["ENV"])  # 2

    app.register_blueprint(views_bp, url_prefix="/")
    app.register_blueprint(controller_bp, url_prefix="/")
    return app
