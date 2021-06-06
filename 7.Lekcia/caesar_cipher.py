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

