   # ZVYSOK PO DELENI ->    5 % 2 = 1

# VSTUP ->  input("zadaj year")
# VYSTUP ->  ci je year prestupny

year = input("Input year: ")
year = int(year)
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Rok je PRESTUPNY")
        else:
            print("Rok je NEPRESTUPNY")
    else:
        print("Rok je PRESTUPNY")
else:
    print("Rok je NEPRESTUPNY")


if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Rok je prestupny")
else:
    print("Rok je neprestupny")
