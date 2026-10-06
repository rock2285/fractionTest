import unittest
from fraction import Fraction

class TestFractionAdd(unittest.TestCase):
    def test_add_two_positive_fractions(self):
        self.assertEqual(Fraction(1, 3) + Fraction(1, 6), Fraction(1, 2))

    def test_add_integer_to_fraction(self):
        self.assertEqual(Fraction(3, 4) + 2, Fraction(11, 4))

    def test_add_zero(self):
        self.assertEqual(Fraction(5, 7) + 0, Fraction(5, 7))

    def test_add_negative_to_negative(self):
        self.assertEqual(Fraction(-2, 3) + Fraction(-1, 3), Fraction(-1, 1))

    def test_add_positive_to_negative(self):
      self.assertEqual(Fraction(-2, 3) + Fraction(3, 5), Fraction(-1, 15))

    def test_add_cancels_to_zero(self):
        self.assertEqual(Fraction(2, 3) + Fraction(-2, 3), Fraction(0, 1))

    def test_unsupported_type_raises_type_error(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) + "2"
