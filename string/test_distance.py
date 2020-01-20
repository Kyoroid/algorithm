import unittest
from distance import *

class TestDistance(unittest.TestCase):

    def test_levenshtein(self):
        data = {
            'input': ['nashorn', 'nginx'],
            'output': 6
        }
        self.assertEqual(levenshtein(*data['input']), data['output'])

if __name__ == '__main__':
    unittest.main()