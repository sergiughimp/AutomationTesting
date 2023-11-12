print("*********************************************************** operators")
print("******************************** assignation")
a = 10
a += 2 # a = a + 2
a -= 2 # a = a + 4
a *= 2 # a = a * 2
a /= 2 # a = a / 2 -> 10.0 -> division becomes float
print(a)
a = int(a)
a //= 2 # operator // for numbers without digits
print(a)

print(7 / 2)
print(7 // 3)

print("******************************** arithmetics")
a, b = 12, 5
print(f"Addition: {a + b}")
print(f"Substraction {a - b}")
print(f"Multiplication {a * b}")
print(f"Division (numbers with digits -> float) {a / b}") # numbers with digits -> float
print(f"Division (numbers without digits -> float) {a // b}") # numbers without digits -> int
print(f"Modulo {a % b}") # modulo
print(f"Exponentiation {a ** b}") # power
# can use arithmetics (+, *) operators on other data types: string, int, float
print("***************** concatenation")
print("Michael" + " " + "Jordan")
print("Michael " * 5)


print("******************************** comparison")
number1, number2 = 5, 7
print(f"number1: {number1}, number2: {number2}")
print(f"Equal: number1 and number2: {number1 == number2}")
print(f"Not equal: number1 and number2: {number1 != number2}")
print(f"Greater than: number1 and number2: {number1 > number2}")
print(f"Less than number1 and number2: {number1 < number2}")
print(f"Greater then or equal to: number1 and number2: {number1 >= number2}")
print(f"Greater then or equal to: number1 and number2: {number1 <= number2}")


print("******************************** logical: and, or, not")
has_driver_licence = True
age = 18
print("and = returns True if both statements are true")
assert has_driver_licence and age >= 18, "Have no rights to drive"

grade1, grade2, grade3 = 7, 8, 5
# assert grade1 > 4 and grade2 > 4 and grade3 > 4, "Failed"

print("or = returns True if one of the statements are true")
grade1, grade2, grade3 = 2, 3, 5
assert grade1 > 4 or grade2 > 4 or grade3 > 4, "You didn't pass any exams"

print("not = reverse the result, returns False if the result is true")
is_adult = age > 18
print(is_adult)
print(not is_adult)

print("*********************************************************** control flow")
print("******************************** if")

# age = int(input("Age: "))
age = 15
if age < 18:
    print("You are not adult")
    print(f"you have {age} years old")
print("if is done")
print()
# grade = int(input("Grade: "))
grade = 5
if grade > 4:
    print("congratulations, you passed")
print(f"You have the grade {grade}")

print("******************************** if - else")
# age = int(input("Age: "))
age = 21
if age >= 18:
    print("you are an adult")
else:
    print("you are not an adult")
print(f"you the the age {age}")

print("******************************** if - else - if - else")
age = 26
if age < 0:
    print("age doesn't exist")
elif age <= 2:
    print(f"you have {age} years old. you are a baby")
elif age <= 12:
    print(f"you have {age} years old. you are a child")
elif age <= 18:
    print(f"you have {age} years old. you are a adolescent")
elif age <= 60:
    print(f"you have {age} years old. you are a adult")
    if age <= 24:
        print(f"you have {age} years old. you are a student")
    else:
        print(f"you have {age} years old. you are a employed")
else:
    print(f"you have {age} years old. you are a retired")
