import unittest
from lib.integer.multiple_and_divisor import *


class TestListDivisors(unittest.TestCase):
    
    def test_list_divisors(self):
        actual = list_divisors(12)
        self.assertListEqual([1, 12, 2, 6, 3, 4], actual)
        actual = list_divisors(12, sorted=True)
        self.assertListEqual([1, 2, 3, 4, 6, 12], actual)
    
    def test_list_divisors_type_check(self):
        actual = list_divisors(12, sorted=True)
        self.assertListEqual([int, int, int, int, int, int], [type(e) for e in actual])


class TestListMultiples(unittest.TestCase):

    def test_list_multiples(self):
        actual = list_multiples(3, 23)
        self.assertListEqual([3, 6, 9, 12, 15, 18, 21], actual)
        actual = list_multiples(3, 24)
        self.assertListEqual([3, 6, 9, 12, 15, 18, 21, 24], actual)


class TestCountDivisors(unittest.TestCase):

    def test_count_divisors(self):
        counts = count_divisors(17)
        actual = len(counts)
        self.assertEqual(18, actual)
        actual = counts[1]
        self.assertEqual(1, actual)
        actual = counts[17]
        self.assertEqual(2, actual)
        actual = counts[12]
        self.assertEqual(6, actual)
        actual = counts[16]
        self.assertEqual(5, actual)
