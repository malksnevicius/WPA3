cislo = input("Zadaj cislo:")

if cislo == "10":  # porovnam ci vstup z klavesnice je 10
    # str  == str
    print(f"{cislo} a je rovne 10")  # ak je 10, vypisem
    print("IF")
elif cislo == "11":  # INAK ak vstup z klavesnice je 11
    # str == str
    print(f"{cislo} a je rovne 11")
    print("ELIF")
else:  # INAK (v opacnom pripade) vypisem toto
    print(f"{cislo} nieje ani 10 ani 11")
    print("ELSE")