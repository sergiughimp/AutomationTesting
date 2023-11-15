print("******************************** functions")
# block of code that can be reused when is called

print("**** simple function")
def say_hello():
    print("Hello")
    print("My first function")
say_hello()

print("**** functions with parameters (variables that can be passed to function)")
def say_hello_to(name):
    print(f"Hello {name}")
say_hello_to("Michael")

print("**** functions with 2 parameters")
# parameters goes to the positions. first variable goes to first parameter. second variable goes to second parameter
def say_good_bye(name, age):
    print(f"Hello {name}, you have {age} years old")
say_good_bye("Michael", "45")

def say_hi(name, message="standard message!"):
    print(f"{message}")
    print(f"I said hi to {name}")
say_hi("John")
say_hi("David","Another message")
say_hi("Tomas")

# parameters stays only in the body of the function, and all the variables from inside the function
print("**** functions with return (value that a function sends back when it is called)")

# counter function: a list, find_element
# return: how many times find_element is in the list

def counter(list, find_element):
    counter_element = 0
    for item in list:
        if item == find_element:
            counter_element += 1
    print(f"We finished to look, we found element {find_element} in the list {counter_element} times")
    return counter_element
print(counter([1, 2, 3, 2, 3], 3))

# return is optional
# can have more returns in one function but only one will be active when we call the function. When Python finds return keyword he stops the function

def function_multiple_return(age):
    if age < 18:
        return "adolescent"
    elif age < 65:
        return "adult"
    else:
        return "retired"
print(function_multiple_return(34))

'''
Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.
1.
    alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
    numere_pare = []
    numere_impare = []
    numere_pozitive = []
    numere_negative = []
    Itereaza prin listă alte_numere
    Populează corect celelalte liste
    Afișeaza cele 4 liste la final
'''
def get_even_numbers(list_numbers):
    new_list = []
    for item in list_numbers:
        if item % 2 == 0:
            new_list.append(item)
    return new_list
def get_odd_numbers(list_numbers):
    new_list = []
    for item in list_numbers:
        if item % 2 != 0:
            new_list.append(item)
    return new_list
def get_positive_numbers(list_numbers):
    new_list = []
    for item in list_numbers:
        if item > 0:
            new_list.append(item)
    return new_list
def get_negative_numbers(list_numbers):
    new_list = []
    for item in list_numbers:
        if item < 0:
            new_list.append(item)
    return new_list

other_numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
even_numbers = get_even_numbers(other_numbers)
odd_numbers = get_odd_numbers(other_numbers)
positive_numbers = get_positive_numbers(other_numbers)
negative_numbers = get_negative_numbers(other_numbers)

print(even_numbers)
print(odd_numbers)
print(positive_numbers)
print(negative_numbers)

'''
4. Alege un număr de la tastatură
    Ex: 7
    Scrie un program care să genereze în consolă următoarea piramidă
    1
    22
    333
    4444
    55555
    666666
    7777777

    Ex:3
    1
    22
    333
'''
def piramide(number):
    for i in range(1, number+1):
        print(f"{i}" * i)
piramide(7)

'''
3.Ghicitoare de număr:
    numar_secret = Generați un număr random între 1 și 30
    Numar_ghicit = None
    Folosind un while
    User alege un număr
    Programul îi spune:
        ● Nr secret e mai mare
        ● Nr secret e mai mic
        ● Felicitări! Ai ghicit!
'''

from random import randint
# will return True if you guessed the number. False otherwise
def guessed(your_number, secret_number):
    if your_number == secret_number:
        print(f"Number {your_number} is equal to number {secret_number}")
        print(f"Congratulations! You guessed the number!")
        return True
    if your_number > secret_number:
        print(f"Number {your_number} is bigger than {secret_number}")
        return False
    else:
        print(f"Number {your_number} is lower than {secret_number}")
        return False

secret_number = randint(1, 30)
tries = 0
max_tries = 5
while tries < max_tries:
    your_number = int(input("Enter a number from 1 to 30: "))
    tries += 1
    if guessed(your_number, secret_number):
        break
else:
    print("You didn't guess from 5 tries. Game over")
