# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

import random

class Kettle():
    
    def __init__(self, material, min_capacity, max_capacity):
        self.material = material
        self.min_capacity = min_capacity
        self.max_capacity = max_capacity
    
    def __str__(self):
        my_str = (f"Material: {self.material}\n"
            f"Minimum Capacity: {self.min_capacity}\n"
            f"Maximum Capacity: {self.max_capacity}")
        return my_str
    
    def __add__(self, other):
        if self.material == other.material:
            added_material = self.material
        else:
            added_material = self.material + " & " + other.material
        return Kettle(added_material, min(self.min_capacity, other.min_capacity), self.max_capacity + other.max_capacity)

first_kettle = Kettle("copper", 100, 500)
second_kettle = Kettle("iron", 50, 300)
third_kettle = Kettle("copper", 75, 1000)

print(first_kettle)
print(first_kettle + second_kettle)
print(first_kettle + third_kettle)

class Dog():
    
    def __init__(self, breed, sex, color):
        self.breed = breed
        self.sex = sex
        self.color = color
    
    def __str__(self):
        return f"This {self.sex} dog is a {self.color} {self.breed}"
    
    def __add__(self, other):
        if self.sex == other.sex:
            output = Dog(None, None, None)
        else:
            n = random.randint(0, 1)
            if n == 0:
                offspring_sex = "male"
            else:
                offspring_sex = "female"
            output = Dog(self.breed + "/" + other.breed, offspring_sex, self.color + "/" + other.color)
        return output

first_dog = Dog("labrador", "male", "yellow")
second_dog = Dog("poodle", "female", "black")
third_dog = Dog("german shepherd", "male", "brown/grey")

print(first_dog)
print(first_dog + second_dog)
print(first_dog + third_dog)
print(second_dog + third_dog)

class TrafficLight():
    
    def __init__(self, green, orange, red):
        self.green = green
        self.orange = orange
        self.red = red
    
    def __str__(self):
        my_str = ("The light is:\n"
            f"Green - {self.green}\n"
            f"Orange - {self.orange}\n"
            f"Red - {self.red}"
            )
        return my_str
    
    def __add__(self, other):
        if self.green == other.green:
            green = True
        else:
            green = False
        if self.orange == other.orange:
            orange = True
        else:
            orange = False
        if self.red == other.red:
            red = True
        else:
            red = False
        return TrafficLight(green, orange, red)

first_light = TrafficLight(True, False, False)
second_light = TrafficLight(False, True, True)

print(first_light)
first_light.green = False
print(first_light)
print(first_light + second_light)