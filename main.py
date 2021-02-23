from fraction import Fraction
import unittest

class TestInit(unittest.TestCase):
  def test_divZero(self):
    """
    with self.assertRaises(ZeroDivisionError):
      a=Fraction(1,0)
    """

class TestStr(unittest.TestCase):
  def test_display(self):
    a = Fraction(1,2)
    self.assertEquals(" 1/2 ",a.__str__())
    
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestInit)
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStr)
unittest.TextTestRunner().run(suite)