import unittest
from lib.combinatorics.factorial import list_mod_facts, list_mod_inv_facts
from lib.combinatorics.combination import *


class TestModComb(unittest.TestCase):
    
    def test_mod_comb(self):
        f = list_mod_facts(100000, 1000000007)
        invf = list_mod_inv_facts(100000, 1000000007)
        actual = mod_comb(10, 3, 1000000007, f, invf)
        self.assertEqual(120, actual)
        actual = mod_comb(100000, 30000, 1000000007, f, invf)
        self.assertEqual(169452473, actual)


class TestModConvWithRepl(unittest.TestCase):
    
    def test_mod_comb_with_repl(self):
        f = list_mod_facts(200000, 1000000007)
        invf = list_mod_inv_facts(100000, 1000000007)
        actual = mod_comb_with_repl(10, 3, 1000000007, f, invf)
        self.assertEqual(220, actual)
        actual = mod_comb_with_repl(100000, 30000, 1000000007, f, invf)
        self.assertEqual(640337804, actual)
