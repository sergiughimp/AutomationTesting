
class Burger:
    def __init__(self, ingrediente, sos, vegetarian=False):
        self.ingredients = ingrediente
        self.vegetarian = vegetarian
        self.sos = sos

    def receta(self):
        print("Prajiti cifla")
        print("Puneti partea de jos a ciflei pe o farfurie")
        if self.vegetarian:
            print("Adaugati o bucata prajita de hallomi!")
        else:
            print("Adaugati o bucata de vita angus")
        for ingredient in self.ingredients:
            ingredient.gateste()
        print(f"Turnati mult sos {self.sos} peste ingrediente")
        print("Puneti partea de sus a ciflei peste burger")
        print("Serviti cald!")
        print()

class Ingredient:
    def __init__(self, nume_ingredient, metoda_gatire):
        self.nume_ingredient = nume_ingredient
        self.metoda_gatire = metoda_gatire
    def gateste(self):
        print(f"Ingredient {self.nume_ingredient}")
        print(f"\t{self.metoda_gatire}")

chedar = Ingredient("Cheddar", "taiati felii si puneti peste burger")
ceapa_caramelizara = Ingredient("Ceapa", "prajiti in ulei pana devine dulce apoi puneti peste burger")
castraveti_murati = Ingredient("Castraveti murati","taiati castravetii felii si puneti peste burger")
rosii = Ingredient("Rosii", "taiati felii si puneti peste burger")

buger_meat = Burger([chedar, ceapa_caramelizara, castraveti_murati], "BBQ")
buger_meat.receta()

buger_vegetarian = Burger([rosii, ceapa_caramelizara, castraveti_murati], "BBQ", True)
buger_vegetarian.receta()