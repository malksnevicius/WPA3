year1 = int(input("Zadaj rok: "))
# year_count = int(input("Zadaj pocet rokov: "))
year2 = int(input("Zadaj rok: "))

# year = 2000
# end_year = year + year_count

# for year in range(year1, year2)
# while year1 < year2

while year1 <= year2:
    # year <= year + 10

    # 1x  2000 <= 2010
    # 2x  2001 <= 2011
    # 3x  2002 <= 2012
    if (year1 % 4 == 0 and year1 % 100 != 0) or year1 % 400 == 0:
        print(f"Rok {year1} je prestupny")
    year1 = year1 + 1
    # year += 1
    # year = year + 1
    # year *= 1
    # year = year * 1
    # year /= 1
    # year = year / 1
    # year -= 1
    # year = year - 1