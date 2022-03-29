"""Write a method which returns the nth fibonacci number. Write a single, parameterized unit test to test the method.
"""

def fibonacci(n):
    """this function finds n'th fibonacci number

    Args:
        n ([int]): input parameter 

    Raises:
        ValueError: 

    Returns:
        [type]: return n'th fibonacci number
    """
    if n < 0:
        raise ValueError
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) 
    