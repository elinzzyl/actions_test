import unittest

class Test1(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("execute setUpClass")

    @classmethod
    def tearDownClass(self):
        print("execute tearDownClass")

    def setUp(self):
        print("execute setUp")

    def tearDown(self):
        print("execute tearDown")

    def test_one(self):
        print('execute test_one')
        self.assertTrue('FOO'.isupper())

    def test_two(self):
        print('execute test_two')
        self.assertTrue('foo'.islower())



if __name__ == '__main__':
    unittest.main(verbosity=2)