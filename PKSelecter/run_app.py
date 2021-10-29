import click
import unittest

# from tests import mytest
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
@click.argument("test_names_tuple", nargs=-1)  # nargs -1 로 해야 문자열로 받음 아니면 문자로 받음
def test(test_names_tuple):
    """test_mode"""
    test_dir = "test"

    try:
        if test_names_tuple:
            for index in range(len(test_names_tuple)):
                print("mode: test_mode, test_name :  {}".format(test_names_tuple))
                name_to_test_suite = unittest.TestLoader().discover(
                    test_dir, test_names_tuple[index]
                )
                print(type(name_to_test_suite))
                unittest.TextTestRunner(verbosity=1).run(name_to_test_suite)
        else:
            raise ValueError

    except ValueError:
        print("Error, you must be 'flask test_mode a.py b.py ...' ")
