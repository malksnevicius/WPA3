import random
from typing import List

def generate_matrix(rows: int, cols: int, min_: int, max_: int) -> List[list]:
    """ Generuje maticu cisel zo zadaneho rozsahu
    Ako vstupy sluzia min/max hodnot a pocty riadkov
    a stlpcov
    :param rows: int pocet riadkov
    :param cols: int pocet stlpcov
    :param min_: int minimalna hodnota
    :param max_: int maximalna hodnota
    :return:  list  s jednotlivymi riadkami
    """
    if not isinstance(rows, int) or not isinstance(cols, int) \
            or not isinstance(min_, int) or not isinstance(max_, int):
        raise TypeError("Inputs have to be integers")
    outer_list = []
    for _ in range(rows):
        inner_list = []   # inner_list = list()
        inner_list = []
        for _ in range(cols):
            inner_list.append(random.randint(min_, max_))
        outer_list.append(inner_list)
    return outer_list


print(f"__name__: {__name__}")
if __name__ == "__main__":
    rows = int(input("Zadaj pocet riadkov: "))
    cols = int(input("Zadaj pocet stlpcov: "))

    min_ = int(input("Zadaj minimalnu hodnotu: "))
    max_ = int(input("Zadaj maximalnu hodnotu: "))

    matrix = generate_matrix(rows, cols, min_, max_)
    for inner in matrix:
        for item in inner:
            print(f"{item:>10}", end="")
        print()