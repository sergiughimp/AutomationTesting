# parent class (base)
class Person:
    counter_persons = 0
    def __init__(self, name, age, address):
        Person.counter_persons += 1
        self.name = name
        self.age = age
        self.address = address
    def describe(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

    def year_born(self):
        return 2023 - self.age

# child class (inherits Person, and all the attributes and methods)
class Student(Person):
    def __init__(self, name, age, address, college, year_learn):
        # super() = parent class (Person). constructor of parent class
        super().__init__(name, age, address)
        self.college = college
        self.year_learn = year_learn

    def describe(self):
        super().describe()
        print(f"College: {self.college}, Year learn: {self.year_learn}")

    def graduate_year(self):
        return 2023 +  (4 - self.year_learn)

class Empoloyee(Person):
    def __init__(self, name, age, address, company, wage):
        super().__init__(name, age, address)
        self.company = company
        self.wage = wage

    def describe(self):
        super().describe()
        print(f"Company: {self.company}, wage ${self.wage}")

    def yearly_wage(self):
        return self.wage * 12

print(Person.counter_persons)
person1 = Student("John", 21, "34 Priory way", "University of London", 3)
person2 = Empoloyee("Michael", 45, "22 New Ave", "Google", 3400)
print(Person.counter_persons)

person1.describe()
print(person1.year_born())
print(person1.graduate_year())

person2.describe()
print(person2.year_born())
print(person2.yearly_wage())