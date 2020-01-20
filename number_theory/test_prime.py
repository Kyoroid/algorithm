import unittest
from prime import *
import itertools
import operator


class TestPrime(unittest.TestCase):

    def test_prime_sieve(self):
        data = {
            'input': 15, 
            'output': [2, 3, 5, 7, 11, 13]
        }
        self.assertEqual(prime_sieve(data['input']), data['output'])

    def test_prime_factorization(self):
        data = {
            'input': 252,
            'output': [2, 2, 3, 3, 7]
        }
        self.assertEqual(prime_factorization(data['input']), data['output'])
        data = {
            'input': 524287,
            'output': [524287, ]
        }
        self.assertEqual(prime_factorization(data['input']), data['output'])

    def test_lcm(self):
        data = {
            'input': [7, 12, 13, 14],
            'output': {2: 2, 3: 1, 5: 0, 7: 1, 11: 0, 13: 1}
        }
        self.assertEqual(lcm(data['input']), data['output'])


if __name__ == '__main__':
    unittest.main()