# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.

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

# Start of new code:

class BigDog(Dog):
    
    def __init__(self, breed, sex, color, size):
        super().__init__(breed, sex, color)
        self.size = size
    
    def gets_fatter(self):
        self.size += 1

my_dog = BigDog('labrador', 'male', 'black', 20)
print(my_dog)
my_dog.gets_fatter()
print(my_dog)

class CopperKettle(Kettle):
    
    def __init__(self, min_capacity, max_capacity):
        super().__init__('copper', min_capacity, max_capacity)

my_kettle = CopperKettle(150, 500)
print(my_kettle)

class BigLabrador(BigDog):
    
    def __init__(self, sex, color, size):
        super().__init__('labrador', sex, color, size)

my_lab = BigLabrador('male', 'black', 20)
print(my_lab)