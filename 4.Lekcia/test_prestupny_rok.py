import prestupny_rok
from unittest import TestCase

print(f"__name__: {__name__}")

class TestPrestupnyRok(TestCase):
    def test_valid_leap(self):
        leap = prestupny_rok.leap_year(2000)
        self.assertIsNotNone(leap)
        self.assertTrue(leap)

    def test_valid_leap_not_100(self):
        leap = prestupny_rok.leap_year(1996)
        self.assertIsNotNone(leap)
        self.assertTrue(leap)

    def test_invalid_leap_100(self):
        leap = prestupny_rok.leap_year(1900)
        self.assertIsNotNone(leap)
        self.assertFalse(leap)

    def test_invalid_leap(self):
        leap = prestupny_rok.leap_year(1998)
        self.assertIsNotNone(leap)
        self.assertFalse(leap)

    def test_invalid_string(self):
        leap = prestupny_rok.leap_year("ahoj")
        self.assertIsNotNone(leap)
        self.assertFalse(leap)

    def test_invalid_float(self):
        leap = prestupny_rok.leap_year(1003.20)
        self.assertIsNotNone(leap)
        self.assertFalse(leap)






