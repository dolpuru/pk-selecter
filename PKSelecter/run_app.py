# from config import config, APP_NAME
from app import create_app


application = create_app()
application.run( port = 80)