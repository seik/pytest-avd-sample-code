import pytest


class TestClass(object):
    def test_one(self):
        x = "this"
        assert "h" in x


class TestClassSetUp(object):
    @classmethod
    def setup_class(cls):
        cls.one = 1

    def test_one(self):
        x = self.one
        assert x == 1


class TestClassFixture(object):
    @pytest.fixture
    def one(self):
        return 1

    def test_one(self, one):
        assert one == 1
