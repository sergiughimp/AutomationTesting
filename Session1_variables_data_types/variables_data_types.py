print("*********************************************************** comments")
'''
Multiline comment

'print' function = way to communicate with program (output)
'input' function = to give data to program from user keyboard
'''

# one line comment

print("Hello world") # inline comment

print("*********************************************************** variable = container to store values")
# snake_case = style to define variables in python (small letters, underscore between words)
my_first_variable = 1
print(my_first_variable)
# name of variables can contain only: small and big letters, numbers, underscores
# name have to be unique (value can be the same)
var1 = 5
print(var1)
var_1 = 100
print(var_1)
VAR_ = "x"
print(VAR_)
# can't start with numbers
# 1var = 10

# multiple assignment
a, b, c = 10, 20, 30 # a = 10, b = 20, c = 30
print(a, b, c)
x = y = z = 15
print(x, y, z)
# name of variables has to have meaning
age1 = 24
print(age1)
print("*********************************************************** data types")
# bool = True and False
adult = True # <=> with 1
print(adult)
maried = False # <=> with 0
print(maried)
# char = only one character
char = "C"
print(char)
# string = characters. everything in quotations is a string. single or double quotes
str1 = "42"
print(str1)
str2 = "True"
print(str2)
str3 = "Michael"
print(str3)
str4 = "McDonald's"
print(str4)

# int = numbers (-10, 2, 4, 2223)
age2 = 45
print(age2)
year_born = 1999
print(year_born)
# float / double = numbers with decimals
pi = 3.14
print(pi)
depth = 4.5
print(depth)
height = 3.3
print(height)

print("*********************************************************** type_casting")
print(f"Type of str1: {str1} is: {type(str1)}")
print(f"Type of str2: {str2} is: {type(str2)}")

# type_casting = force the conversion from one data type to another
# sir1 from string -> to int
my_int1 = int(str1)
print(f"Type of my_int1: {my_int1} is: {type(my_int1)}")

# sir1 from string -> to float
my_float1 = float(str1)
print(f"Type of my_float1: {my_float1} is: {type(my_float1)}")

# sir1 from string -> to bool
my_bool = bool(str1)
print(f"Type of my_bool: {my_bool} is: {type(my_bool)}")

# my_int1 from int -> to float
my_float2 = float(my_int1)
print(f"Type of my_bool: {my_float2} is: {type(my_float2)}")

# all the variables can be converted to string

# int to bool
true = bool(5)
print(f"Type of my_bool: {true} is: {type(true)}")
false = bool(0)
print(f"Type of my_bool: {false} is: {type(false)}")

print("*********************************************************** 'print' function & concatenation")
first_name = "Michael"
last_name = "Jordan"
print(f"Full name is {first_name} {last_name}") # concatenation only the strings
age = 34
print(f"Full name is {first_name} {last_name} and the age is {age}") # concatenation strings and int


print(f"My age raised with one year {age + 1}")

author_book = f"The author of the book is {first_name} {last_name}. "
print(author_book)
author_book += f"The age of the author is {age}"
print(author_book)

print("*********************************************************** assert")
# assert = used to make verifications
# if condition is True, the code goes forward
# if condition is False, the code stops, the code give error
year_born4 = 1991
age4 = 32
# check if the year_born4 == age4
assert 2023 - year_born4 == age4, f"Year born is {year_born4} and it doesn't match with age {age4}"

year_born4 = 1991
age4 = 31
# check if the year_born4 == age4
# after comma put the error message
# assert 2023 - year_born4 == age4, f"Year born is {year_born4} and it doesn't match with age {age4}"

s1 = "42"
int_s1 = int(s1)
assert int_s1 == 42, f"{int_s1} is not an int equal with 42"

print("*********************************************************** input()")
# input = take values from user (from keyboard)
# \n = newline
name = input("Enter the name: ")
print(f"Hello, {name}!")

# by default, everything from user is a string
age5 = int(input(f"Enter your age: "))
print(type(age5))

# exercise : assert & input: cod captcha
x, y = 14, 25
result_captcha = int(input(f"{x} + {y}? "))
assert result_captcha == x + y, "You are not a human, you are a robot"
