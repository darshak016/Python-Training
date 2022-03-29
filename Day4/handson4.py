"""Write a program that takes integer age from the user if age is under 18, 
raise custom exception UnderAgeError and if age is over 40, raise custom exception OverAgeError
"""

class UnderAgeError(Exception):
    """ This Exception class called when age is under 18"""
    def __init__(self,age:int):
        """Print Error

        Args:
            age (int): [description]
        """
        self.age = age
        self.message = "You are Under Age by {} years..!!"
        super().__init__(self.message.format(18 - self.age))

class OverAgeError(Exception):
    """Print Error

    Args:
        Exception ([type]): [description]
    """
    def __init__(self,age:int):
        self.age = age
        self.message = "You are Over Age by {} years..!!"
        super().__init__(self.message.format(self.age - 18))

try:
    age = int(input("Enter age: "))
    if age > 18:
        raise OverAgeError(age)
    else:
        raise UnderAgeError(age)
    
except ValueError as e:
    print(e.args[0])
        