import matrix
from unittest import TestCase

print(f"__name__: {__name__}")

class TestGenerateMatrix(TestCase):
    def test_valid_input(self):
        result = matrix.generate_matrix(1, 1, 2, 2)
        self.assertEqual(result, [[2]])

    def test_valid_input_more_rows(self):
        result = matrix.generate_matrix(3, 1, 2, 2)
        self.assertEqual(result, [[2], [2], [2]])

    def test_valid_input_more_cols(self):
        result = matrix.generate_matrix(1, 3, 2, 2)
        self.assertEqual(result, [[2, 2, 2]])

    def test_valid_input_more_rows_cols(self):
        result = matrix.generate_matrix(2, 3, 2, 2)
        self.assertIsInstance(result, list)
        self.assertEqual(result, [[2, 2, 2], [2, 2, 2]])

    def test_invalid_input_rows(self):
        self.assertRaises(
            TypeError, matrix.generate_matrix, "a", 3, 2, 2
        )

    def test_invalid_input_cols(self):
        self.assertRaises(
            TypeError, matrix.generate_matrix, 2, 3.0, 2, 2
        )

    def test_invalid_input_min_(self):
        self.assertRaises(
            TypeError, matrix.generate_matrix, 2, 3, "a", 2
        )

    def test_invalid_input_max_(self):
        self.assertRaises(
            TypeError, matrix.generate_matrix, 2, 3, 1, 2.0
        )

    def test_zeroes_input(self):
        result = matrix.generate_matrix(0, 0, 0, 0)
        self.assertEqual(result, [])