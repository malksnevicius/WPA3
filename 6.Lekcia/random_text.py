import random
import string


def random_text(dlzka: int) -> str:
    """ Returns random string of 'dlzka'
    :param dlzka:  int   length of string
    :return: str  string of given  length
    """
    return "".join(random.choices(f"{string.ascii_letters} 1234567890", k=dlzka))
    #    "".join(["d", "3", "v", "4"])
    #    "|AHOJ|".join(["d", "3", "v", "4"])


if __name__ == "__main__":
    rnd_text = random_text(250)
    print(rnd_text)
    number_list = [int(znak) for znak in rnd_text if znak.isdigit() and int(znak) % 2 == 0]
    print(number_list)
    print(list(set(number_list)))   # [2, 6, 2, 8]