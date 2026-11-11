import pytest
from calc import (
    add,
    is_even,
    average
)


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_average():
    assert average([2, 4, 6]) == 4
    assert average([1, 2]) == pytest.approx(1,5)
    assert average([7]) == 7


def test_is_even_returning_none():
    assert is_even(None) == None


pytest.mark.parametrize(
    "n.exp",
    [
        (0, True),
        (4, True),
        (5, False)
    ]
)
def test_is_even(n, exp):
    assert is_even(n) == exp