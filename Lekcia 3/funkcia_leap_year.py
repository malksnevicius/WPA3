# type hints
def leap_year(year: int) -> bool:
    """ Function for checking of leap years
    :param year: int year
    :return: bool true/false
    """
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


year = int(input("Zadaj rok: "))

leap = leap_year(year)


if leap:
    print(f"Rok {year} je prestupny")


cislo = 10
if cislo and cislo == 10:
    print("cislo je zadane")

retazec = "ahoj"
if retazec and retazec == "ahoj":
    print("retazec je zadany")

retazec = ""
if retazec:
    print("retazec je zadany")

# True -> 1
# False -> 0
# number = 100   # -100, 100
number = 0
if number:
    pass
# number = None
if 0 <= number >= 0:    # if 0: ...   if 0: ....    -> False   if False  ->  if False == True
    print("nieco vykonavam")

if number % 2 == 0:
    print('parne')

if not number % 2:  # ->  if not (number % 2 => 0) ->  if not 0  -> if not False  ->  not False -> True -> if True
    print("parne")