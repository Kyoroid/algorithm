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


class TestPrimeFactorizationSPF(unittest.TestCase):
    def test_list_spf(self):
        spf = list_spf(12)
        self.assertListEqual([0, 1, 2, 3, 2, 5, 2, 7, 2, 3, 2, 11, 2], spf)

    def test_prime_factorization_spf(self):
        spf = list_spf(1000003)
        actual_base, actual_count = prime_factorization_spf(1, spf)
        self.assertListEqual([1], actual_base)
        self.assertListEqual([1], actual_count)
        actual_base, actual_count = prime_factorization_spf(2, spf)
        self.assertListEqual([2], actual_base)
        self.assertListEqual([1], actual_count)
        actual_base, actual_count = prime_factorization_spf(2696, spf)
        self.assertListEqual([2, 337], actual_base)
        self.assertListEqual([3, 1], actual_count)
        actual_base, actual_count = prime_factorization_spf(1000002, spf)
        self.assertListEqual([2, 3, 166667], actual_base)
        self.assertListEqual([1, 1, 1], actual_count)
        actual_base, actual_count = prime_factorization_spf(1000003, spf)
        self.assertListEqual([1000003], actual_base)
        self.assertListEqual([1], actual_count)

    def test_prime_factorization_spf_type_check(self):
        spf = list_spf(1000003)
        actual_base, actual_count = prime_factorization_spf(1000002, spf)
        self.assertListEqual([int, int, int], [type(e) for e in actual_base])
        self.assertListEqual([int, int, int], [type(e) for e in actual_count])
