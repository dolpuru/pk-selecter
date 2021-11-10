import os
import unittest
import click
from flask.app import Flask

from app import create_app
from config import config
from config import config_dict


application = create_app(config_dict['development']) # FLASK_CONFIG or Devemode



"""development_mode"""
@application.cli.command("dev_mode")
@click.argument("name")
def development(name):

    # application.run(debug=True)
    print(
        "ENV : ", application.config["ENV"], "\n"
        "DEBUG : ", application.config["DEBUG"], "\n"
        "TESTING : ", application.config["TESTING"], "\n",
    )  
    print("mode: dev_mode, {}".format(name))


"""test_mode"""
@application.cli.command("test_mode")
@click.argument("test_names_tuple", nargs=-1)  # nargs -1 로 해야 문자열로 받음 아니면 문자로 받음
def test(test_names_tuple):

    """test_mode"""
    test_dir = "test"
    print(
        "application config, DEBUG, Testing\n",
        "ENV : ", application.config["ENV"], "\n"
        "DEBUG : ", application.config["DEBUG"], "\n"
        "TESTING : ", application.config["TESTING"], "\n",
    )  
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
    
