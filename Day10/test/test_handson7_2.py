"""Write unit tests for the function created for Day-4 Hands-on with at least 2-3 different scenarios for each question.
Question no. - 6, 7, 8 & 9.

______________Question 7____________-

Write a python program to find Urls from a given string
"""

import pytest
from demo.handson7_2 import find_url

def test_get_url_from_string():
    """test the url given in the string
    """
    expected_out = ['https://google.com']
    assert find_url("this is https://google.com") == expected_out
    
def test_failed_to_get_url_from_string():
    """test the url given in the string
    """
    expected_out = []
    assert find_url("There is no url in this string") == expected_out    