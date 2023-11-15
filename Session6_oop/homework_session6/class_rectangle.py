'''
2. Clasa Dreptunghi
    Atribute: lungime, latime, culoare
    Constructor pentru toate atributele
    Metode:
        ● descrie()
        ● aria()
        ● perimetrul()
        ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
    Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().
'''

class Rectangle:
    def __init__(self, length, weight, color):
        self.length = length
        self.weight = weight
        self.color = color

    def descrineRectangle(self):
        print(f"The length of the rectangle is {self.length}, the weight of the rectangle is {self.weight} and the color of the rectangle is {self.color}")
    def areaRectangle(self):
        print(f"The area of the rectangle is {self.length * self.weight}")
    def perimeterRectangle(self):
        print(f"The perimeter of rectangle is {2 * (self.length + self.weight)}")
    def changeColorRectangle(self, new_color):
        self.color = new_color

rectangle1 = Rectangle(4, 6,"red")
rectangle1.descrineRectangle()
rectangle1.areaRectangle()
rectangle1.perimeterRectangle()
rectangle1.changeColorRectangle("black")
rectangle1.descrineRectangle()