print("*********** loops")
print("**** for: to iterate over a sequence of data. with a known number of steps")

# range(x) = takes all the numbers from 0 to x - 1 (inclusive)
print(list(range(10)))

for index in range(10):
    print(f"Index has the value {index}")
print("** first loop")

for idx in range(3, 7):
    print(f"I am learning to count from 3 to 7")
    print(f"    arrived to {idx}")
print("** second loop")

for i in range(1, 10, 2):
    print(f"I am learning to count from 1 to 10 with step 2")
    print(f"    arrived to {i}")

number_day_week = 7
for i in range(1, number_day_week + 1):
    print(f"Is {i} day of the week")

musical_notes = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
for idx in range(len(musical_notes)):
    print(f"On the index {idx} we found the musical note {musical_notes[idx]}")

print("**** for each")
for musical_note in musical_notes:
    print(f"Current musical note is: {musical_note}")

print("count how many times 'do' is in the list 'musical_note'")
count_do = 0
for musical_note in musical_notes:
    if musical_note == "do":
        count_do += 1
print(count_do)

print("**** break: stop the iteration")
print("want to find musical_note 'la'. If I found I want to stop. If it doesn't exist in the list, print that it doesn't exist")
find_musical_note = "la"
found = False # flag variable
for musical_note in musical_notes:
    if musical_note == find_musical_note:
        print(f"Musical note {musical_note} was found")
        found = True
        break
if not found:
    print("We didn't found the musical note")
print("Loop ends here")

print("**** for else: runs only when iteration of for ends without any taking something from for")
find_musical_note = "sil"
for musical_note in musical_notes:
    if musical_note == find_musical_note:
        print(f"Musical note {musical_note} was found")
        break
else:
    print("We didn't found the musical note")

print("**** continue: continues to the iteration to next step")
print("print all musical notes, without that one that starts with 's'")
print("Musical notes that not starting with 's'")
for musical_note in musical_notes:
    if musical_note[0] == 's':
        continue
    else:
        print(musical_note)

print("print all the numbers from 1 to 10 that are not divided with 3")
for i in range(0, 10):
    if i % 3 == 0:
        continue
    print(f"Number {i} is not divided with 3")

print("**** while: iterates until the condition is true")
i = 0
while i < 5:
    print(i)
    i += 1

# while = used as long as we don't know how many times the code will run, but we have a condition
# validate an input from user
age_is_correct = False
while not age_is_correct:
    # age = int(input("Enter your age: "))
    age = 19
    if 1 < age < 99:
        age_is_correct = True
    else:
        print(f"The age is not right. it has to be between 1 and 99. Try again!")

print("**** while else: runs only when iteration of while ends without any taking something from while")
# validate a password
user, password = "Michael", "secretpassword"
print("You are not login. You have to log in")
number_tries = 0
max_number_tries = 3
while number_tries < max_number_tries:
    my_password = input("Enter your password: \n")
    if password == my_password:
        print("Congratulations! you are logged in")
        break
    else:
        print("you entered a wrong password, try again the password")
    number_tries += 1
    print(f"You tried {number_tries} times to enter the password!")
    print(f"You have {max_number_tries - number_tries} tries left")
else:
    print(f"You tried {max_number_tries} to login. You can't try more")

print("**** nested loop: for in for")
hotel = [
    ["Management office", "Conference office", 10, 11, 12, 13, 14, 15], # parter
    [20, 21, 22, 23, 24, 25], # first floor
    [30, 31, 32, 33, 34, 35], # second floor
    [40, 41, 42, 43] # third floor
]

for floor in hotel:
    print(f"New floor {floor}")
    for room in floor:
        print(f"    room {room}")


for i in range(5):
    for j in range(4):
        print(f"{i} * {j} = {i * j}")
    print()