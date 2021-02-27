from io import StringIO
import unittest
import unittest.mock
from lib.integer.prime_factorization import *


@unittest.mock.patch("sys.stderr", new_callable=StringIO)
@unittest.mock.patch("sys.stdout", new_callable=StringIO)
class TestPrimeFactorization(unittest.TestCase):
    def test_prime_factorization(self, mock_stdout, mock_stderr):
        actual_base, actual_count = prime_factorization(1)
        self.assertListEqual([1], actual_base)
        self.assertListEqual([1], actual_count)
        actual_base, actual_count = prime_factorization(2)
        self.assertListEqual([2], actual_base)
        self.assertListEqual([1], actual_count)
        actual_base, actual_count = prime_factorization(2696)
        self.assertListEqual([2, 337], actual_base)
        self.assertListEqual([3, 1], actual_count)
        actual_base, actual_count = prime_factorization(999999999988)
        self.assertListEqual([2, 11, 124847, 182041], actual_base)
        self.assertListEqual([2, 1, 1, 1], actual_count)
        actual_base, actual_count = prime_factorization(999999999989)
        self.assertListEqual([999999999989], actual_base)
        self.assertListEqual([1], actual_count)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))

    def test_prime_factorization_type_check(self, mock_stdout, mock_stderr):
        actual_base, actual_count = prime_factorization(999999999988)
        self.assertListEqual([int, int, int, int], [type(e) for e in actual_base])
        self.assertListEqual([int, int, int, int], [type(e) for e in actual_count])
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))


@unittest.mock.patch("sys.stderr", new_callable=StringIO)
@unittest.mock.patch("sys.stdout", new_callable=StringIO)
class TestPrimeFactorizationSPF(unittest.TestCase):
    def test_list_spf(self, mock_stdout, mock_stderr):
        spf = list_spf(12)
        self.assertListEqual([0, 1, 2, 3, 2, 5, 2, 7, 2, 3, 2, 11, 2], spf)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))

    def test_prime_factorization_spf(self, mock_stdout, mock_stderr):
        spf = list_spf(1000003)
        actual_base, actual_count = prime_factorization_spf(1, spf)
        self.assertListEqual([1], actual_base)
        self.assertListEqual([1], actual_count)
        actual_base, actual_count = prime_factorization_spf(2, spf)
        self.assertListEqual([2], actual_base)
        self.assertListEqual([1], actual_count)
        actual_base, actual_count = prime_factorization_spf(2696, spf)
        self.assertListEqual([2, 337], actual_base)
        self.assertListEqual([3, 1], actual_count)
        actual_base, actual_count = prime_factorization_spf(1000002, spf)
        self.assertListEqual([2, 3, 166667], actual_base)
        self.assertListEqual([1, 1, 1], actual_count)
        actual_base, actual_count = prime_factorization_spf(1000003, spf)
        self.assertListEqual([1000003], actual_base)
        self.assertListEqual([1], actual_count)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))

    def test_prime_factorization_spf_type_check(self, mock_stdout, mock_stderr):
        spf = list_spf(1000003)
        actual_base, actual_count = prime_factorization_spf(1000002, spf)
        self.assertListEqual([int, int, int], [type(e) for e in actual_base])
        self.assertListEqual([int, int, int], [type(e) for e in actual_count])
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))
