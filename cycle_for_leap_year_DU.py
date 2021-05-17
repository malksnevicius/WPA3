year = ["1950", "1951", "1952", "1953", "1954", "1955", "1956", "1957", "1958", "1959", "1960"]

for year in range (1950, 1970, 1):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Rok je prestupny")
    else:
        print("Rok je neprestupny")

# Tomas, neviem ako do odpovede dostat aj roky,a za tym potom hlasku ci je rok prestupny alebo neprestupny
# na dnes uz musim skoncit, mozno este zajtra nieco vylepsim
