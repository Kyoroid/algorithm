import unittest
from number_theory.prime import *
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
            'input': [252, ],
            'output': [[2, 2, 3, 3, 7], ]
        }
        dout = list(prime_factorization(data['input']))
        self.assertEqual(dout, data['output'])
        data = {
            'input': [252, 524287],
            'output': [[2, 2, 3, 3, 7], [524287,]]
        }
        dout = list(prime_factorization(data['input']))
        self.assertEqual(dout, data['output'])
        data = {
            'input': [1, ],
            'output': [[], ]
        }
        dout = list(prime_factorization(data['input']))
        self.assertEqual(dout, data['output'])

    def test_lcm(self):
        data = {
            'input': [7, 12, 13, 14],
            'output': 1092
        }
        self.assertEqual(lcm(data['input']), data['output'])
        data = {
            'input': [[7, 12, 13, 14], 103],
            'output': 62
        }
        self.assertEqual(lcm(*data['input']), data['output'])


if __name__ == '__main__':
    unittest.main()