import unittest


class MyTest(unittest.TestCase):
    def runTest(self):
        self.assertEqual(1, 1)


class MyTest2(unittest.TestCase):
    def runTest(self):
        self.assertEqual(1, 1)


# ta = unittest.TestLoader().loadTestsFromTestCase(MyTest)
ta = unittest.TestLoader().loadTestsFromNames([MyTest, MyTest2])
unittest.TextTestRunner(verbosity=1).run(ta)
