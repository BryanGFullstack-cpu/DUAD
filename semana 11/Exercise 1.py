#Cree una clase de Circle con un atributo de radio y un método para calcular el área.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)
    
c = Circle(5)
print(c.get_area())

