import unittest
from app import app

class Testprime(unittest.TestCase):
    def test_true_when_x_is_7(self):
        prime = app.is_prime(7)
        self.assertTrue(prime, 'True')

    def test_false_when_x_is_36(self):
        prime = app.is_prime(36)
        self.assertTrue(prime, 'False')
    
    def test_true_when_x_is_13219(self):
        prime = app.is_prime(13219)
        self.assertTrue(prime, 'True')

if __name__==('__main__'):
    unittest.main()