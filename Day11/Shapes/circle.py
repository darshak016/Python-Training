from __future__ import print_function
from __future__ import division
import math
from shape import Shape

class Circle(Shape):
    global PI
    PI = 3.14
    
    def __init__(self,radius):
        """Initialize Circle object

        Args:
            radius ([int]):
        """
        self.radius = radius
       
    def perimeter(self):
        """Calculate perimeter of Circle.

        Returns:
            Return perimeter of Circle.
        """
        return 2*PI*self.radius
    
    def area(self):
        """Calculate area of Circle.

        Returns:
            Return area of Circle
        """
        return PI*(self.radius**2)    
    
    def __repr__(self):
        """Represent object as a string

        Returns:
            REturn String
        """
        return "Radius: {}".format(self.radius)
    
    def __gt__(self,other):
        """Compare area of current object with other object.

        Args:
            other ([type]): [description]

        Returns:
            Return true if current obj is greater
        """
        if self.area() > other.area():
            return True
        else:
            return False
        
    @staticmethod    
    def get_radius_from_area(area):
        """_summary_

        Args:
            area (_float_): 

        Returns:
            _type_: return radius of circle based on area
        """
        radius = (area / PI ) ** 0.5
        return radius    