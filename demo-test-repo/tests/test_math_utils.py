from src.math_utils import add, average


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_average():
    assert average([1, 2, 3]) == 2
    assert average([10, 20]) == 15
