import unittest
from combination.counting import *
import itertools
import operator


class TestCounting(unittest.TestCase):

    def test_nCk_mod_v1(self):
        data = {
            'input': [4, 2],
            'output': 6,
            'mod': 10**9 + 7
        }
        self.assertEqual(nCk_mod_v1(*data['input']), data['output'])
        data = {
            'input': [10000, 4000],
            'output': 306267707,
            'mod': 10**9 + 7
        }
        self.assertEqual(nCk_mod_v1(*data['input']), data['output'])
    


if __name__ == '__main__':
    unittest.main()
