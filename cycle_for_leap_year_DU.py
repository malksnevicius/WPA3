# chybaju ti tu vstupy, samostatne takto ten kod nieje spustitelny
# nieco ako     year1=input()

# 1 chybicka je, ze tento rozsah sa vygeneruje ako  [1950, 1969)
# chceli sme, aj ked to nebolo presne definovane [1950, 1970] takze pri rangi
# treba pridat  1970+1  (ak chceme do 1970 generovat)
# 3ti parameter 1 netreba davat, by default 1, ta tam je
for year in range (1950, 1970, 1):
    print(year)
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Rok je prestupny")
        # stacilo podla zadania vypisat iba prestupne roky
    else:
        print("Rok je neprestupny")


