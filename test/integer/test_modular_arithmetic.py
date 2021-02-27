from io import StringIO
import unittest
import unittest.mock
from lib.integer.modular_arithmetic import *


@unittest.mock.patch("sys.stderr", new_callable=StringIO)
@unittest.mock.patch("sys.stdout", new_callable=StringIO)
class TestModInv(unittest.TestCase):
    def test_mod_inv(self, mock_stdout, mock_stderr):
        actual = mod_inv(7, 10000)
        self.assertEqual(7143, actual)
        with self.assertRaises(InversionError):
            mod_inv(12, 10000)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))


@unittest.mock.patch("sys.stderr", new_callable=StringIO)
@unittest.mock.patch("sys.stdout", new_callable=StringIO)
class TestPModPow(unittest.TestCase):
    def test_mod_pow(self, mock_stdout, mock_stderr):
        actual = mod_pow(7, 1000, 101)
        self.assertEqual(1, actual)
        self.assertEqual(pow(7, 1000, 101), actual)
        actual = mod_pow(7, -1, 1000000007)
        self.assertEqual(142857144, actual)
        self.assertEqual(pow(7, -1, 1000000007), actual)
        actual = mod_pow(7, -10007, 101)
        self.assertEqual(55, actual)
        self.assertEqual(pow(7, -10007, 101), actual)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))
