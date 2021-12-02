# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

import math

class Rectangle():
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length*self.width
    
    def perimeter(self):
        return 2*(self.length + self.width)

class Circle():
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi*self.radius*self.radius
    
    def perimeter(self):
        return 2*math.pi*self.radius

unit_circle = Circle(1)
unit_square = Rectangle(1,1)

print(unit_circle.area())
print(unit_circle.perimeter())

print(unit_square.area())
print(unit_square.perimeter())