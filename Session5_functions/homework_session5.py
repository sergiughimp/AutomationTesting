'''
Exerciții obligatorii - grad de dificultate: Usor spre Mediu.
'''
'''
1.Funcție care să calculeze și să returneze suma a două numere
'''

def sum(number1, number2):
    return number1 + number2
print(sum(4,5))
'''
2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
'''
def is_number_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_number_even(3))
'''
3. Funcție care returnează numărul total de caractere din numele tău complet. (nume, prenume, nume_mijlociu)
'''

def total_characters(first_name, last_name, middle_name=""):
    return len(first_name) + len(last_name) + len(middle_name)
print(total_characters("Eva", "Evans", "Maria"))
print(total_characters("John","Tyson"))
'''
4. Funcție care returnează aria dreptunghiului
'''
def area_rectangle(length, width):
    return length * width
print(area_rectangle(3, 8))
'''
5. Funcție care returnează aria cercului
'''
def area_cirle(radius):
    return radius ** 2 * 3.14
print(area_cirle(4))
'''
6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.
'''
def find_character(character, string):
    return character in string
print(find_character("a","apple"))
'''
7. Funcție fără return, primește un string și printează pe ecran:
    ● Nr de caractere lower case este x
    ● Nr de caractere upper case este y
'''
def lower_upper_counter_characters(string):
    cnt_upper = 0
    cnt_lower = 0
    for character in string:
        if character.upper():
            cnt_upper += 1
        if character.lower():
            cnt_lower += 1
    print(f"Upper characters are {cnt_upper}")
    print(f"Lower characters are {cnt_lower}")
lower_upper_counter_characters("sadDa")
'''
8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu numerele pozitive
'''
def get_positive_numbers(list):
    positive_numbers = []
    for i in list:
        if i > 0:
            positive_numbers.append(i)
    return positive_numbers
print(get_positive_numbers([2, 3, 4, -2, -3]))
'''
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
    ● Primul număr x este mai mare decat al doilea nr y
    ● Al doilea nr y este mai mare decat primul nr x
    ● Numerele sunt egale.
'''
def check_bigger_number(number1, number2):
    if number1 > number2:
        print(f"Number {number1} is greater than {number2}")
    elif number1 < number2:
        print(f"Number {number1} is lower than {number2}")
    else:
        print(f"Number {number1} equals with {number2}")
check_bigger_number(5, 6)
'''
10. Funcție care primește un număr și un set de numere.
    ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
    ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
'''
def add_number_set(number, new_set):
    if number in new_set:
        print(f"Number {number} is already in the set")
        return False
    else:
        new_set.add(number)
        print(f"Number {number} was added to the set")
        return True
new_set = {4, 65, 7, 3, 8, 12}
print(new_set)
print(add_number_set(4, new_set))
'''
Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.
'''
'''
1. Funcție care primește o lună din an și returnează câte zile are acea luna
'''
def count_days_in_month(month):
    if month == "JAN" or month == "MARCH" or month == "MAY" or month == "JUL" or month == "AUG" or month =="OCT" or month == "DEC":
        counted_days = 31
        return counted_days
    elif month == "APR" or month == "JUN" or month == "SEP" or month == "NOV":
        counted_days = 30
        return counted_days
    else:
        counted_days = 28
        return counted_days
print(count_days_in_month("JAN"))
'''
2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.
    În final vei putea face:
        a, b, c, d = calculator(10, 2)
        ● print("Suma: ", a)
        ● print("Diferenta: ", b)
        ● print("Inmultirea: ", c)
        ● print("Impartirea: ", d)
'''
def calculator1(number1, number2, sign):
    if sign == "+":
        return number1 + number2
    elif sign == "-":
        return number1 - number2
    elif sign == "*":
        return number1 * number2
    elif sign == "/":
        return number1 / number2
print(calculator1(6, 4, "+"))
print(calculator1(6, 4, "-"))
print(calculator1(6, 4, "*"))
print(calculator1(6, 4, "/"))

# or
def calculator2(number1, number2):
    return number1 + number2, number1 - number2, number1 * number2, number1 / number2
a, b = 4, 5
sum, dif, mult, div = calculator2(a, b)
print(f"Result of {a} and {b} is: Sum {sum}, Difference {dif}, Produs {mult}, Division {div}")

'''
3. Funcție care primește o lista de cifre (adică doar 0-9)
    Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
    Returnează un DICT care ne spune de câte ori apare fiecare cifră
    => dict {
            0: 0
            1 :2
            2: 0
            3: 1
            4: 0
            5: 3
            6: 0
            7: 2
            8: 0
            9: 1
        }
'''
from pprint import pprint
def count_digits(list):
    new_dict = dict()
    for i in range(10):
        new_dict[i] = list.count(i)
    return new_dict
list = [1, 3, 1, 5, 9, 7, 7, 5, 5, 8, 9, 6, 7, 5, 7]
pprint(count_digits(list))

'''
4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
'''
def max_number(number1, number2, number3):
    if number1 > number2 and number1 > number3:
        return number1
    elif number2 > number1 and number2 > number3:
        return number2
    else:
        return number3
print(max_number(4, 5, 6))
'''
5. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr
    Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
'''
def sum_of_numbers(number):
    sum = 0
    for i in range(number + 1):
        sum += i
    return sum
print(sum_of_numbers(3))
'''
Exerciții Opționale - Bonus
'''
'''
1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune
    Exemplu:
        list1 = [1, 1, 2, 3]
        list2 = [2, 2, 3, 4]
        Răspuns: {2, 3}
'''
def common_numbers(list1, list2):
    new_list = []
    for item in list1:
        if item in list2:
            new_list.append(item)
    return new_list
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
print(common_numbers(list1, list2))
'''
2. Funcție care să aplice o reducere de preț
    Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
    Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e invalidă.
'''
def discount(price, discount):
    if 0 < discount <= 100:
        print("Discount is applied")
        price -= (discount * price) / 100
    else:
        print("Discount is not applied")
    return price
print(discount(139, 10))