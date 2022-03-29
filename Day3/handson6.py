from handson1 import Shape
import sys

class Circle(Shape):
    global PI
    PI = 3.14
    
    def __init__(self,radius = 2):
        """Initialize Circle object and take argument from command line

        Args:
            radius ([int]):
        """
        if len(sys.arg) == 1:
            try:
                self.radius = sys.argv[1]
                
            except ValueError:
                print("Enter Valid value")    
                
        else:
            self.radius = radius    
        
    def __del__(self):
        """all references to the object have been deleted
        """
        print("Object deleted")
            
       
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
            Return true if area of current obj is greater
        """
        if self.area() > other.area():
            return True
        else:
            return False
