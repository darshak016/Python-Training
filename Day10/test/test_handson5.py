"""Modify the first exercise to print a message before and after the execution of each individual test.
"""

import pytest
from demo.handson1 import addition_method

def test_addition():
    """Test addition of two positive number with given input
    """
    print("__This is the test_addition function__")
    assert addition_method(10, 10) == 20

def test_negative_number():
    """test addition of one or two negative number with given input
    """
    print("__This is the test_negative_number function__")
    with pytest.raises(ValueError):
        assert addition_method(-10, 10) == 20