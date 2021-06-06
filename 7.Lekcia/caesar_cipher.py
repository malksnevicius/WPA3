# ahoj, takze k rieseniam
# 1) uprava unittestov by sa robit nemala, tie testy mate ako kontrolu
# a zaroven ako pomoc pri vyvijani.. tj ak test kaze False, mala by si ten
# false dodrzat
# 2) ak som unittesty pustal, tak tiez neprechadzaju.

# false docielis tym, ze si na zaciaktu skontrolujes, ci je text naozaj str, ci
# je shift naozaj int, a ci je shift v rozmedzi 0-26
# if not isinstance(text, str):
#    return False
# if not isinstance(shift, int) or shift < 0 or shift > 26:
#    return False

# kazdopadne, tie kody su spravne, uplne v pohode sa to da takto pouzit
# ak teda doplnis veci do takeho stavu, aby to ficalo voci testom

def caesar_cipher(text: str, shift:int) -> str:
    """Gets text and encrypt it with cipher.

    :param text: str: to encrypt
    :param shift: int: right shift on the alphabet
    :return: str: encrypted text
    """
    abc_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
    abc_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]
    return_string = ""

    for char in text:
        if char in abc_lower:
            new_index = (abc_lower.index(char) + shift) % 26
            new_letter = abc_lower[new_index]
            return_string += new_letter
        elif char in abc_upper:
            new_index = (abc_upper.index(char) + shift) % 26 # skratene: new_letter = abc_upper[(abc_upper.index(char) + shift) % 26]
            new_letter = abc_upper[new_index]
            return_string += new_letter
        else:
            return_string += char
    return return_string



# decrypt je troska tricky, ale ked si uvedomis, ze decript je vlastne
# posun, ale opacny... tak sa da pouzit funkcia encrypt
# akurat spravis:
#
#   def decrypt_caesar(text: str, shift:int) -> str:
#       return encrypt_caesar(text, 26-shift)
#   a tymto si zariadis aj vsetky validacie aj vsetky potrebne veci
def decrypt_caesar(text: str, shift:int) -> str:
    """Gets encrypted caesar cipher and shift, and decrypt it

    :param text: str: to encrypt
    :param shift: int: right shift on the alphabet
    :return: str: encrypted text
    """
    abc_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
    abc_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]
    return_string = ""

    for char in text:
        if char in abc_lower:
            new_index = (abc_lower.index(char) - shift) % 26
            new_letter = abc_lower[new_index]
            return_string += new_letter
        elif char in abc_upper:
            new_index = (abc_upper.index(char) - shift) % 26 # skratene: new_letter = abc_upper[(abc_upper.index(char) + shift) % 26]
            new_letter = abc_upper[new_index]
            return_string += new_letter
        else:
            return_string += char
    return return_string


# brute force caesar je iba a len o tom, ze skusis dekryptovat kazdy text
# vsetkymi posunmi, a nasledne z toho listu precitas, ktora veta dava zmysel,
# tj to bude ta
