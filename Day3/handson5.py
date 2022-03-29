"""In task 2, implement function to compare two shape's perimeter and area based on length/breadth of the shape. 
Add validations on the input taken from user.
"""
import math
from handson2 import Shape
from Shape import square,rectangle,triangle,pentagon,heptagon,hexagon,octagon

class Circle(Shape):
    global PI
    PI = 3.14
    
    def __init__(self,radius):
        """Initialize Circle object

        Args:
            radius ([int]):
        """
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
        
    def compare_shape(self):
            """This function compare perimeter and area of circle with other shapes
            """
            shape_type = input("Enter type of shape to compare with circle: ")
            
            if shape_type == 'circle':
                try:
                    new_radius = int(input("Enter radius of circle: "))
                except ValueError:
                    print("Enter valid value")
                    return    
                obj_circle = Circle(new_radius)
                if self.area() == obj_circle.area():
                    print("Both shape have same area")
                else:
                    print("area of both shape is different")
                
                if self.perimeter() == obj_circle.perimeter():
                    print("Both shape have same perimeter")
                else:
                    print("perimeter of both shape is different")        
        
            elif shape_type == 'square':
                try:
                    new_side = int(input("Enter length of square side: "))
                except ValueError:
                    print("Enter valid value")
                    return    
                obj_square = Square(new_side)
                if self.area() == obj_square.area():
                    print("Both shape have same area")
                else:
                    print("area of both shape is different")
                
                if self.perimeter() == obj_square.perimeter():
                    print("Both shape have same perimeter")
                else:
                    print("perimeter of both shape is different")
            
            elif shape_type == 'rectangle':
                try:
                    new_length = int(input("Enter length of rectangle: "))
                    new_width = int(input("Enter width of rectangle: "))
                except ValueError:
                    print("Enter valid value")
                    return    
                obj_rectangle = rectangle.Rectangle(new_length, new_width)
                if self.area() == obj_rectangle.area():
                    print("Both shape have same area")
                else:
                    print("area of both shape is different")
                
                if self.perimeter() == obj_rectangle.perimeter():
                    print("Both shape have same perimeter")
                else:
                    print("perimeter of both shape is different")
        
            elif shape_type == 'triangle':
                try:
                    new_side1 = int(input("Enter side1 of triangle: "))
                    new_side2 = int(input("Enter side2 of triangle: "))
                    new_side3 = int(input("Enter side3 of triangle: "))
                except ValueError:
                    print("Enter valid value")
                    return    
                obj_triangle = triangle.Triangle(new_side1, new_side2, new_side3)
                if self.area() == obj_triangle.area():
                    print("Both shape have same area")
                else:
                    print("area of both shape is different")
                
                if self.perimeter() == obj_triangle.perimeter():
                    print("Both shape have same perimeter")
                else:
                    print("perimeter of both shape is different")
                    
            elif shape_type == 'pentagon':
                try:
                    new_side = int(input("Enter side of Pentagon: "))
                 
                except ValueError:
                    print("Enter valid value")
                    return    
                obj_pentagon = pentagon.Pentagon(new_side)
                if self.area() == obj_pentagon.area():
                    print("Both shape have same area")
                else:
                    print("area of both shape is different")
                
                if self.perimeter() == obj_pentagon.perimeter():
                    print("Both shape have same perimeter")
                else:
                    print("perimeter of both shape is different")
                    
            elif shape_type == 'hexagon':
                try:
                    new_side = int(input("Enter side of hexagon: "))
                 
                except ValueError:
                    print("Enter valid value")
                    return    
                obj_hexagon = hexagon.Hexagon(new_side)
                if self.area() == obj_hexagon.area():
                    print("Both shape have same area")
                else:
                    print("area of both shape is different")
                
                if self.perimeter() == obj_triangle.perimeter():
                    print("Both shape have same perimeter")
                else:
                    print("perimeter of both shape is different") 
                    
            elif shape_type == 'heptagon':
                try:
                    new_side = int(input("Enter side of heptagon: "))
                 
                except ValueError:
                    print("Enter valid value")
                    return    
                obj_heptagon = heptagon.Heptagon(new_side)
                if self.area() == obj_heptagon.area():
                    print("Both shape have same area")
                else:
                    print("area of both shape is different")
                
                if self.perimeter() == obj_heptagon.perimeter():
                    print("Both shape have same perimeter")
                else:
                    print("perimeter of both shape is different")  
                                         
            else: 
    
                try:
                    new_side = int(input("Enter side of octagon: "))
                 
                except ValueError:
                    print("Enter valid value")
                    return    
                obj_octagon = octagon.Octagon(new_side)
                if self.area() == obj_octagon.area():
                    print("Both shape have same area")
                else:
                    print("area of both shape is different")
                
                if self.perimeter() == obj_octagon.perimeter():
                    print("Both shape have same perimeter")
                else:
                    print("perimeter of both shape is different")

def main():
    obj1 = Circle(5)
    obj1.compare_shape()
       
if __name__ == '__main__':
    main()