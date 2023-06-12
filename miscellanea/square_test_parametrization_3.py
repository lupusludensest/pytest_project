# A simple tests with parametrized input
# Gurov Vic dt 27 Apr 2023, thu

import pytest

# Simple function that squares a number
def square(num):
    return num * num

# Our test is parametrized
@pytest.mark.parametrize("num", [1, 2, pytest.param(3, marks=pytest.mark.skip), 4, 5])
def test_square(num):
    result = square(num)
    assert result == num ** 2