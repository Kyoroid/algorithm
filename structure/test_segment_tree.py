import unittest
from structure.segment_tree import *


class TestSegmentTree(unittest.TestCase):

    def test_tolist(self):
        INF = 100000000
        data = {
            'input': [3, -INF],
            'output': [-INF, -INF, -INF]
        }
        st = SegmentTree(*data['input'])
        self.assertEqual(st.tolist(), data['output'])

    def test_update(self):
        INF = 100000000
        data = {
            'input': [3, -INF],
            'output': [-INF, -INF, -INF]
        }
        st = SegmentTree(*data['input'])
        self.assertEqual(st.tolist(), data['output'])
        data = {
            'input': [(0, 1), (2, 4), (1, 3), (1, 5)],
            'output': [1, 5, 4]
        }
        for key, value in data['input']:
            st.update(key, value)
        self.assertEqual(st.tolist(), data['output'])

    def test_query(self):
        INF = 100000000
        N = 200000
        data = {
            'input': [N, -INF],
            'output': [-INF, -INF, -INF]
        }
        st = SegmentTree(*data['input'])
        for key, value in zip(range(N), range(N)):
            st.update(key, value)
        data = {
            'input': [450, 19953],
            'output': 19953-1
        }
        self.assertEqual(st.query(*data['input']), data['output'])


class TestSegmentTreeFunc(unittest.TestCase):

    def test_update(self):
        INF = 100000000
        data = {
            'input': [3, -INF],
            'output': [-INF, -INF, -INF]
        }
        st = seginit(*data['input'])
        self.assertEqual(segview(st, 3), data['output'])

    def test_query(self):
        INF = 100000000
        N = 200000
        data = {
            'input': [N, -INF],
            'output': [-INF, -INF, -INF]
        }
        st = seginit(*data['input'])
        for key, value in zip(range(N), range(N)):
            segupdate(st, key, value)
        data = {
            'input': [450, 19953],
            'output': 19953-1
        }
        self.assertEqual(segquery(st, *data['input']), data['output'])


if __name__ == '__main__':
    unittest.main()
