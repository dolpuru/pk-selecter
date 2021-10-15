# from config import config, APP_NAME
from app import create_app
from config import config

application = create_app(config)
application.run(port=80)
