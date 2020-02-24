import unittest
from number_theory.prime import *


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


if __name__ == '__main__':
    unittest.main()
