# A simple tests with parametrized input
# Gurov Vic dt 27 Apr 2023, thu

import pytest

# Simple function that squares a number
def square(num):
    return num * num

# Our test is parametrized
@pytest.mark.parametrize(
    "num",
    [
        pytest.param(-1, id = 'negative'),
        pytest.param(0, id = 'zero'),
        pytest.param(1, id = 'positive'),
    ],
)
def test_square(num):
    result = square(num)
    assert result == num ** 2