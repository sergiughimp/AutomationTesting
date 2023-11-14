'''
Exerciții obligatorii - grad de dificultate: Usor spre Mediu .
1.Având lista:
    mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
    Folosește un for că să iterezi prin toată lista și să afișezi;
        ● ‘Mașina mea preferată este x’.
        ● Fă același lucru cu un for each.
        ● Fă același lucru cu un while.
'''
cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for i in range(0, len(cars)):
    print(f"My favourite car is {cars[i]}")

for car in cars:
    print(f"My favourite car is {car}")

i = 0
while i < len(cars):
    print(f"My favourite car is {cars[i]}")
    i += 1
'''
2. Aceeași listă:
Folosește un for else
    În for
        - Modifică elementele din listă astfel încât să fie scrie cu majuscule, exceptând primul și ultimul.
    În else:
        - Printează lista.
'''
for i in range(0, len(cars)):
    if i == 0 or i == len(cars):
        continue
    cars[i] = cars[i].upper()
else:
    print(cars)

'''
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes. Itereaza prin ea prin modalitatea aleasă de tine.
    Dacă mașina e mercedes:
        Printează ‘am găsit mașina dorită de dvs’
        Ieși din ciclu folosind un cuvânt cheie care face acest lucru
    Altfel:
        Printează ‘Am găsit mașina X. Mai căutam‘
'''
cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for car in cars:
    if car == "Mercedes":
        print(f"We found the car {car} that you are looking for")
        break
    else:
        print(f"The car is  {car}. Keep looking for the car")
'''
4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
    - Dacă mașina e Trabant sau Lăstun:
        Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
    - Printează S-ar putea să vă placă mașina x.
'''
for car in cars:
    if car == "Trabant" or car == "Lăstun":
        continue
    print(f"You may like this car {car}")
'''
5. Modernizează parcul de mașini:
    ● Crează o listă goală, masini_vechi.
    ● Itereaza prin mașini.
    ● Când găsesti Lăstun sau Trabant:
        - Salvează aceste mașini în masini_vechi.
        - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
    ● Printează Modele vechi: x.
    ● Modele noi: x.
'''
cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
old_cars = []
for i in range(len(cars)):
    if cars[i] == "Trabant" or cars[i] == "Lăstun":
        old_cars.append(cars[i])
        cars[i] = "Tesla"
print(old_cars)
print(cars)
'''
6. Având dict:
    pret_masini = {
        'Dacia': 6800,
        'Lăstun': 500,
        'Opel': 1100,
        'Audi': 19000,
        'BMW': 23000
    }
    Vine un client cu un buget de 15000 euro.
        ● Prezintă doar mașinile care se încadrează în acest buget.
        ● Itereaza prin dict.items() și accesează mașina și prețul.
        ● Printează Pentru un buget de sub 15000 euro puteți alege mașină x Lastun
        ● Iterează prin listă.
'''
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
budget = 15000
for car_name, car_price in pret_masini.items():
    if car_price > budget:
        continue
    print(f"For a budget less than {budget} you can pick the car {car_name}")
'''
7. Având lista:
    numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
        ● Iterează prin ea.
        ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
'''
numbers = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
count_3 = 0
for number in numbers:
    if number == 3:
        count_3 += 1
print(count_3)
'''
8. Aceeași listă:
    ● Iterează prin ea
    ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
'''
sum = 0
for number in numbers:
    sum += number
print(sum)
'''
9. Aceeași listă:
    ● Iterează prin ea.
    ● Afișază cel mai mare număr (nu ai voie să folosești max).
'''
max_number = -9999
for number in numbers:
    if number > max_number:
        max_number = number
print(max_number)
'''
10. Aceeași listă:
    ● Iterează prin ea.
    ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
    Ex: dacă e 3, să devină -3
        ● Afișază noua listă.
'''
for i in range(len(numbers)):
    if numbers[i] > 0:
        numbers[i] = -numbers[i]
print(numbers)
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
other_numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
even_numbers = []
odd_numbers = []
positive_numbers = []
negative_numbers = []
for number in other_numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    elif number % 2 != 0:
        odd_numbers.append(number)
    if number > 0:
        positive_numbers.append(number)
    elif number < 0:
        negative_numbers.append(number)
print(even_numbers)
print(odd_numbers)
print(positive_numbers)
print(negative_numbers)

'''
2. Aceeași listă:
    Ordonează crescător lista fară să folosești sort.
    Te poți inspira vizual de aici.
    https://www.youtube.com/watch?v=lyZQPjUT5B4
'''
other_numbers = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for i in range(0, len(other_numbers)):
    for j in range(i + 1, len(other_numbers)):
        if other_numbers[i] > other_numbers[j]:
            other_numbers[i], other_numbers[j] = other_numbers[j], other_numbers[i]
print(other_numbers)
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

number_guessed = False
while number_guessed == False:
    secret_number = int(input("Enter a number from 1 to 30: "))
    random_number = randint(1, 30)
    if secret_number > random_number:
        print(f"Number {secret_number} is bigger than {random_number}")
    elif secret_number < random_number:
        print(f"Number {secret_number} is lower than {random_number}")
    elif secret_number == random_number:
        print(f"Congratulations! You guessed the number!")
    number_guessed = True
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

number = 7
for i in range(1, number+1):
    for j in range(1, i + 1):
        print(i, end="")
    print()
'''
5.
    tastatura_telefon = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [0]
    ]
    Iterează prin listă 2d
    Printează ‘Cifra curentă este x’
    (hint: nested for - adică for în for)
'''
phone_keyboard = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for numbers in phone_keyboard:
    for digit in numbers:
        print(f"The current number is {digit}")