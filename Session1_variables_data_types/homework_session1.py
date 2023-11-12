'''Exerciții obligatorii - grad de dificultate: Ușor spre Mediu:
1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
'''
print("Ex 1")
print("variable = container to store values")
'''
2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă :
    - string
    - int
    - float
    - bool
    Observație: Valorile vor fi alese de tine după preferințe.
'''
print("Ex 2")
fruit = "apple"
number_fruit = 3
kilograms_fruit = 0.7
in_basket_fruit = False
'''
3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
'''
print("Ex 3")
print(f"fruit {fruit} has data type {type(fruit)}")
print(f"numer of the fruit {number_fruit} has data type {type(number_fruit)}")
kilograms_fruit = kilograms_fruit
print(f"grams of fruit {kilograms_fruit} has data type {type(kilograms_fruit)}")
print(f"in basket fruit {in_basket_fruit} has data type {type(in_basket_fruit)}")
'''
4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
    - Verifică tipul acesteia.
'''
print("Ex 4")
kilograms_fruit = round(kilograms_fruit)
print(kilograms_fruit)
'''
5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile. Rezolvă nepotrivirile de tip prin ce modalitate dorești.
'''
print("Ex 5")
print(f"Yesterday I bought a {fruit}")
print(f"Number of them are {number_fruit}")
print(f"It weighs {kilograms_fruit} kilograms")
print(f"It is in the basket {in_basket_fruit}")
'''
6. Citește de la tastatură:
    - numele;
    - prenumele.
    Afișează: 'Numele complet are x caractere'.
'''
print("Ex 6")
# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")

first_name = "Michael"
last_name = "Ross"
print(f"Full name is {first_name} {last_name} and it has {len(first_name) + len(last_name)} characters")
'''
7. Citește de la tastatură:
    - lungimea;
    - lățimea.
    Afișează: 'Aria dreptunghiului este x'.
'''
print("Ex 7")
# length = input("Enter length: ")
# width = input("Enter width: ")

length = 5
width = 4
print(f"The area of triangle is: {length * width}")
'''
8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
    - afișează de câte ori apare cuvântul 'the';
'''
print("Ex 8")
coral_string = "Coral is either the stupidest animal or the smartest rock"
print(coral_string.count("the"))
'''
9. Același string.
    ● Afișează de câte ori apare cuvântul 'the';
    ● Printează rezultatul.
'''
print("Ex 9")
# print(coral_string.count("the"))
'''
10. Același string.
    ● Folosiți un assert ca să verificați dacă acest string conține doar numere.
'''
print("Ex 10")
# assert coral_string.isdigit() == coral_string, "No numbers"
s = "444"
assert s.isdigit(), "no numbers"
'''
Exerciții Opționale - grad de dificultate: Mediu spre greu (s-ar putea să ai nevoie de Google).
1. Exercițiu:
    - citește de la tastatură un string de dimensiune impară;
    - afișează caracterul din mijloc.
'''
print("Ex 1")
odd_size_string = "lumos"
for i in range(0, len(odd_size_string)):
    if int(len(odd_size_string) / 2) == i:
        print(odd_size_string[i])
'''
2. Folosind assert, verifică dacă un string este palindrom.
'''
print("Ex 2")
palindrom_string = "odo"
assert "odo" == palindrom_string[::-1], "it is not palindrom"
'''
3. Folosind o singură linie de cod :
    - citește un string de la tastatură (ex: 'alabala portocala');
    - salvează fiecare cuvânt într-o variabilă;
    - printează ambele variabile pentru verificare.
'''
print("Ex 3")
string = "alabala portocala"
first_string1, second_string1 = "alabala", "portocala"
first_string2, second_string2 = string.split()

print(first_string1, second_string1)
print(first_string2, second_string2)
'''
4. Exercițiu:
    - citește un string de la tastatură (ex: alabala portocala);
    - salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
    - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.
'''
first_character_string = string[0]
print(first_character_string)
for i in range(1, len(string)-1):
    if string[i] == first_character_string:
        upper = string[i].upper()
        replace = string.replace(string[i], upper)
print(string[0] + replace[1:-1] + string[-1])
'''
5.Exercițiu:
    - citește un user de la tastatură;
    - citește o parolă;
    - afișează: 'Parola pt user x este ***** și are x caractere';
    - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.
    eg: parola abc => ***
    parola abcd => ****
'''
user = "John"
password = "11111"
print(f"The user is {user} and the password is {password.replace(password, "*"*len(password))}. the password has {len(password)} characters")