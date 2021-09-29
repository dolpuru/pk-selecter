
"""
Application Factory Module
"""
from flask import Flask
# from app.api.controller_api import controller_bp
from .api.views_api import views_bp


def create_app():
    app = Flask(__name__,
        static_folder='./templates/',
        template_folder='./templates/')
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

    # app.register_blueprint(controller_bp)r
    app.register_blueprint(views_bp,  url_prefix='/')
    return app
