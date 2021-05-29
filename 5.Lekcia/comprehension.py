leap_years = [year for year in range(int(input("Zadaj prvy rok: ")), int(input("Zadaj posledny rok: ")))\
              if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0]
print(leap_years)