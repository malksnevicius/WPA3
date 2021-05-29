from typing import List


def create_pyramid(base: int, orientation: str, center: bool) -> List[str]:
    """ vyrobi pyramidu na zaklade vstupov
    :param base: int  pocet * zakladne
    :param orientation: str reversed, normal
    :param center: bool  true / false
    :return: list  s riadkami pyramidy
    """
    if not isinstance(base, int) or not isinstance(orientation, str) \
            or not isinstance(center, bool) or orientation not in ['normal', 'reversed']:
        raise TypeError("Input parameters are: base: int, orientation: str[normal, reversed], center: bool")
    pyramid = []

    for i in range(base):
        if orientation == "normal":
            row = "*"*(i+1)
        else:
            row = "*" * (base - i)
        pyramid.append(row)

    if center: # prednaska 5 - 0:22 cas,
        for idx, value in enumerate(pyramid):
            centered = ""
            for char in value:
                centered += f"{char} "
            pyramid[idx] = f"{centered:^{base*2}}"

    return pyramid


def create_pyramid_2(base: int, orientation: str, center: bool) -> List[str]:
    """ vyrobi pyramidu na zaklade vstupov
    Pouzite su iba list comprehension a inline if
    :param base: int  pocet * zakladne
    :param orientation: str reversed, normal
    :param center: bool  true / false
    :return: list  s riadkami pyramidy
    """
    if not isinstance(base, int) or not isinstance(orientation, str) \
            or not isinstance(center, bool) or orientation not in ['normal', 'reversed']:
        raise TypeError("Input parameters are: base: int, orientation: str[normal, reversed], center: bool")
    basic = ["*"*(i+1) if orientation == "normal" else "*"*(base-i) for i in range(base)]
    pyramid = [f"{''.join([f'{char} ' for char in value]):^{base*2}}" for value in basic] if center else basic
    return pyramid


if __name__ == "__main__":
    pyramida = create_pyramid(5, "reversed", True)
    for x in pyramida:
        print(x)
