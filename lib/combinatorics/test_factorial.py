import unittest
from lib.combinatorics.factorial import *


class TestListModFacts(unittest.TestCase):
    
    def test_list_mod_facts(self):
        f = list_mod_facts(10, 997)
        self.assertListEqual([1, 1, 2, 6, 24, 120, 720, 55, 440, 969, 717], f)


class TestListModInvFacts(unittest.TestCase):

    def test_list_mod_inv_facts(self):
        invf = list_mod_inv_facts(10, 997)
        self.assertListEqual([1, 1, 499, 831, 457, 889, 979, 852, 605, 178, 616], invf)
