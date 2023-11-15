'''
1.Clasa Cerc
    Atribute: raza, culoare
    Constructor pentru ambele atribute
    Metode:
        ● descrie_cerc() - va PRINTA culoarea și raza
        ● aria() - va RETURNA aria
        ● diametru()
        ● circumferinta()
'''
class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        self.pi = 3.14
    def describe_circle(self):
        print(f"The circle has the radius {self.radius} and the color {self.color}")
    def area_circle(self):
        print(f"The area of the circle is {self.pi * self.radius ** 2}")
    def diameter_circle(self):
        print(f"The diameter of the circle is {self.radius * 2}")
    def circumference_circle(self):
        print(f"The circumference of the circle is {2 * self.pi * self.radius}")

circle1 = Circle(3, "yellow")
circle1.describe_circle()
circle1.area_circle()
circle1.diameter_circle()
circle1.circumference_circle()