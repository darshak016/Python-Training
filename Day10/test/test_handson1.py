"""Write a method which takes 2 integers as arguments and A) returns the sum of them if both are positive or B) 
raises a ValueError exception if either of them are negative. 
Write unit tests to test the method with 100% coverage.
"""

import pytest
from demo.handson1 import addition_method

def test_addition_method():
    """Test addition of two positive number with given input
    """
    assert addition_method(10, 10) == 20

def test_negative():
    """Test addition of one or two negative number with given input
    """
    with pytest.raises(ValueError):
        assert addition_method(-10, 10) == 20