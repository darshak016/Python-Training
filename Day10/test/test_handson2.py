"""Create a class `Account` with an int attribute `balance` and two methods add, 
and subtract which only take a single positive integer as an argument and respectively adds or subtracts them from 
he balance or raises ValueError if the balance is not sufficient. Write unit tests to test all the methods with 100% coverage.
"""

import pytest
from demo.handson2 import Account

def test_add_amount():
    """Test add balance in account.
    """
    obj1 = Account(0)
    assert obj1.add(20) == 20

def test_sub_amount():
    """Test withdrawl of balance in account
    """
    obj1 = Account(0)
    with pytest.raises(ValueError):
        assert obj1.subtract(20) == 0
    
def test_negative():
    """Test withdrawl of balance in account
    """
    obj1 = Account(100)
    assert obj1.subtract(20) == 80