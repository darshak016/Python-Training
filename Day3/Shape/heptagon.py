import math
from handson1 import Shape


class Heptagon(Shape):
        def __init__(self,side):
            """Initialize Heptagon object

            Args:
                side length of Heptagon ([int]):
            """
            self.side = side
            
        def perimeter(self):
            """Calculate perimeter of Heptagon.

            Returns:
                Return perimeter of Heptagon.
            """
            return self.side*7
        
        def area(self):
            """Calculate area of heptagon.

            Returns:
                Return area of heptagon.
            """
            return 7 * (self.side ** 2) / (4 * tan(PI / 7))
        
        def __repr__(self):
            """Represent object as a string

            Returns:
                Return String
            """
            return "Heptagon: side {}".format(self.side) 
        
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