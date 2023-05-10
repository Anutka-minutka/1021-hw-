import unittest
from lesson9 import*
class my_test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(2,2),4)
if __name__=='__main__':
    unittest.lesson9()
