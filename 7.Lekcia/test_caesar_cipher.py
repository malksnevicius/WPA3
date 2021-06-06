from unittest import TestCase
from caesar_cipher import caesar_cipher, decrypt_caesar

# Tomas, venovala som tomuto dnes par hodin
# ale nedopracovala somsa k prejdeniu vsetkcyh testov
# pri testoch kde shift nebol v ramci 1-26, som skusala self.isinstance
# a tiez self.assertFalse ale nemam spravne riesenie

class TestCeasarCipher(TestCase):
    def test_caesar_cipher_standard(self):
        result = caesar_cipher("ahoj svet!", 1)
        self.assertEqual(result, "bipk twfu!")

    def test_caesar_cipher_upper_lower(self):
        result = caesar_cipher("Ahoj Svet!", 1)
        self.assertEqual(result, "Bipk Twfu!")

    def test_caesar_cipher_index_more_than_26(self):
        self.assertRaises(
            TypeError, caesar_cipher.,
            "Ahoj Svet!", 277
        )
    def test_caesar_cipher_index_less_than_0(self):
        self.assertRaises(
            TypeError, caesar_cipher,
            "Ahoj Svet!", -200
        )

    def test_caesar_cipher_index_cross_z(self):
        result = caesar_cipher("ZzZzZz", 1)
        self.assertEqual(result, "AaAaAa")

    def test_caesar_cipher_special_chars(self):
        result = caesar_cipher(" $#$*@#&$@#!?.,", 10)
        self.assertEqual(result, " $#$*@#&$@#!?.,")

    def test_caesar_cipher_non_text(self):
        result = caesar_cipher(23, 1)
        self.assertRaises(TypeError, caesar_cipher, 23)


class TestCeasarCipherDecrypt(TestCase):
    def test_caesar_cipher_standard(self):
        result = decrypt_caesar("bipk twfu!", 1)
        self.assertEqual(result, "ahoj svet!")

    def test_caesar_cipher_upper_lower(self):
        result = decrypt_caesar("Bipk Twfu!", 1)
        self.assertEqual(result, "Ahoj Svet!")

    def test_caesar_cipher_index_more_than_26(self):
        self.assertRaises(
            TypeError, decryt_caesar,
            "Ahoj Svet!", 277
        )

    def test_caesar_cipher_index_less_than_0(self):
        result = decrypt_caesar("Ahoj Svet!", -60)
        self.assertRaises(
            TypeError, decrypt_caesar,
            "Ahoj Svet!", -60
        )

    def test_caesar_cipher_index_cross_z(self):
        result = decrypt_caesar("ZzZzZz", 1)
        self.assertEqual(result, "YyYyYy")

    def test_caesar_cipher_index_cross_a(self):
        result = decrypt_caesar("AaAaAa", 1)
        self.assertEqual(result, "ZzZzZz")

    def test_caesar_cipher_index_special_chars(self):
        result = decrypt_caesar(" $#$*@#&$@#!?.,", 10)
        self.assertEqual(result, " $#$*@#&$@#!?.,")

