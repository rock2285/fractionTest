from fraction import Fraction
import unittest

class TestInit(unittest.TestCase):
  #you should inspect the data members of self here, don't use __str__
  #several of these will need to check to see if an exception is raised
  def test_divZero(self):
    with self.assertRaises(ZeroDivisionError,msg="Denominator of zero fails to raise DivByZero"):
      a = Fraction(1,0)
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
    self.assertEqual(" 1/2 ",a.__str__())
  def test_displayInt(self):
    pass
  def test_displayNeg(self):
    pass
    
