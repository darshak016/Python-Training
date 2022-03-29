"""Write unit tests for the function created for Day-4 Hands-on with at least 2-3 different scenarios for each question.
Question no. - 6, 7, 8 & 9.

____________Q7_______________
Write a program to convert a string value to integer and raise a custom exception
"""

import pytest
from demo.handson7_1 import *


@pytest.mark.parametrize("input_string, result", [("20", 20), ("-50", -50)])
def test_string_to_int(input_string, result):
    """Test with given string 

    Args:
        input_string ([string]): 
        result ([int]): 
    """
    assert string_to_int(input_string) == result


def test_string_to_int_with_exception():
    """"It will test 'string_to_int' Function with wrong input type.
    """
    with pytest.raises(StringToIntError):
        assert string_to_int("string") == 180