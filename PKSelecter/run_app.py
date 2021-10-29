import click
import unittest
from tests.mytest import MyTest
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
@click.argument("name",  nargs=-1) #nargs -1 로 해야 문자열로 받음 아니면 문자로 받음
def test(name):
    """test_mode"""
    print("mode: test_mode, test_name :  {}".format(name))
    ta = unittest.TestLoader().loadTestsFromNames('tests/' + name)
    unittest.TextTestRunner(verbosity=1).run(ta)