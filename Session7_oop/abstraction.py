import math

# example: area, perimeter
from abc import ABC
class GeometricalForm(ABC):

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError


class Circle(GeometricalForm):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 3 * 3.14

    def perimeter(self):
        return self.radius * 3.14

class Rectangle(GeometricalForm):
    def __init__(self, length, weight):
        self.length = length
        self.weight = weight

    def area(self):
        return self.length * self.weight
    def perimeter(self):
        return (self.length + self.weight) * 2

    def diagonal(self):
        return math.sqrt(self.length**2 + self.weight**2)

circle1 = Circle(10)
print(circle1.area())
print(circle1.perimeter())

rectangle1 = Rectangle(4, 5)
print(rectangle1.area())
print(rectangle1.perimeter())
print(rectangle1.diagonal())


list_forms = [Circle(4), Rectangle(5, 6), Circle(10), Rectangle(11, 8)]
for form in list_forms:
    print()
    print(f"Perimeter {form.perimeter()}")
    print(f"Area: {form.area()}")