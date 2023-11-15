# class = template to create objects from that class
# class = sum of characteristics (attributes) and actions (methods)
# name of the class are writen by capital letters (CamelCase)
class Person:

    # objects = instance of a class (properties: attributes (characteristcs), methods (functions in the class that tell what objects can do))
    # first_name = ""
    # last_name = ""
    # age = 0
    # height = 0.0

    # __init__ = constructor of the class, used as a start to create objects in the class. always executed when the class is being initiated. like a field on a form with * to be completed
    def __init__(self, first_name, last_name, age, height):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height

    # self = keyword used to access variable that belongs to that class
    def present_me(self):
        print(f"Hello, I'm {self.first_name} {self.last_name}, I'm {self.age} years old and my height is {self.height} cm")

    # methods = functions on objects (takes the object called as self parameter)
    def age_increases(self):
        self.age += 1

#'person1' and 'person2' are objects created from class Person
person1 = Person("Mary", "Tyson", 45, 1.65)
person2 = Person("Michael", "Jonson", 34, 1.87)

# because we used class Person as a template for creating objects, we can call both methods
person1.present_me()
person2.present_me()

print(person1.age)
print(person2.age)

person1.age_increases()
person1.present_me()

persons = [person1, person2]

for person in persons:
    person.age_increases()
    person.present_me()