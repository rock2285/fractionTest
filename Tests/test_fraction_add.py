import unittest

from fraction import Fraction

class TestFractionAdditions(unittest.TestCase)
    def test_add_two_fractions_same_denominator(self)
        self.assertEqual(Fraction(1, 4) + Fraction(2, 4), Fraction(3, 4))

    def test_add_by_integer(self)
        self.assertEqual(Fraction(2, 3) + 1, Fraction(5, 3))

    def test_add_by_zero
        self.assertEqual(Fraction(1, 5) + 0, Fraction(1, 5))

    def test_sum_is_reduced_to_lowest_terms(self):
        self.assertEqual(Fraction(3, 6) + Fraction(1, 6), Fraction(2, 3))

     def test_add_negative_fractions(self):
        self.assertEqual(Fraction(-1, 3) + Fraction(2, 3), Fraction(1, 3))

      def test_unsupported_operand_type_raises_type_error(self):
            with self.assertRaises(TypeError):
                Fraction(1, 2) + "not a fraction"
