"""
Application Config Setting
"""
import os

# from logging.config import dictConfig

# from dotenv import load_dotenv

# load_dotenv(verbose=True)

APP_NAME = "PKSelect"
# BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """General Config"""

    SLOW_API_TIME = 0.5
    API_LOGGING = False
    JSON_AS_ASCII = False

    @staticmethod
    def init_app(app):
        pass


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    ENV = "=====TEST Mode====="


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    ENV = "=====Development Mode====="


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    ENV = "=====Production Mode====="

    # @staticmethod
    # def init_app(app):
    #     '''logging'''
    #     dictConfig({
    #         'version': 1,
    #         'formatters': {
    #             'default': {
    #                 'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    #             }
    #         },
    #         'handlers': {
    #             'file': {
    #                 'level': 'WARNING',
    #                 'class': 'logging.handlers.RotatingFileHandler',
    #                 'filename': os.getenv(APP_NAME + '_ERROR_LOG_PATH') or './server.error.log',
    #                 'maxBytes': 1024 * 1024 * 5,
    #                 'backupCount': 5,
    #                 'formatter': 'default',
    #             },
    #         },
    #         'root': {
    #             'level': 'WARNING',
    #             'handlers': ['file']
    #         }
    #     })


config_dict = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}

config = config_dict["testing"]


if __name__ == "__main__":
    pass
