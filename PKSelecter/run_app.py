# from config import config, APP_NAME
import click
from PKSelecter.app import create_app

# from flask_cli import FlaskCLI
from PKSelecter.config import config


# app = Flask(__name__)

# @app.route('/')
# def helloWorld():
#     return 'Hello, World!'
application = create_app(config)
# application.run(port=80)


# @application.click.command()
# @application.click.option("--test", help="test of args")
# @application.click.argument("name")
# def test_(name):
#     print(name)


@application.cli.command("test_mode")
@click.argument("name")
def create(name):
    """Creates a user"""
    print("Create user: {}".format(name))
