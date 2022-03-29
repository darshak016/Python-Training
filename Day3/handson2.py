"""Create classes: Circle, Square, Rectangle, Triangle, Pentagon, Hexagon, Heptagon, Octagon as 
child classes of Shape. These classes should have functions to calculate perimeter, area, 
description about the shape and comparison with another shape based on area or perimeter. 
For eg: there is an object of Circle with x area and object of Heptagon with y area, 
a function should tell which object has a larger area.
"""
import math
from handson1 import Shape

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
            Return true if area of current obj is greater
        """
        if self.area() > other.area():
            return True
        else:
            return False
        
        
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
            
         
            