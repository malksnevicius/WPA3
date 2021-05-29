def leap_year(year):
    """ Function for lear year validation
    :param year: int year
    :return: bool  True / False
    """
    # ci je vstup int, ak chcem zistit typ tak pouziva sa instancia - isinstance()
    if not isinstance(year, int):
        return False
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

print(f"__name__: {__name__}")