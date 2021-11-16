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
    DEBUG=False
    TESTING=True
    ENV="\n>>>>> THIS IS TESTING MODE <<<<<\n"


class DevelopmentConfig(Config):
    DEBUG=True
    TESTING=False


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
}

config = config_dict[os.getenv("FLASK_CONFIG") or "default"]
# print(os.getenv("FLASK_CONFIG"))
if __name__ == "__main__":
    pass
