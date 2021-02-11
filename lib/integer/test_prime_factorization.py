import unittest
import math
from lib.integer.composite_and_prime import sieve
from lib.integer.prime_factorization import *


class TestPrimeFactorization(unittest.TestCase):
    
    def test_prime_factorization(self):
        actual_base, actual_count = prime_factorization(1)
        self.assertListEqual([1], actual_base)
        self.assertListEqual([1], actual_count)
        actual_base, actual_count = prime_factorization(2)
        self.assertListEqual([2], actual_base)
        self.assertListEqual([1], actual_count)
        actual_base, actual_count = prime_factorization(2696)
        self.assertListEqual([2, 337], actual_base)
        self.assertListEqual([3, 1], actual_count)
        actual_base, actual_count = prime_factorization(999999999988)
        self.assertListEqual([2, 11, 124847, 182041], actual_base)
        self.assertListEqual([2, 1, 1, 1], actual_count)
        actual_base, actual_count = prime_factorization(999999999989)
        self.assertListEqual([999999999989], actual_base)
        self.assertListEqual([1], actual_count)


    def test_prime_factorization_type_check(self):
        actual_base, actual_count = prime_factorization(999999999988)
        self.assertListEqual([int, int, int, int], [type(e) for e in actual_base])
        self.assertListEqual([int, int, int, int], [type(e) for e in actual_count])