"""Write a method which takes 2 integers as arguments and A) returns the sum of them if both are positive or 
B) raises a ValueError exception if either of them are negative. 
Write unit tests to test the method with 100% coverage.
"""

def addition_method(number1:int, number2:int):
    """ add two number if both are positive integer else raise exception

    Args:
        number1 (int):
        number2 (int): 

    Raises:
        ValueError: 

    Returns:
        [int]: return addition of two number 
    """
    if number1 >0 and number2 > 0:
        return number1 + number2
    else:
        raise ValueError("Number is negative")


