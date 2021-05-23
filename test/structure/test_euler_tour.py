from io import StringIO
from bisect import bisect_left
import unittest
import unittest.mock
from lib.structure.euler_tour import *


@unittest.mock.patch("sys.stderr", new_callable=StringIO)
@unittest.mock.patch("sys.stdout", new_callable=StringIO)
class TestEulerTour(unittest.TestCase):
    def test_euler_tour(self, mock_stdout, mock_stderr):
        N = 7
        G = [[1, 2], [3, 4, 6], [], [5,], [], [], []]
        t_in, t_out, depth = euler_tour(N, G)
        self.assertListEqual([0, 1, 11, 2, 6, 3, 8], t_in)
        self.assertListEqual([13, 10, 12, 5, 7, 4, 9], t_out)
        self.assertListEqual([0, 1, 1, 2, 2, 3, 2], depth)
    
    def test_query_get_subtree_size(self, mock_stdout, mock_stderr):
        """xを根とするサブツリーの大きさを取得する
        """
        N = 7
        G = [[1, 2], [3, 4, 6], [], [5,], [], [], []]
        t_in, t_out, depth = euler_tour(N, G)
        sorted_t_in = list(sorted(t_in))

        x = 1
        actual = bisect_left(sorted_t_in, t_out[x]) - bisect_left(sorted_t_in, t_in[x])
        self.assertEqual(5, actual)

        x = 4
        actual = bisect_left(sorted_t_in, t_out[x]) - bisect_left(sorted_t_in, t_in[x])
        self.assertEqual(1, actual)
        
        x = 3
        actual = bisect_left(sorted_t_in, t_out[x]) - bisect_left(sorted_t_in, t_in[x])
        self.assertEqual(2, actual)

    def test_query_count_nth_generations(self, mock_stdout, mock_stderr):
        """ノードxを祖先とする、n世代目の子孫の数を取得する

        Parameters
        ----------
        mock_stdout : [type]
            [description]
        mock_stderr : [type]
            [description]
        """
        N = 7
        G = [[1, 2], [3, 4, 6], [], [5,], [], [], []]
        t_in, t_out, depth = euler_tour(N, G)
        sorted_t_in = list(sorted(t_in))

        parent = 1
        actual = bisect_left(sorted_t_in, t_out[parent]) - bisect_left(sorted_t_in, t_in[parent])
        self.assertEqual(5, actual)

        parent = 4
        actual = bisect_left(sorted_t_in, t_out[parent]) - bisect_left(sorted_t_in, t_in[parent])
        self.assertEqual(1, actual)
        
        parent = 3
        actual = bisect_left(sorted_t_in, t_out[parent]) - bisect_left(sorted_t_in, t_in[parent])
        self.assertEqual(2, actual)