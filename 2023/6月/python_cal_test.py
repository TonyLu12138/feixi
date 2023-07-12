import pytest
from python_cal import add, sub, mul, div

class Test_python_cal:
    def test_add(self):
        assert add(2, 3) == 5
        assert add(0, 0) == 0
        assert add(-5, 5) == 0

    def test_sub(self):
        assert sub(5, 2) == 3
        assert sub(10, 5) == 5
        assert sub(0, 0) == 0

    def test_mul(self):
        assert mul(2, 3) == 6
        assert mul(0, 5) == 0
        assert mul(-4, 3) == -12

    def test_div(self):
        assert div(10, 2) == 5
        assert div(-10, 3) == -3.3333333333333335