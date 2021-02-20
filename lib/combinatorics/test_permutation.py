import unittest
from lib.combinatorics.factorial import list_mod_facts, list_mod_inv_facts
from lib.combinatorics.permutation import *


class TestModPerm(unittest.TestCase):
    def test_mod_perm(self):
        f = list_mod_facts(100000, 1000000007)
        invf = list_mod_inv_facts(100000, 1000000007)
        actual = mod_perm(10, 3, 1000000007, f, invf)
        self.assertEqual(720, actual)
        actual = mod_perm(100000, 30000, 1000000007, f, invf)
        self.assertEqual(584804559, actual)
