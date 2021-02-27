from io import StringIO
import unittest
import unittest.mock
from lib.integer.multiple_and_divisor import *


@unittest.mock.patch("sys.stderr", new_callable=StringIO)
@unittest.mock.patch("sys.stdout", new_callable=StringIO)
class TestListDivisors(unittest.TestCase):
    def test_list_divisors(self, mock_stdout, mock_stderr):
        actual = list_divisors(12)
        self.assertListEqual([1, 12, 2, 6, 3, 4], actual)
        actual = list_divisors(12, sorted=True)
        self.assertListEqual([1, 2, 3, 4, 6, 12], actual)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))

    def test_list_divisors_type_check(self, mock_stdout, mock_stderr):
        actual = list_divisors(12, sorted=True)
        self.assertListEqual([int, int, int, int, int, int], [type(e) for e in actual])
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))


@unittest.mock.patch("sys.stderr", new_callable=StringIO)
@unittest.mock.patch("sys.stdout", new_callable=StringIO)
class TestListMultiples(unittest.TestCase):
    def test_list_multiples(self, mock_stdout, mock_stderr):
        actual = list_multiples(3, 23)
        self.assertListEqual([3, 6, 9, 12, 15, 18, 21], actual)
        actual = list_multiples(3, 24)
        self.assertListEqual([3, 6, 9, 12, 15, 18, 21, 24], actual)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))


@unittest.mock.patch("sys.stderr", new_callable=StringIO)
@unittest.mock.patch("sys.stdout", new_callable=StringIO)
class TestCountDivisors(unittest.TestCase):
    def test_count_divisors(self, mock_stdout, mock_stderr):
        counts = count_divisors(17)
        actual = len(counts)
        self.assertEqual(18, actual)
        actual = counts[1]
        self.assertEqual(1, actual)
        actual = counts[17]
        self.assertEqual(2, actual)
        actual = counts[12]
        self.assertEqual(6, actual)
        actual = counts[16]
        self.assertEqual(5, actual)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))
