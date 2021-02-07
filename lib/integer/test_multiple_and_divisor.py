import unittest
from lib.integer.multiple_and_divisor import *


class TestDivisor(unittest.TestCase):
    
    def test_list_divisors(self):
        actual = list_divisors(12)
        self.assertListEqual([1, 12, 2, 6, 3, 4], actual)
        actual = list_divisors(12, sorted=True)
        self.assertListEqual([1, 2, 3, 4, 6, 12], actual)


class TestMultiple(unittest.TestCase):

    def test_list_multiples(self):
        actual = list_multiples(3, 23)
        self.assertListEqual([3, 6, 9, 12, 15, 18, 21], actual)
        actual = list_multiples(3, 24)
        self.assertListEqual([3, 6, 9, 12, 15, 18, 21, 24], actual)


if __name__ == "__main__":
    unittest.main()
