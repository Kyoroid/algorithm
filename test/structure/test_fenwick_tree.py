from io import StringIO
import unittest
import unittest.mock
from lib.structure.fenwick_tree import *


@unittest.mock.patch("sys.stderr", new_callable=StringIO)
@unittest.mock.patch("sys.stdout", new_callable=StringIO)
class TestFenwickTree(unittest.TestCase):
    def test_init(self, mock_stdout, mock_stderr):
        ft = FenwickTree(5)
        self.assertEqual(ft.n, 5)

    def test_find_greater_than_x_in_range(self, mock_stdout, mock_stderr):
        # https://stackoverflow.com/questions/39363745/find-the-number-of-elements-greater-than-x-in-a-given-range
        # a must be unique
        n = 5
        a = [5, 4, 2, 1, 3]
        queries = [(0, 1, 6), (2, 5, 2)]
        # bv: (A[i], i) or (v, l, r)
        seq = [(1, 3), (2, 2, 5), (2, 2), (3, 4), (4, 1), (5, 0), (6, 0, 1)]
        ft = FenwickTree(n)
        actual = []
        for s in seq[::-1]:
            if len(s) == 3:
                _, l, r = s
                answer = ft.sum(l, r)
                actual.append(answer)
            elif len(s) == 2:
                _, i = s
                ft.add(i, 1)
        self.assertEqual(actual, [0, 2])
