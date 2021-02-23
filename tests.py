from fraction import Fraction
import unittest

class TestInit(unittest.TestCase):
  def test_divZero(self):
    pass
  def test_default(self):
    pass
  def test_oneArg(self):
    pass
  def test_twoArg(self):
    pass
  def test_threeArg(self):
    pass
  def test_invalidArg(self):
    pass
  def test_negDenom(self):
    pass
  def test_reduced(self):
    pass

class TestStr(unittest.TestCase):
  def test_displayfraction(self):
    a = Fraction(1,2)
    self.assertEquals(" 1/2 ",a.__str__())
  def test_displayInt(self):
    pass
  def test_displayNeg(self):
    pass
    
