import unittest
from number_theory.modular import *


class TestModular(unittest.TestCase):

    def test_modpow(self):
        data = {
            'input': [2, 1000000000, 10**9+7],
            'output': 140625001
        }
        self.assertEqual(modpow(*data['input']), data['output'])

if __name__ == '__main__':
    unittest.main()