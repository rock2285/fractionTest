import unittest
 
from fraction import Fraction
 
class TestFractionAdd(unittest.TestCase):

def test_add_same_denominator(self):
  self.assertEqual(Fraction(1, 5) + Fraction(2, 5), Fraction(3, 5))

def test_add_different_denominators(self):
  self.assertEqual(Fraction(1,2) + Fraction(1,3), Fraction(5,6))

def test_add_result_is_reduced(self):
  self.assertEqual(Fraction(1, 6) + Fraction(1, 3), Fraction(1, 2))
