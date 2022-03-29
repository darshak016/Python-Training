"""Write a program to convert a string value to integer and raise a custom exception
"""

class StringToIntError(Exception):
    def __init__(self, string) -> None:
        message = "invalid input {}".format(string)
        super().__init__(message)


def string_to_int(string):
    """function to convert string value into integer

    Args:
        string ([string]): take string as parameter 

    Raises:
        StringToIntError: custom error written as class

    Returns:
        [int]: return integer
    """
    temp = string
    if temp.isdecimal():
        number = int(string)
    else:
        raise StringToIntError(string)
    return number

    
    
