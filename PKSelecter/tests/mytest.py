import unittest
from app import create_app
from config import config_dict as config

class MyTest(unittest.TestCase):


    def runTest(self):
        self.assertEqual(1, 1)