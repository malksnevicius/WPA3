for year in range (1950, 1970, 1):
    print(year)
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Rok je prestupny")
    else:
        print("Rok je neprestupny")


