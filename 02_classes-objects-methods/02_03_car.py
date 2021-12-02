# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class Car():
    
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed
    
    def __str__(self):
        my_str = f"Model: {self.model}, Year: {self.year}, Max Speed: {self.max_speed}"
        return my_str
    
    def more_speed(self):
        self.max_speed += 5

a = Car(1, 1982, 50)
b = Car(7, 2013, 140)

print(a)
print(b)

a.more_speed()
print(a)