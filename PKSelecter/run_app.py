# from config import config, APP_NAME
import click
from app import create_app

# from flask_cli import FlaskCLI
from config import config


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
@application.cli.command("dev_mode")
@click.argument("name")
def develope(name):
    """develope_mode"""
    print("mode: dev_mode, {}".format(name))


@application.cli.command("production_mode")
@click.argument("name")
def production(name):
    """production_mode"""
    print("mode: production_mode, {}".format(name))


@application.cli.command("test_mode")
@click.argument("name")
def test(name):
    """test_mode"""
    print("mode: test_mode, {}".format(name))
