from __future__ import print_function
from __future__ import division
import math
from shape import Shape


class Octagon(Shape):
        def __init__(self,side):
            """Initialize Octagon object

            Args:
                side length of Octagon ([int]):
            """
            self.side = side
            
        def perimeter(self):
            """Calculate perimeter of Octagon.

            Returns:
                Return perimeter of Octagon.
            """
            return self.side*8
        
        def area(self):
            """Calculate area of octagon.

            Returns:
                Return area of octagon.
            """
            return 8 * (self.side ** 2) / (4 * tan(PI / 8))
        
        def __repr__(self):
            """Represent object as a string

            Returns:
                Return String
            """
            return "Octagon: side {}".format(self.side) 
        
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
            
        @staticmethod    
        def get_length_from_area(area):
            """
            Args:
                area (_float_): 

            Returns:
                _type_: return side length of Octagon based on area
            """
            length = (area / 3.63 ) ** 0.5
            return length        