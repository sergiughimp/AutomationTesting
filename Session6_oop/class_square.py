class Square:
    def __init__(self, length, color):
        self.length = length
        self.color = color

    def area(self):
        area = self.length ** 2
        return area

square1 = Square(12,"white")
print(square1.length)
print(square1.color)
print(square1.area())

square2 = Square(14, "red")
print(square2.length)
print(square2.color)
print(square2.area())