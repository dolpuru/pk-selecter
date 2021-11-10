import os
from os import path as environ
import unittest
import click
from flask.app import Flask
from flask.cli import FlaskGroup

from app import create_app
from config import config
from config import config_dict


application = create_app(config) # FLASK_CONFIG or Devemode
print(os.getenv("FLASK_CONFIG"))

"""development_mode"""
# @application.cli.command("dev_mode")
# @click.argument("name", nargs=-1)
# def development(name):
    
#     application = create_app(config_dict['development'])

#     print(
#         "ENV : ", application.config["ENV"], "\n"
#         "DEBUG : ", application.config["DEBUG"], "\n"
#         "TESTING : ", application.config["TESTING"], "\n",
#     )  
#     print("mode: dev_mode, {}".format(name))
    
#     application.run()



"""test_mode"""
@application.cli.command("test_mode")
@click.argument("test_names_tuple", nargs=-1)  # nargs -1 로 해야 문자열로 받음 아니면 문자로 받음
def test(test_names_tuple):

    application = create_app(config_dict['testing'])
    test_dir = "test"
    print(
         application.config["ENV"],
        "|- - - Config Check - - - -|\n"
        " |- - - DEBUG : ", application.config["DEBUG"], "- - -|"
        "\n |- - - TESTING : ", application.config["TESTING"], " - -|"
        "\n ┗ - - - - - - - - - - - - -┛\n"
    )  
    try:
        # tests에 없는 요소가 들어오면 에러처리
        if test_names_tuple:
            for index in range(len(test_names_tuple)):
                print(">>> mode: test_mode \n>>> test name : '{}'".format(test_names_tuple[index]))
                name_to_test_suite = unittest.TestLoader().discover(
                    test_dir, test_names_tuple[index]
                )
                unittest.TextTestRunner(verbosity=1).run(name_to_test_suite)
        else:
            raise ValueError

    
    except ValueError:
        print("Error, you must be 'flask test_mode a.py b.py ...' ")
    

