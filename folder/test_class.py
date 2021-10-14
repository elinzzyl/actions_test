class TestClassOne(unittest.TestCase):
    def test_one(self):
        x = "this"
        assert 't'in x

    def test_two(self):
        x = "hello"
        assert 'l' in x


class TestClassTwo(unittest.TestCase):
    def test_one(self):
        x = "iphone"
        assert 'p'in x

    def test_two(self):
        x = "apple"
        assert 'b' not in x

if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)        