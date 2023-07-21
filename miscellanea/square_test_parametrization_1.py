# A simple tests with parametrized input
# Gurov Vic dt 27 Apr 2023, thu

import pytest

# Simple function that squares a number
def square(num):
    return num * num

# Our test is parametrized
@pytest.mark.parametrize("num, ref", [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)])
def test_square(num, ref):
    result = square(num)
    assert result == ref