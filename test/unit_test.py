import unittest
from app import app

class AppTestCase(unittest.TestCase):

  def test_be_0_when_x_is_0(self):
    res = app.calc(0)
    self.assertEqual(res, '0')

  def test_be_15_when_x_is_3(self):
    res = app.calc(3)
    self.assertEqual(res, '15')

  def test_be_4dot5_when_x_is_7dot5(self):
    res = app.calc(1.5)
    self.assertEqual(res, '7.5')

if __name__ == "__main__":
    unittest.main()