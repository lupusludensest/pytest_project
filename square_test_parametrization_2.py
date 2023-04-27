# A simple tests with parametrized input
# Gurov Vic dt 27 Apr 2023, thu

import pytest
import math

# Simple function that squares a number
def pow(base, exponent):
    return base ** exponent

# Our test is parametrized
@pytest.mark.parametrize("base", [1, 2, 3])
@pytest.mark.parametrize("exponent", [4, 5, 6])
def test_pow(base, exponent):
    # Test if our function matches math.pow
    result = pow(base, exponent)
    assert result == math.pow(base, exponent)