from __future__ import print_function
from __future__ import division
import math
from shape import Shape


class Square(Shape):
        def __init__(self,side):
            """Initialize Square object

        Args:
            side of Square ([int]):
        """
            self.side = side
            
        def perimeter(self):
            """Calculate perimeter of Square.

            Returns:
                Return perimeter of Square.
            """
            return 4*self.side
        
        def area(self):
            """Calculate area of Square.

            Returns:
                Return area of square.
            """
            return self.side**2
        
        def __repr__(self):
            """Represent object as a string

            Returns:
                Return String
            """
            return "Square: {}".format(self.side) 
        
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
                _type_: return side length of Heptagon based on area
            """
            length = area ** 0.5
            return length         
