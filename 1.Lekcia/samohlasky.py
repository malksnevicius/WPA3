meno = input("Zadaj meno:")
meno = meno.lower()

# 1===================================================================================================
if meno.startswith("a") or meno.startswith("e") or meno.startswith("o") or meno.startswith("i") or \
    meno.startswith("u") or meno.startswith("y"):
    print("Tvoje eno zacina na samohlasku!")
else:
    print("Tvoje meno zacina na spoluhlasku")

# 2===================================================================================================
if meno.startswith("a"):
    print("Tvoje meno zacina na samohlasku")
elif meno.startswith("e"):
    print("Tvoje meno zacina na samohlasku")
elif meno.startswith("i"):
    print("Tvoje meno zacina na samohlasku")
elif meno.startswith("o"):
    print("Tvoje meno zacina na samohlasku")
elif meno.startswith("u"):
    print("Tvoje meno zacina na samohlasku")
elif meno.startswith("y"):
    print("Tvoje meno zacina na samohlasku")
else:
    print("Tvoje meno zacina na spoluhlasku")
