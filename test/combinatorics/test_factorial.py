from io import StringIO
import unittest
import unittest.mock
from lib.combinatorics.factorial import *


@unittest.mock.patch("sys.stderr", new_callable=StringIO)
@unittest.mock.patch("sys.stdout", new_callable=StringIO)
class TestListModFacts(unittest.TestCase):
    def test_list_mod_facts(self, mock_stdout, mock_stderr):
        f = list_mod_facts(10, 997)
        self.assertListEqual([1, 1, 2, 6, 24, 120, 720, 55, 440, 969, 717], f)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))


@unittest.mock.patch("sys.stderr", new_callable=StringIO)
@unittest.mock.patch("sys.stdout", new_callable=StringIO)
class TestListModInvFacts(unittest.TestCase):
    def test_list_mod_inv_facts(self, mock_stdout, mock_stderr):
        invf = list_mod_inv_facts(10, 997)
        self.assertListEqual([1, 1, 499, 831, 457, 889, 979, 852, 605, 178, 616], invf)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))
