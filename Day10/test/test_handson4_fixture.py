"""Modify the tests from the second exercise so that only one instance of Account is used across all tests using fixtures.
"""

import pytest
from demo.handson2 import Account

@pytest.fixture
def obj():
    """This is fixture that initialize object of Account class

    Returns:
        [object]: 
    """
    return Account(1000) 

def test_add_amount(obj):
    """Test amount addition functionality 

    Args:
        obj ([object]):
    """
    assert obj.add(20) == 1020
 
def test_add_negative_amount(obj):
    """Test negative amount addition functionality  

    Args:
        obj ([object]): 
    """
    with pytest.raises(ValueError):
        assert obj.add(-20) == 1000    
    
def test_subtract(obj):
    """Test amount withdrawal functionality 

    Args:
        obj ([object]): 
    """
    assert obj.subtract(20) == 980
  
def test_subtract_negative_amount(obj):
    """Test negative amount withdrawal functionality 

    Args:
        obj ([object]): 
    """
    with pytest.raises(ValueError):
        assert obj.subtract(-20) == 1000     
    
def test_subtract_with_insufficient_balance(obj):
    """Test amount withdrawal functionality when balance is insufficient 

    Args:
        obj ([object])
    """
    with pytest.raises(ValueError):
        assert obj.subtract(2000) == 1000           