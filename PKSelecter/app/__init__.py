
"""
Application Factory Module
"""
from datetime import datetime
from flask import Flask
from flask.json import JSONEncoder
from app import api
from app.api.main import main_bp
from app.api.view import template_bp


def create_app(config):
    app = Flask(
        import_name=__name__,
        instance_relative_config=True,
        # static_url_path='/',
        static_folder='view/template/',
        template_folder='view/template/'
    )

    # app.json_encoder = CustomJSONEncoder
    # app.config.from_object(config)
    # config.init_app(app)
    # api.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(template_bp)
    return app
