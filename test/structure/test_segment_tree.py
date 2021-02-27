from io import StringIO
import unittest
import unittest.mock
from lib.structure.segment_tree import *


@unittest.mock.patch("sys.stderr", new_callable=StringIO)
@unittest.mock.patch("sys.stdout", new_callable=StringIO)
class TestSegmentTree(unittest.TestCase):
    def test_from_sequence(self, mock_stdout, mock_stderr):
        A = [3, -1, 4, 2, 3, -6, 11]
        st = SegmentTree.from_sequence(A, op=min, init_value=10 ** 8)
        actual = st.prod(0, len(A))
        self.assertEqual(actual, -6)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))

    def test_set(self, mock_stdout, mock_stderr):
        A = [3, -1, 4, 2, 3, -6, 11]
        st = SegmentTree.from_sequence(A, op=min, init_value=10 ** 8)
        actual = st.set(5, -4)
        actual = st.prod(0, len(A))
        self.assertEqual(actual, -4)
        actual = st.set(5, 0)
        actual = st.prod(0, len(A))
        self.assertEqual(actual, -1)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))

    def test_prod(self, mock_stdout, mock_stderr):
        A = [3, -1, 4, 2, 3, -6, 11]
        st = SegmentTree.from_sequence(A, op=min, init_value=10 ** 8)
        actual = st.prod(0, 3)
        self.assertEqual(actual, -1)
        actual = st.prod(4, 7)
        self.assertEqual(actual, -6)
        actual = st.prod(2, 3)
        self.assertEqual(actual, 4)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))

    def test_interval_error(self, mock_stdout, mock_stderr):
        A = [3, -1, 4, 2, 3, -6, 11]
        st = SegmentTree.from_sequence(A, op=min, init_value=10 ** 8)
        with self.assertRaises(IntervalError):
            st.prod(3, 3)
        with self.assertRaises(IntervalError):
            st.prod(4, 3)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))
