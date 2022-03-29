from __future__ import print_function
from __future__ import division
import math
from shape import Shape


class Hexagon(Shape):
        def __init__(self,side):
            """Initialize Hexagon object

            Args:
                side length of Hexagon ([int]):
            """
            self.side = side
            
        def perimeter(self):
            """Calculate perimeter of Hexagon.

            Returns:
                Return perimeter of Hexagon.
            """
            return self.side*6
        
        def area(self):
            """Calculate area of hexagon.

            Returns:
                Return area of hexagon.
            """
            return ((3 * math.sqrt(3) * 
            (self.side * self.side)) / 2)
        
        def __repr__(self):
            """Represent object as a string

            Returns:
                Return String
            """
            return "Hexagon: side {}".format(self.side) 
        
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
                _type_: return side length of Hexagon based on area
            """
            length = (area / 3.63 ) ** 0.5
            return length        