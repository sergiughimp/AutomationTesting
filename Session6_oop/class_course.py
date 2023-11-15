from class_person import Person
class Course:

    def __init__(self, company, name, term, start_date, number_place):
        self.company = company
        self.name = name
        self.term = term
        self.start_date = start_date
        self.number_place = number_place
        self.students = []

    def registration(self, student):
        if self.number_place > 0:
            self.students.append(student)
            self.number_place -= 1
            print(f"The student {student.first_name}{student.last_name} was registered with success")
        else:
            print("The are no more places")


    def describe_course(self):
        print(f"{self.name} | {self.company} | {self.term} | {self.start_date} days")
        print("-" * 20)
        for student in self.students:
            print(f"{student.first_name} {student.last_name} ({student.age} years old)")
        if not self.students:
            print("There are not students yet")
        print()

course_python = Course("Python Course", "Automation", 120, "2022-09-02", 3)
print(course_python.describe_course())

student1 = Person("Michael", "Tyson", 34, 1.78)
student2 = Person("Evan", "Anderson", 25, 1.67)

course_python.registration(student1)
course_python.registration(student2)
print(course_python.describe_course())

course_python.registration(
    Person("David", "Johnson", 45, 1.98)
)
print(course_python.describe_course())
