import math
from handson1 import Shape


class Rectangle(Shape):
        def __init__(self,length,width):
            """Initialize Rectangle object

            Args:
                length and width of Rectangle ([int]):
            """
            self.width,self.length = width,length
            
        def perimeter(self):
            """Calculate perimeter of Rectangle.

            Returns:
                Return perimeter of Rectangle.
            """
            return 2*self.length + 2*self.width
        
        def area(self):
            """Calculate area of rectangle.

            Returns:
                Return area of rectangle.
            """
            return self.length*self.width
        
        def __repr__(self):
            """Represent object as a string

            Returns:
                Return String
            """
            return "Rectangle: Length {0}, Width {1}".format(self.length,self.width) 
        
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
            

class Triangle(Shape):
        def __init__(self,side1,side2,side3):
            """Initialize Triangle object

        Args:
            Three sides if Triangle ([int]):
        """
            self.side1,self.side2,self.side3 = side1,side2,side3
            
        def perimeter(self):
            """Calculate perimeter of Triangle.

            Returns:
                Return perimeter of Triangle.
            """
            return self.side1+self.side2+self.side3
        
        def area(self):
            """Calculate area of triangle.

            Returns:
                Return area of triangle.
            """
            s = self.perimeter() / 2
            triangle_area = (s*(s-self.side1)*(s-self.side2)*(s-self.side3))
            return triangle_area
        
        def __repr__(self):
            """Represent object as a string

            Returns:
                Return String
            """
            return "Triangle: side1 {0}, side2 {1},side3 {2}".format(self.side1,self.side2,self.side3) 
        
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