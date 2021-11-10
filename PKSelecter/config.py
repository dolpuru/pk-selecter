"""
Application Config Setting
"""
import os

APP_NAME = "PKSelect"


class Config:
    """General Config"""
    SLOW_API_TIME = 0.5
    API_LOGGING = False
    JSON_AS_ASCII = False

    @staticmethod
    def init_app(app):
        pass


class TestingConfig(Config):
    # test_config = dict(DEBUG=True, 
    # TESTING=True, 
    # ENV="=====TEST Mode=====")
    DEBUG=True, 
    TESTING=True, 
    ENV="=====TEST Mode====="


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    ENV = "==========helllo hjk develope========="


class ProductionConfig(Config):
    DEBUG = False
    TESTING = True
    ENV = "=====Production Mode====="


config_dict = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}

config = config_dict[os.getenv("FLASK_CONFIG") or "default"]
# print(config)
# # os.environ("FLASK_CONFIG") = "testing"
# os.getenv("FLASK_CONFIG") = "testing"
# print("flask_config :::::::::::", os.getenv("FLASK_CONFIG"))  # 1

if __name__ == "__main__":
    pass
