import click

from app import create_app
from config import config

application = create_app(config)


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
