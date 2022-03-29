"""From the tasks done on Day 3, if a user provides area, find the length of perfect shapes (eg: circle, square)
"""
from __future__ import print_function

from builtins import input
from Shapes import circle,square,rectangle,triangle,pentagon,heptagon,hexagon,octagon

def main():
    try:
        shape_name = input("Enter name of the shape: ")
    except ValueError as e:
        print(e)
    else:
        try:
            area = float(input("Enter area: "))
        except ValueError as e:
            print(e)
        else:        
            if shape_name == 'circle':
                radius = circle.Circle.get_radius_from_area(area)
                print("Radius is {}".format(radius))
            elif shape_name == 'hexagon':
                side_length = hexagon.Hexagon.get_length_from_area(area)
                print("Side length is {}".format(side_length))
            elif shape_name == 'pentagon':
                side_length = pentagon.Pentagon.get_length_from_area(area)
                print("Side length is {}".format(side_length))
            elif shape_name == 'heptagon':
                side_length = heptagon.Heptagon.get_length_from_area(area)
                print("Side length is {}".format(side_length))                     
            elif shape_name == 'octagon':
                side_length = octagon.Octagon.get_length_from_area(area)
                print("Side length is {}".format(side_length))

if __name__ == "__main__":
    main()  