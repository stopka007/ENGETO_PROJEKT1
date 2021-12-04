'''
author = Štěpán Nižník
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
oddelovac = "-" * 30
#input uzivatele
registered_users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
user = input("Username: ")
password = input("Password: ")
print(oddelovac)

#zjisteni jestli je uzivatel registrovany a jestli zadal spravne uzivatelske jmeno a heslo
if password == registered_users.get(user):
    print(f"Welcome to the app, {user}.")
else:
    print("Invalid Username or Password.")
    exit()
print(oddelovac)

#Vybrani ktery text chce uzivatel zanalyzovat
cislo_textu = input("With number between 1 to 3, choose a text you want to analyze: ")

#Zjisteni jestli je cislo spravne zadano, jestli je to cislo v urcity vzdalenosti
if cislo_textu.isdigit() and int(cislo_textu) in range(1, len(TEXTS) + 1):
    print(f"You chose text number {cislo_textu}.")
    cislo_textu = int(cislo_textu) - 1
else:
    print("Invalid number.")
    exit()
print(oddelovac)

#Rozdeleni textu na jednotliva slova a vytvoreni slovniku
jednotliva_slova = TEXTS[cislo_textu].split()
text = []
for word in jednotliva_slova:
    #rozdeleni buff-to-white na jednotliva slova a pridani do slovniku text
    if "-" in word:
        jednotliva_slova = word.replace("-", " ")
        text.extend(jednotliva_slova.split())
    #pridani ostatni slov do slovniku a odstraneni tecky,carky
    else:
        text.append(word.strip(".,"))

#vypsat kolik slov je ve vybranem textu
number_of_words = len(text)
print(f"There are {number_of_words} words.")

#vypsat slova ktere zacinaji na velke pismeno
titlecase_words = 0
for word in text:
    if word[0].isupper():
        titlecase_words += 1
print(f"There are {titlecase_words} titlecase words.")

#vypsat slova psana velkymi pismeny
uppercase_words = 0
for word in text:
    if word.isupper() and word.isalpha():
        uppercase_words += 1
print(f"There are {uppercase_words} uppercase words.")

#vypsat slova psana malymi pismeny
lowercase_words = 0
for word in text:
    if word.islower():
        lowercase_words += 1
print(f"There are {lowercase_words} lowercase words.")

#vypsat pocet cisel
number_of_numbers = 0
for word in text:
    if word.isdigit():
        number_of_numbers += 1
print(f"There are {number_of_numbers} numbers.")

#suma cisel v textu
sum_numbers = 0
for word in text:
    if word.isdigit():
        sum_numbers += int(word)
print(f"Sum of all numbers is {sum_numbers}.")
print(oddelovac)

#spocitat kolikrat je v textu slovo s urcitou delkou
cetnost_delek = {}
for word in text:
    if len(word) not in cetnost_delek:
        cetnost_delek[len(word)] = 1
    else:
        cetnost_delek[len(word)] += 1

#Vypsani vysledku
hvezdicka = "*"
nejvetsi = max(cetnost_delek.values())
print(f"LEN|{'OCCURENCES':^{nejvetsi}}|NR.")
print(oddelovac)
for delka, pocet in enumerate(cetnost_delek.keys(), 1):
    #if abychom vynechali urcitou delku slova pokud se neobjevuje ani jednou a pozdeji tim padem nenasobili non-typem "none"
    if cetnost_delek.get(delka) == None:
        continue
    else:
        print(f"{delka:^3}|{hvezdicka * cetnost_delek.get(delka):^{nejvetsi}}|{cetnost_delek.get(delka)}", sep="\n")

print(oddelovac)