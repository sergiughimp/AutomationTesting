'''
ABSTRACTION
    Clasa abstractă FormaGeometrica
    Conține un field PI=3.14
    Conține o metodă abstractă aria (opțional)
    Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’
'''
'''
INHERITANCE
    Clasa Pătrat - moștenește FormaGeometrica
    constructor pentru latură
'''
'''
ENCAPSULATION
    latura este proprietate privată
    Implementează getter, setter, deleter pentru latură
    Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
    Clasa Cerc - moștenește FormaGeometrica
    constructor pentru rază
    raza este proprietate privată
    Implementează getter, setter, deleter pentru rază
    Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
'''
'''
POLYMORPHISM
    Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
    Creează un obiect de tip Patrat și joacă-te cu metodele lui
    Creează un obiect de tip Cerc și joacă-te cu metodele lui
'''

from abc import ABC

class GeometricalForm(ABC):

    pi = 3.14
    def area(self):
        raise NotImplementedError

    def desribe(self):
        print("Probably I have corners")

class Square(GeometricalForm):
    __side = 10

    def __init__(self, name):
        self.name = name

    def getter_side(self):
        return self.__side

    def setter_side(self, new_side):
        self.__side = new_side
    def deleter_side(self):
        pass
    def area(self):
        return self.__side * self.__side

class Circle(GeometricalForm):

    __radius = 12
    def __init__(self, name):
        self.name = name

    def getter_radius(self):
        return self.__radius
    def setter_radius(self, new_radius):
        self.__radius = new_radius

    def area(self):
        return self.__radius ** 2 * self.pi

    def describe(self):
        print("I don't have corners")

square = Square("Square")
circle = Circle("Circle")

print(f"Area of square before changing the side is {square.area()}")
square.desribe()
square.setter_side(5)
print(f"Area of square after changing the side is {square.area()}")

print(f"Area of circle before changing the radius is {circle.area()}")
circle.desribe()
circle.setter_radius(5)
print(f"Area of circle after changing the side is {circle.area()}")