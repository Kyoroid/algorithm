from io import StringIO
import unittest
import unittest.mock
import numpy as np
from lib.misc.ranking_and_inversion import *


@unittest.mock.patch("sys.stderr", new_callable=StringIO)
@unittest.mock.patch("sys.stdout", new_callable=StringIO)
class TestRankingAndInversion(unittest.TestCase):
    def test_rank_vector(self, mock_stdout, mock_stderr):
        x = np.array([1, 4, 2, 3], dtype=np.int64)
        y = rank_vector(x)
        np.testing.assert_array_equal(y, np.array([0, 3, 1, 2], dtype=np.int64))
        x = np.array([1, 1, 1, 1], dtype=np.int64)
        y = rank_vector(x)
        np.testing.assert_array_equal(y, np.array([0, 1, 2, 3], dtype=np.int64))
    
    def test_inversion_vector(self, mock_stdout, mock_stderr):
        # https://atcoder.jp/contests/chokudai_S001/tasks/chokudai_S001_j
        x = np.array([3, 1, 5, 4, 2], dtype=np.int64)
        y = inversion_vector(x)
        np.testing.assert_array_equal(y, np.array([2, 0, 2, 1, 0], dtype=np.int64))
        x = np.array([1, 2, 3, 4, 5, 6], dtype=np.int64)
        y = inversion_vector(x)
        np.testing.assert_array_equal(y, np.array([0, 0, 0, 0, 0, 0], dtype=np.int64))
        x = np.array([7, 6, 5, 4, 3, 2, 1], dtype=np.int64)
        y = inversion_vector(x)
        np.testing.assert_array_equal(y, np.array([6, 5, 4, 3, 2, 1, 0], dtype=np.int64))
        x = np.array([19, 11, 10, 7, 8, 9, 17, 18, 20, 4, 3, 15, 16, 1, 5, 14, 6, 2, 13, 12], dtype=np.int64)
        y = inversion_vector(x)
        self.assertEqual(y.sum(), 114)
