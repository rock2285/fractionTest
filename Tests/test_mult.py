from fraction import Fraction
import unittest


class test_fraction_mult(unittest.TestCase):
  def test_multiply_two_fractions(self):
    self.assertEqual(Fraction(1, 2) * Fraction(2, 3), Fraction(1, 3))

  def test_multiply_by_integer(self):
    self.assertEqual(Fraction(3, 4) * 2, Fraction(3, 2))

  def test_multiply_zero(self):
    self.assertEqual(Fraction(5, 7) * 0, Fraction(0, 1))

  def test_multiply_negative_values(self):
    self.assertEqual(Fraction(-2, 3) * Fraction(3, 5), Fraction(-2, 5))
    self.assertEqual(Fraction(-2, 3) * Fraction(-3, 5), Fraction(2, 5))

  def test_unsupported_type_raises_type_error(self):
    with self.assertRaises(TypeError):
      Fraction(1, 2) * "2"
