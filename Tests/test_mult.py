import unittest

from fraction import Fraction


class TestFractionMultiplication(unittest.TestCase):
    def test_multiplies_two_fractions(self):
        self.assertEqual(Fraction(1, 2) * Fraction(3, 4), Fraction(3, 8))

    def test_multiplies_fraction_by_integer(self):
        self.assertEqual(Fraction(2, 3) * 3, Fraction(2, 1))

    def test_multiplies_by_zero(self):
        self.assertEqual(Fraction(5, 7) * 0, Fraction(0, 1))

    def test_multiplies_negative_fractions(self):
        self.assertEqual(Fraction(-2, 3) * Fraction(9, -4), Fraction(3, 2))

    def test_product_is_reduced_to_lowest_terms(self):
        self.assertEqual(Fraction(6, 8) * Fraction(10, 9), Fraction(5, 6))

    def test_multiplication_does_not_modify_operands(self):
        first = Fraction(2, 3)
        second = Fraction(3, 5)

        result = first * second

        self.assertEqual(first, Fraction(2, 3))
        self.assertEqual(second, Fraction(3, 5))
        self.assertEqual(result, Fraction(2, 5))

    def test_unsupported_operand_type_raises_type_error(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) * "not a fraction"


if __name__ == "__main__":
    unittest.main()
