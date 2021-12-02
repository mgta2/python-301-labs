# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.

class Form():
    
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def __str__(self):
        str_output = f"{self.name}, {self.age}, {self.height}, {self.weight}"
        return str_output
    
    def __repr__(self):
        str_output = (f"Name (str): {self.name}\n"
                      f"Age (int): {self.age}\n"
                      f"Height (cm, float): {self.height}\n"
                      f"Weight (kg, float): {self.weight}"
                      )
        return str_output

john_doe = Form("john", 30, 180.5, 70.5)
jane_doe = Form("jane", 40, 160.0, 60.8)

print(repr(john_doe))
print(jane_doe)