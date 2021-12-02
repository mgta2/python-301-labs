# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    
    def __init__(self, name, color, position_from_sun):
        self.name = name
        self.color = color
        self.position_from_sun = position_from_sun
    
    def __str__(self):
        my_str = (f"Name: {self.name}, "
                  f"Color: {self.color}, "
                  f"Position from Sun: {self.position_from_sun}"
                  )
        return my_str

earth = Planet("Earth", "Blue", 3)
mars = Planet("Mars", "Red", 4)
neptune = Planet("Neptune", "Blue", 8)

print(earth)
print(mars)
print(neptune)
