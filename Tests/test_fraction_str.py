from fraction import Fraction
import unittest

class test_fraction_str(unittest.TestCase):
  def test_displayfraction(self):
    a = Fraction(1,2)
    self.assertEqual(" 1/2 ",a.__str__())
  def test_displayInt(self):
    pass #if the denominator is 1, does display omit the /1?
  def test_displayNeg(self):
    pass #if the fraction is negative, is it possible to erroneously have it display 1/-2, vs -1/2?
    
