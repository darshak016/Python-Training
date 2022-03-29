import math
from handson1 import Shape


class Pentagon(Shape):
        def __init__(self,side):
            """Initialize Pentagon object

            Args:
                side length of Pentagon ([int]):
            """
            self.side = side
            
        def perimeter(self):
            """Calculate perimeter of Pentagon.

            Returns:
                Return perimeter of Pentagon.
            """
            return self.side*5
        
        def area(self):
            """Calculate area of pentagon.

            Returns:
                Return area of pentagon.
            """
            return (sqrt(5 * (5 + 2 *
           (sqrt(5)))) * self.side * self.side) / 4
        
        def __repr__(self):
            """Represent object as a string

            Returns:
                Return String
            """
            return "Pentagon: side {}".format(self.side) 
        
        def __gt__(self,other):
            """Compare area of current object with other object.

            Args:
                other ([type]): [description]

            Returns:
                Return true if area of current obj is greater
            """
            if self.area() > other.area():
                return True
            else:
                return False