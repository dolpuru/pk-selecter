import click
import unittest
import os

# from tests import mytest
from app import create_app

from config import config
from config import config_dict


application = create_app(config)


@application.cli.command("dev_mode")
@click.argument("name")
def develope(name):
    """develope_mode"""
    print("mode: dev_mode, {}".format(name))
    a = config_dict["testing"]
    print(a.test_config)
    # print("Aaaaaaaaaa", config_dict["testing"])
    # print("bbbbbbbbbb", config_dict["testing"].test_config)
    application.config.update(config_dict["testing"].test_config)
    # application.debug = True
    # application.testing = False

    application.run()


@application.cli.command("production_mode")
@click.argument("name")
def production(name):
    """production_mode"""
    print("mode: production_mode, {}".format(name))


@application.cli.command("test_mode")
@click.argument("test_names_tuple", nargs=-1)  # nargs -1 로 해야 문자열로 받음 아니면 문자로 받음
def test(test_names_tuple):
    os.environ["FLASK_CONFIG"] = "testing"
    print("flask_config in run_app.py", os.getenv("FLASK_CONFIG"))  # 3
    """test_mode"""
    test_dir = "test"
    print(
        "application config, DEBUG, Testing",
        application.config["ENV"],
        application.config["DEBUG"],
        application.config["TESTING"],
    )  # 4
    try:
        if test_names_tuple:
            for index in range(len(test_names_tuple)):
                print("mode: test_mode, test_name :  {}".format(test_names_tuple))
                name_to_test_suite = unittest.TestLoader().discover(
                    test_dir, test_names_tuple[index]
                )
                print(type(name_to_test_suite))  # 5
                unittest.TextTestRunner(verbosity=1).run(name_to_test_suite)
        else:
            raise ValueError

    except ValueError:
        print("Error, you must be 'flask test_mode a.py b.py ...' ")
