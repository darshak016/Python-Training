"""Write a method which returns the nth fibonacci number. Write a single, parameterized unit test to test the method.
"""

import pytest
from demo.handson3 import fibonacci

@pytest.mark.parametrize("test_input, expected_output",
                         [
                             (4,2),
                             (10,34),
                             (7,8)
                         ])
def test_fibonacci(test_input, expected_output):
    assert fibonacci(test_input) == expected_output
    
def test_fibonacci_error():
    with pytest.raises(ValueError):
        fibonacci(-10)    