import unittest
from lib.integer.composite_and_prime import *


class TestSieve(unittest.TestCase):
    def test_sieve(self):
        primes = sieve(10000)
        self.assertListEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], primes[:10])
        self.assertEqual(7919, primes[999])
        self.assertNotIn(57, primes)
