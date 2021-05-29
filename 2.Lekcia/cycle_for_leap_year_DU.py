year1 = input("Zadaj prvy rok:")
year2 = input("Zadaj druhy rok:")

year1 = int(year1)
year2 = int(year2)

for year in range (year1, (year2 + 1)):
    print(year)
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Rok je prestupny")


