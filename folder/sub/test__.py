import unittest

class Test1(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("execute setUpClass")

    @classmethod
    def tearDownClass(self):
        print("execute tearDownClass ")

    def setUp(self):
        print("execute setUp")

    def tearDown(self):
        print("execute tearDown")

    def test_upper(self):
        print('execute test_upper ')
        self.assertTrue('FOO'.isupper())

    def test_lower(self):
        print('execute test_lower  ')
        self.assertTrue('foo'.islower())



if __name__ == '__main__':
    unittest.main(verbosity=2)