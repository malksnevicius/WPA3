import random

riadok = int(input("Zadaj riadok:"))
stlpec = int(input("Zadaj stlpec:"))
maximum = int(input("Zadaj max:"))
minimum = int(input("Zadaj min:"))  # nemoyem dat min a max lebo to su funkcie a to by sme si ich potom zbytocne
# prepisali, alternativa je dat podtrznik min_ a max_, to potom nie je funkcia


outer_list = []

for y in range(riadok):
    inner_list = []  # alebo takto tiez sa to da: inner_list = list()
    for i in range(stlpec):
        inner_list.append(random.randint(minimum, maximum))
    outer_list.append(inner_list)

for inner in outer_list:
    for item in inner:
        print(f"{item:>10}", end="") # vypise inner tak ye oddleni cisla na 10 znakov, end="" - je, ze vypise vsetko a potom ide na novy riadok
    print()  # toto print nam da novy riadok
