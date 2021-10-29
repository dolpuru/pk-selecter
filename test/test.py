# from PKSelecter.tests.mytest import Mytest
import unittest

# ta = unittest.TestLoader().loadTestsFromNames("Mytest")
# unittest.TextTestRunner(verbosity=1).run(ta)


tests = unittest.TestLoader().discover("./", pattern="m*.py")
print(tests)
print(type(tests))
unittest.TextTestRunner(verbosity=2).run(tests)
