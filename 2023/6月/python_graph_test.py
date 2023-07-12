import pytest
from python_graph import circle,PI,rectangle,square

class Test_python_graph:
    def test_circle(self):
        assert circle(2) == 12.56
        assert circle(0) == 0
        with pytest.raises(ValueError):
            circle(-5)

    def test_rectangle(self):
        assert rectangle(5, 2) == 10
        assert rectangle(10, 5) == 50
        assert rectangle(0, 0) == 0
        with pytest.raises(ValueError):
            rectangle(-5,0)


    def test_square(self):
        assert square(2) == 4
        assert square(0) == 0
        with pytest.raises(ValueError):
            square(-5)