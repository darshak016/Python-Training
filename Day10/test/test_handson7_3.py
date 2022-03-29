"""Write unit tests for the function created for Day-4 Hands-on with at least 2-3 different scenarios for each question.
Question no. - 6, 7, 8 & 9.

___________-Question 8_______________

Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format

"""

import pytest
from demo.handson7_3 import convert_date


@pytest.mark.parametrize("test_input, expected_output",
                         [
                             ("2000-09-16","16-09-2000"),
                             ("2005-10-16","16-10-2005")
                         ])
def test_convert_date(test_input, expected_output):
    """using given parameter test the function

    Args:
        test_input ([string]): parameter given to function convert_Date
        expected_output ([string]): 
    """
    assert convert_date(test_input) == expected_output    