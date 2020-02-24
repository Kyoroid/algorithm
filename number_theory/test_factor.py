import unittest
from number_theory.factor import *


class TestFactor(unittest.TestCase):

    def test_modlcm(self):
        data = {
            'input': [[7, 12, 13, 14], 103],
            'output': 62
        }
        self.assertEqual(modlcm(*data['input']), data['output'])


if __name__ == '__main__':
    unittest.main()
