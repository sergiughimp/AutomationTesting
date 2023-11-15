# exceptions = special classes used when something goes wrong in the code
# try - except = used for manage possible exception in the code. and the code will not break
list_numbers = [1, 2, 3, 4]
print(list_numbers[0])
try:
    print(list_numbers[5])
except IndexError as e:
    print("Found an error: IndexError")
    print(e)

# try - except = can be used when we receive data from the user (check the expected result)
try:
    age = int(input("Enter the age: "))
    print(f"The age is {age}")
except ValueError as e:
    print(f"what you entered is not a number")


try:
    even_number = int(input("Enter an even number: "))
    assert even_number % 2 == 0
except ValueError as e:
    print("what your entered is not a number")
except AssertionError as e:
    print("The number is not even!")