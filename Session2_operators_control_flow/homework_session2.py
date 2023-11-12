'''
Exerciții obligatorii - grad de dificultate: Ușor spre Mediu. Pentru toate exercițiile se va folosi noțiunea de if în rezolvare. Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if. X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe. X este un int.
'''
'''
    1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
'''
print("'if' is used when a block of code have to be executed, if the condition is true"
      "'else' is used when a block of code have to executed, if the condition is false"
      "'else if' is used when a new condition is tested, if the first condition is false")

'''
    2. Verifică și afișează dacă x este număr pozitiv sau nu.
'''
number = 7
if number > 0:
    print(f"Number {number} is positive")
'''
    3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
'''
number = -1
if number > 0:
    print(f"Number {number} is positive")
elif number < 0:
    print(f"Number {number} is negative")
else:
    print("Number is equal with 0")
'''
    4. Verifică și afișează dacă x este între -2 și 13.
'''
number = 9
if number > -2 and number < 13:
    print(f"The number {number} is between -2 and 13")
else:
    print(f"The number {number} is not between -2 and 13")
'''
    5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
'''
x, y = 12, 8
if x - y < 5:
    print(f"Difference between the number {x} and the number {y} is less than 5")
else:
    print(f"Difference between the number {x} and the number {y} is not less than 5")
'''
    6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
'''
x = 19
if not (x > 5 and x < 27):
    print(f"Number {x} not in [5, 27]")
else:
    print(f"Number {x} in [5, 27]")
'''
    7. x și y (int). Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
'''
x, y = 6, 6
if x == y:
    print(f"Number {x} and number {y} are equals")
else:
    print(f"Number {x} and number {y} are not equals")
'''
    8. X, y, z - laturile unui triunghi. Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
'''
x, y, z = 6, 6, 7
if x == y == z:
    print("Triunghi echilateral")
elif x == y or y == z or z == x:
    print("Triunghi isoscel")
else:
    print("Triunghi oarecare")
'''
    9. Citește o literă de la tastatură. Verifică și afișează dacă este vocală sau nu
'''
letter = 'b'
if letter == "A" or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U' or letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print(f"The letter {letter} is vowel")
else:
    print(f"The letter {letter} is consonant")
'''
    10.Transformă și printează notele din sistem românesc în >
        Peste 9 => A
        Peste 8 => B
        Peste 7 => C
        Peste 6 => D
        Peste 4 => E
        4 sau sub => F
'''
grade = 8
if grade > 10:
    print("grade doesn't exist")
elif grade >= 9:
    print("grade is A")
elif grade >= 8:
    print("grade is B")
elif grade >= 7:
    print("grade is C")
elif grade >= 6:
    print("grade is D")
elif grade >= 4:
    print("grade is E")
elif grade < 4:
    print("grades is F")
else:
    print("grade doesn't exist")
'''
Exerciții Opționale - grad de dificultate: Mediu spre greu - might need Google.
    1.Verifică dacă x are minim 4 cifre (x e int). (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
'''
x = 345
if len(str(x)) == 4 and str(x).isdigit():
    print(f"Number {x} is at least 4 digits")
else:
    print(f"Number {x} is less than 4 digits")
'''
    2.Verifică dacă x are exact 6 cifre.
'''
x = 341534
if len(str(x)) == 6:
    print(f"Number {x} has exact 6 digits")
else:
    print(f"Number {x} has not exact 6 digits")
'''
    3.Verifică dacă x este număr par sau impar (x e int).
'''
x = 89
if x % 2 == 0:
    print(f"Number {x} is even")
else:
    print(f"Number {x} is odd")
'''
    4. x, y, z (int). Afișează care este cel mai mare dintre ele?
'''
x, y, z = 4, 6, 1
if x > y and x > z:
    print(f"number {x} is bigger")
elif y > x and y > z:
    print(f"number {y} is bigger")
else:
    print(f"number {z} is bigger")
'''
    5. X, y, z - reprezintă unghiurile unui triunghi. Verifică și afișează dacă triunghiul este valid sau nu.
'''
a, b, c =  10, 11, 12
if a + b >= c and b + c >= a and a + c >= b:
    print("Triangle is valid")
else:
    print("Triangle is not valid")
'''
    6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
        ● Citiți de la tastatură un int x
        ● Afișează stringul fără ultimele x caractere
        Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
'''
string = 'Coral is either the stupidest animal or the smartest rock'
x = 7
print(string[:-x])
'''
    7.Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5
'''
new_string = string[0:6] + string[-5:]
print(new_string)
'''
    8. Același string.
        ● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
        ● Folosind această variabilă + slicing, afișează tot stringul până la acest cuvant
        ● output: 'Coral is either the stupidest animal or the smartest '
'''
index = string.index("rock")
print(string[0:index])
'''
    9. Citește de la tastatura un string
        Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
        Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat
'''
new_string = 'Coral is either the stupidest animal or the smartest roc'
first_charater = new_string[0]
last_character = new_string[-1]
assert first_charater.upper() == last_character.upper(), "First character and last character are not the same"
'''
    10. Avand stringul '0123456789'
        ● Afișați doar numerele pare
        ● Afișați doar numerele impare (hint: folositi slicing, controlați din pas)
'''
string = "0123456789"
print(string[0:len(string):2])
print(string[1:len(string):2])
'''
Exerciții Bonus (may need google) .
    11. Joc ghicit zarul
        Caută pe net și vezi cum se generează un număr random
        Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
        Luați un numărul ghicit de la utilizator
        Verificați și afișați dacă utilizatorul a ghicit
    
        Veți avea 3 opțiuni
            ● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
            ● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
            ● Ai ghicit. Felicitari! Ai ales x si zarul a fost y
'''
from random import randint

x = int(input("Enter the dice number from 1 to 6: "))
dice_roll = randint(1, 6)
if dice_roll > x:
    print(f"You lost. Number to low. You choose {x} but the number was {dice_roll}")
elif dice_roll < x:
    print(f"You lost. Number to high. You choose {x} but the number was {dice_roll}")
else:
    print(f"You won. Correct number. You choose {x} and the number is {dice_roll}")