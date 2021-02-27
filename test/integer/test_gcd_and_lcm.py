from io import StringIO
import unittest
import unittest.mock
from lib.integer.gcd_and_lcm import *


@unittest.mock.patch("sys.stderr", new_callable=StringIO)
@unittest.mock.patch("sys.stdout", new_callable=StringIO)
class TestGCD(unittest.TestCase):
    def test_gcd(self, mock_stdout, mock_stderr):
        actual = gcd(17)
        self.assertEqual(17, actual)
        actual = gcd(30, 42)
        self.assertEqual(6, actual)
        actual = gcd(33, 27, 15, 12)
        self.assertEqual(3, actual)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))

    def test_gcd_zero(self, mock_stdout, mock_stderr):
        actual = gcd(24, 0)
        self.assertEqual(24, actual)
        actual = gcd(0, 24)
        self.assertEqual(24, actual)
        actual = gcd(0, 0)
        self.assertEqual(0, actual)
        actual = gcd(0, 24, 0, 21, 0)
        self.assertEqual(3, actual)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))


@unittest.mock.patch("sys.stderr", new_callable=StringIO)
@unittest.mock.patch("sys.stdout", new_callable=StringIO)
class TestLCM(unittest.TestCase):
    def test_lcm(self, mock_stdout, mock_stderr):
        actual = lcm(17)
        self.assertEqual(17, actual)
        actual = lcm(60, 24)
        self.assertEqual(120, actual)
        actual = lcm(12, 15, 24, 10)
        self.assertEqual(120, actual)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))

    def test_lcm_zero(self, mock_stdout, mock_stderr):
        actual = lcm(24, 0)
        self.assertEqual(0, actual)
        actual = lcm(0, 24)
        self.assertEqual(0, actual)
        actual = lcm(0, 0)
        self.assertEqual(0, actual)
        actual = lcm(0, 12, 0, 15, 0)
        self.assertEqual(0, actual)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))
