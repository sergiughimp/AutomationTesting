'''
1. Declară o listă note_muzicale în care să pui do re mi etc până la do
    ● Afișeaz-o
    ● Inversează ordinea folosind slicing și suprascrie această listă.
    ● Printează varianta actuală (inversată).
    ● Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
    ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.
Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face suprascrierea automat și permanentizează aceste modificări. Ambele variante își găsesc utilitatea în funcție de ce ne dorim în acel moment.
'''
musical_notes = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
print(musical_notes)
musical_notes = musical_notes[::-1]
print(musical_notes)
musical_notes.reverse()
print(musical_notes)

assert musical_notes == ["do", "re", "mi", "fa", "sol", "la", "si", "do"], "Musical notes are not the same"
'''
2. De câte ori apare ‘do’?
'''
count_do = musical_notes.count("do")
print(count_do)
'''
3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4] Găsește 2 variante să le unești într-o singură listă.
'''
list_x = [3, 1, 0, 2]
list_y = [6, 5, 4]
list_z = list_x + list_y
print(list_z)
list_x.extend(list_y)
print(list_x)
'''
4.
    ● Sortează și afișază lista generată la exercițiul anterior.
    ● Sortează numărul 0 folosind o funcție.
    ● Afișaza iar lista.
'''
list_z.sort()
print(list_z)
list_z.remove(0)
print(list_z)
'''
5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
    ● Lista este goală.
    ● Lista nu este goală.
'''
if list_z:
    print("the list is not empty")
else:
    print("the list is empty")
'''
6. Folosește o funcție care să șteargă lista de la exercițiul 3.
'''
list_z.clear()
print(list_z)
'''
7. Copy paste la exercițiul 5. Verifică încă o dată. Acum ar trebui să se afișeze că lista e goală.
'''
if list_z:
    print("the list is not empty")
else:
    print("the list is empty")
'''
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}. Folosește o funcție că să afișezi Elevii (cheile)
'''
dict1 = {
    "Ana": 8,
    "Gigel": 10,
    "Dorel": 5
}
print(dict1.keys())
for key, value in dict1.items():
    print(key)
'''
9. Printează cei 3 elevi și notele lor
    Ex: ‘Ana a luat nota {x}’
    Doar nota o vei lua folosindu-te de cheie
'''
for key, value in dict1.items():
    print(f"{key} a luat nota {value}")
'''
10. Dorel a făcut contestație și a primit 6
    ● Modifică nota lui Dorel în 6
    ● Printează nota după modificare
'''
dict1["Dorel"] = 6
print(dict1)
'''
11. Gigel se transferă din clasă
    ● Căuta o funcție care să îl șteargă
    ● Vine un coleg nou. Adaugă Ionică, cu nota 9
    ● Printează noii elevi
'''
del dict1["Gigel"]
dict1["Ionica"] = 9
print(dict1)

# or
dict1.update({
    "David": 9,
    "Adela": 4
})
print(dict1)
'''
12. Set
    zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
    weekend = {'sâmbăta', 'duminică'}
    ● Adaugă în zilele_sapt ‘luni’
    ● Afișeaza zile_sapt
'''
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add("luni")
print(zile_sapt)
'''
13.Folosește un if și verifică dacă:
    ● Weekend este un subset al zilelor din săptămânii.
    ● Weekend nu este un subset al zilelor din săptămânii.
'''
if weekend.issubset(zile_sapt):
    print("weekend is a subset of the zile_sapt")
else:
    print("weekend is not a subset of the zile_sapt")
'''
14. Afișează diferențele dintre aceste 2 seturi.
'''
print(zile_sapt.difference(weekend))
'''
15. Afișază intersecția elementelor din aceste 2 seturi.
'''
print(zile_sapt.intersection(weekend))
'''
Exerciții Opționale - grad de dificultate: Mediu spre greu(may need google) .
1. Ne imaginăm o echipă de fotbal pt teren sintetic.
    3 Schimbări maxime admise:
        ● Declară o Listă cu 5 jucători
        ● Schimbari_efectuate = te joci tu cu valori diferite
        ● Schimbari_max = 3
    Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
        - Efectuează schimbarea
        - Șterge jucătorul scos din listă
        - Adaugă jucătorul intrat
        - Afișaza a intra x, a ieșit y, mai ai z schimbări
    Dacă jucătorul nu e în teren:
        - Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
        - Afișază ‘mai ai z schimbări’
    Testează codul cu diferite valori
'''
import random
players = ["p1", "p2", "p3", "p4", "p5"]
changes = 0
max_changes = 3
negative_tries = 0
random.shuffle(players)

while 0 < max_changes <= 3:
    answer_user = input("Do you want to make a change of the players? (yes/no) \n")
    if answer_user.lower() == "yes":
        print("yes")
        player_out = input("What player do you want to take out? \n")
        while player_out not in players:
            print(f"player {player_out} doesn't exist")
            player_out = input("Choose another player to take out")

        players.remove(player_out)
        print(f"you removed the player {player_out} \n")

        player_in = input("What player do you want to send in? \n")
        while player_in in players:
            print(f"{player_in} is already in the list")
            player_in = input("Choose another player to send in")

        players.append(player_in)
        print(f"you send in the player {player_in} \n")

        max_changes -= 1
        changes += 1

        print(f"The change was successfully between player {player_out} and {player_in}")
        print(f"Final list of players after the {changes} changes is: {players}")
    elif answer_user.lower() == "no":
        print("no")
        print(f"List of players is {players}")
        negative_tries += 1
        if negative_tries == 5:
            break
    else:
        print("You can't make any changes. You have to answer with 'yes' or with 'no'")
print(f"Negative tries {negative_tries}")
print(f"You did all {changes} changes of the players in the game. Game is ended.")