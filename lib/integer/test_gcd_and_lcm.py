import unittest
from lib.integer.gcd_and_lcm import *


class TestGCD(unittest.TestCase):
    
    def test_gcd(self):
        actual = gcd(17)
        self.assertEqual(17, actual)
        actual = gcd(30, 42)
        self.assertEqual(6, actual)
        actual = gcd(33, 27, 15, 12)
        self.assertEqual(3, actual)

    def test_gcd_zero(self):
        actual = gcd(24, 0)
        self.assertEqual(24, actual)
        actual = gcd(0, 24)
        self.assertEqual(24, actual)
        actual = gcd(0, 0)
        self.assertEqual(0, actual)
        actual = gcd(0, 24, 0, 21, 0)
        self.assertEqual(3, actual)


class TestLCM(unittest.TestCase):
    
    def test_lcm(self):
        actual = lcm(17)
        self.assertEqual(17, actual)
        actual = lcm(60, 24)
        self.assertEqual(120, actual)
        actual = lcm(12, 15, 24, 10)
        self.assertEqual(120, actual)

    def test_lcm_zero(self):
        actual = lcm(24, 0)
        self.assertEqual(0, actual)
        actual = lcm(0, 24)
        self.assertEqual(0, actual)
        actual = lcm(0, 0)
        self.assertEqual(0, actual)
        actual = lcm(0, 12, 0, 15, 0)
        self.assertEqual(0, actual)
