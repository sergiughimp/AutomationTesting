from pprint import pprint
print("*********************************************************** data structures")
# data structures = collection of data to store multiple items in one variable. Can be different data types
print("******************************** list")
    # each element in the list has an index. the indexes starts from 0
    # ordered (to add new item it goes to end of the list)
    # mutable (can add, delete, modify elements from the list)
    # allow dupblicates
    # with len() function can deternime the size of the list
list_numbers = [1, 2, 3, 56, 12, 0, -2]
list_string = ["Michael", "John", "David"]
list_bool = [True, False, True, False, False]


list_fruits = ["banana", "apple", "orange", "kiwi"]
print(f"In the first basket we have {list_fruits[0]}")
print(list_fruits[1:3]) # slicing on the list
print(list_fruits[-1]) # negative slicing on the list
print(len(list_fruits)) # size of the list
list_fruits.append("grape") # add a fruit to the list
print(list_fruits)
list_combined = ["banana", True, 12, "apple", 3.14]
print(list_combined)

list_combined.remove("banana") # delete the item "banana"
print(list_combined)
print(list_combined.pop()) # delete and return last item

list_combined.clear()
print(list_combined)

l = ["a", "b", "c", "a", "b", "x", "z", "b"]
index_first_b = l.index("b")
print(index_first_b)
index_second_b = l[index_first_b + 1:].index("b") + index_first_b + 1
print(index_second_b)
index_third_b = l[index_second_b + 1:].index("b") + index_second_b + 1
print(index_third_b)

print(l[0].upper())
print(l[1].upper())

print("***************** functions on list: max, min, sum")
lx = [5, 7, 12, -3, 8, 2, 3, 21]
print(max(lx))
print(min(lx))
print(sum(lx))
print("***************** list membership: in, not in")
print(7 in lx)
print(6 not in lx)

vowels = ["a", "e", "i", "o", "u"]
letter = "b"
if letter in vowels:
    print("the letter is vowel")
else:
    print("the letter is consonant")

print("***************** concatenation of 2 lists")
ly = [70, 33, 14, 51]
print(lx + ly) # concatenation

lx.extend(ly)
print(lx) # extend fist list with adding the second list

print("******************************** dict: key: value pairs")
    # collection of data to store data values in key: value pairs
        # key (should be unique) = indexes
    # ordered, changeable, do not allow duplicates

empty_dict = {}
print(empty_dict)
example_dict = {
    "s": 12,
    3: 24
}
print(example_dict)

depo_cars = ["BMW", "Audi", "Ford", "Honda", "Toyota"]
color_cars = {
    "red": "BMW",
    "green": "Audi",
    "blue": ["Ford", "Ferari"],
    "yellow": "Honda",
    "white": "Toyota",
}
print(color_cars)
print(f"On the red depo we have {color_cars["red"]}")
print(f"On the blue depo we have {color_cars["blue"][0]} si {color_cars["blue"][1]}")

# example: how many times 'a' is in the 'abracadabra'
word = "abracadabra"
letter_a_count = word.count("a")
print(letter_a_count)
letter_b_count = word.count("b")
print(letter_b_count)

# dict: key = letter, value = how many times is in the word
count_letter = {
    "a": word.count("a"),
    "b": word.count("b"),
    "r": word.count("r")
}
print(count_letter)

# group data
student_last_name = "Jordan"
student_first_name = "Michael"
student_age = 23
student_weight = 83.2

student = {
    "last_name": "Jordan",
    "first_name": "Michael",
    "age": 23,
    "weight": 83.2,
    "birthdate": {
        "day": 19,
        "month": "June",
        "year": 1991
    }
}
pprint(student)
print(f"My name is {student["last_name"]} {student["first_name"]} and I have {student["age"]} years old, my weight is {student["weight"]} kg. my birthday is on {student["birthdate"]["day"]} {student["birthdate"]["month"]} {student["birthdate"]["year"]}")

print("******************* operations on dict: add, delete, modify an item on dict")
color_cars2 = {
    "red": "BMW",
    "green": "Audi",
    "blue": "Ford",
    "yellow": "Honda",
    "white": "Toyota",
    "pink": "Ferari"}
# add an item to the dict
pprint(color_cars2)
# delete an item from the dict
del color_cars2["pink"]
print(color_cars2)
# modify an item (value) in the dict
color_cars2["blue"] = "Mercedes"
print(color_cars2)

# print(color_cars2["orange"]) # no cars with this color
if "orange" in color_cars2:
    print(color_cars2["orange"])
else:
    print("No orange car's")
print("******************************** set = only unique items")
    # collection of data to store multiple unique values in a single variable
    # unordered, unchangeable, unidexed, no slicing
empty_set = {}
print(empty_set)
seasons_set = {"spring", "summer", "autumn", "winter"}
print(seasons_set)
seasons_set.add("spring")
print(seasons_set)
seasons_set.add("something")
print(seasons_set)
# set membership
season = "summer"
if season in seasons_set:
    print("Found in the set")
else:
    print("Not in the set")

seasons_set.remove("something")
print(seasons_set)

print(f"Length of the set {len(seasons_set)}")
print("******************************** tuples: can't modified (immutable)")
    # data collection to store multiple items in a single variable
    # ordered and unchangeable, allow duplicates
    # immutable (can't add, delete, modify elements from the tuple)
tuple_numbers = (1, 2, 3, 56, 12, 0, -2)
tuple_string = ("Michael", "John", "David")
tuple_bool = (True, False, True, False, False)

print(tuple_numbers)
print(tuple_string)
print(tuple_bool)

print(tuple_numbers[1])