class TestClassOne(object):
    def test_one(self):
        x = "this"
        assert 't'in x

    def test_two(self):
        x = "hello"
        assert 'l' in x


class TestClassTwo(object):
    def test_one(self):
        x = "iphone"
        assert 'p'in x

    def test_two(self):
        x = "apple"
        assert 'b' not in x