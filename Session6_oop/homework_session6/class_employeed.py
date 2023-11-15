'''
3. Clasa Angajat
    Atribute: nume, prenume, salariu
    Constructor pt toate atributele
    Metode:
        ● descrie()
        ● nume_complet()
        ● salariu_lunar()
        ● salariu_anual()
        ● marire_salariu(procent)
'''

class Employeed:
    def __init__(self, first_name, last_name, wage):
        self.first_name = first_name
        self.last_name = last_name
        self.wage = wage

    def describeEmployee(self):
        print(f"The employee's name is {self.first_name} {self.last_name} and it has the wage ${self.wage}")

    def full_name(self):
        print(f"The employee's full name is {self.first_name} {self.last_name}")
    def monthly_wage(self):
        print(f"Monthly wage is {self.wage}")
    def year_wage(self):
        print(f"The wage per year is {self.wage * 12}")
    def raise_wage(self, procent):
        print(f"The wage was raised with {procent}% and now the wage is {self.wage + (self.wage * procent) / 100}")

employee1 = Employeed("Mary", "Watson", 4000)
employee1.describeEmployee()
employee1.full_name()
employee1.monthly_wage()
employee1.year_wage()
employee1.raise_wage(10)