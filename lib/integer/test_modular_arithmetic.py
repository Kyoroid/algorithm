import unittest
from lib.integer.modular_arithmetic import *


class TestModInv(unittest.TestCase):
    
    def test_modinv(self):
        actual = modinv(7, 10000)
        self.assertEqual(7143, actual)
        with self.assertRaises(InversionError):
            modinv(12, 10000)


class TestPModPow(unittest.TestCase):
    
    def test_pmodpow(self):
        actual = pmodpow(7, 1000, 101)
        self.assertEqual(1, actual)
        self.assertEqual(pow(7, 1000, 101), actual)
        actual = pmodpow(7, -1, 1000000007)
        self.assertEqual(142857144, actual)
        self.assertEqual(pow(7, -1, 1000000007), actual)
        actual = pmodpow(7, -10007, 101)
        self.assertEqual(55, actual)
        self.assertEqual(pow(7, -10007, 101), actual)
