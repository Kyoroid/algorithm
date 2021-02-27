from io import StringIO
import unittest
import unittest.mock
from lib.integer.composite_and_prime import *


@unittest.mock.patch("sys.stderr", new_callable=StringIO)
@unittest.mock.patch("sys.stdout", new_callable=StringIO)
class TestSieve(unittest.TestCase):
    def test_sieve(self, mock_stdout, mock_stderr):
        primes = sieve(10000)
        self.assertListEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], primes[:10])
        self.assertEqual(7919, primes[999])
        self.assertNotIn(57, primes)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))
