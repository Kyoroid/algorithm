from io import StringIO
import unittest
import unittest.mock
from lib.combinatorics.factorial import list_mod_facts, list_mod_inv_facts
from lib.combinatorics.permutation import *


@unittest.mock.patch("sys.stderr", new_callable=StringIO)
@unittest.mock.patch("sys.stdout", new_callable=StringIO)
class TestModPerm(unittest.TestCase):
    def test_mod_perm(self, mock_stdout, mock_stderr):
        f = list_mod_facts(100000, 1000000007)
        invf = list_mod_inv_facts(100000, 1000000007)
        actual = mod_perm(10, 3, 1000000007, f, invf)
        self.assertEqual(720, actual)
        actual = mod_perm(100000, 30000, 1000000007, f, invf)
        self.assertEqual(584804559, actual)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))
