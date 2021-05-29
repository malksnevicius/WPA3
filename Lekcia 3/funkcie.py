# word = input("Vloz slovo: ") # -> retazec -> premennej word


# def moja_prva_funkcia(string):
#     number = int(string)
#     return number
#
#
# cislo = moja_prva_funkcia("150")
# print(cislo)
# print(type(cislo))
#

def funkcia1():
    print("Funkcia1")


def funkcia2(parameter1, parameter2):
    print(f"Funkcia2 -> {parameter1}, {parameter2}")


def funkcia3(parameter1="Ahoj"):
    print(f"Moja_Funkcia3 -> {parameter1}")


def funkcia4(parameter1, parameter2="Ahoj"):
    print(f"Funkcia4 -> {parameter1}, {parameter2}")


funkcia1()
funkcia2("Ahoj", "Svet")

funkcia3()
funkcia3()
funkcia3()
funkcia3()
funkcia3()
funkcia3()
funkcia3("Svet")

funkcia4("Ahoj")
funkcia4("Ahoj", "SVET!")

# print("VSTUP Z KLAVESNICE")
# vstup = input("Zadaj retazec: ")
# funkcia3(vstup)