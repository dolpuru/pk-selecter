
"""
Application Factory Module
"""
from datetime import datetime
from flask import Flask
from flask.json import JSONEncoder
from app import api
# from app.api.controller_api import controller_bp
from app.api.views_api import views_bp


def create_app():
    app = Flask(__name__)
        # import_name=__name__,
        # instance_relative_config=True,
        # static_url_path='/',
        # static_folder='static_templates/',
        # template_folder='static_templates/'
    # )

    # app.json_encoder = CustomJSONEncoder
    # app.config.from_object(config)
    # config.init_app(app)
    # api.init_app(app)

    # app.register_blueprint(controller_bp)
    app.register_blueprint(views_bp,  url_prefix='/')
    return app
