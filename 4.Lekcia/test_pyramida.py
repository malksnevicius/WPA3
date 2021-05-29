import pyramida
from unittest import TestCase


class TestPyramida(TestCase):
    def test_valid_5_normal_false(self):
        res = pyramida.create_pyramid(5, "normal", False)
        self.assertIsInstance(res, list)
        self.assertEqual(
            res,
            ["*", "**", "***", "****", "*****"]
        )

    def test_valid_5_reversed_false(self):
        res = pyramida.create_pyramid(5, "reversed", False)
        self.assertIsInstance(res, list)
        self.assertEqual(
            res,
            ["*****", "****", "***", "**", "*"]
        )

    def test_valid_5_normal_true(self):
        res = pyramida.create_pyramid(5, "normal", True)
        self.assertIsInstance(res, list)
        self.assertEqual(
            res,
            ["    *     ", "   * *    ", "  * * *   ", " * * * *  ", "* * * * * "]
        )

    def test_valid_5_reversed_true(self):
        res = pyramida.create_pyramid(5, "reversed", True)
        self.assertIsInstance(res, list)
        self.assertEqual(
            res,
            ["* * * * * ", " * * * *  ", "  * * *   ", "   * *    ", "    *     "]
        )

    def test_invalid_float_reversed_true(self):
        self.assertRaises(
            TypeError, pyramida.create_pyramid,
            5.0, "normal", True
        )

    def test_invalid_reversed_not_bool(self):
        self.assertRaises(
            TypeError, pyramida.create_pyramid,
            5, "normal", 31
        )

    def test_invalid_second_parameter(self):
        self.assertRaises(
            TypeError, pyramida.create_pyramid,
            5, "notnormal", True
        )

    def test_valid_0_reversed_true(self):
        res = pyramida.create_pyramid(0, "reversed", True)
        self.assertIsInstance(res, list)
        self.assertEqual(
            res,
            []
        )


class TestPyramida2(TestCase):
    def test_valid_5_normal_false(self):
        res = pyramida.create_pyramid_2(5, "normal", False)
        self.assertIsInstance(res, list)
        self.assertEqual(
            res,
            ["*", "**", "***", "****", "*****"]
        )

    def test_valid_5_reversed_false(self):
        res = pyramida.create_pyramid_2(5, "reversed", False)
        self.assertIsInstance(res, list)
        self.assertEqual(
            res,
            ["*****", "****", "***", "**", "*"]
        )

    def test_valid_5_normal_true(self):
        res = pyramida.create_pyramid_2(5, "normal", True)
        self.assertIsInstance(res, list)
        self.assertEqual(
            res,
            ["    *     ", "   * *    ", "  * * *   ", " * * * *  ", "* * * * * "]
        )

    def test_valid_5_reversed_true(self):
        res = pyramida.create_pyramid_2(5, "reversed", True)
        self.assertIsInstance(res, list)
        self.assertEqual(
            res,
            ["* * * * * ", " * * * *  ", "  * * *   ", "   * *    ", "    *     "]
        )

    def test_invalid_float_reversed_true(self):
        self.assertRaises(
            TypeError, pyramida.create_pyramid_2,
            5.0, "normal", True
        )

    def test_invalid_reversed_not_bool(self):
        self.assertRaises(
            TypeError, pyramida.create_pyramid_2,
            5, "normal", 31
        )

    def test_invalid_second_parameter(self):
        self.assertRaises(
            TypeError, pyramida.create_pyramid_2,
            5, "notnormal", True
        )

    def test_valid_0_reversed_true(self):
        res = pyramida.create_pyramid_2(0, "reversed", True)
        self.assertIsInstance(res, list)
        self.assertEqual(
            res,
            []
        )