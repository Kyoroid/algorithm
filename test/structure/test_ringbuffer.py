from io import StringIO
import unittest
import unittest.mock
from lib.structure.ringbuffer import *


@unittest.mock.patch("sys.stderr", new_callable=StringIO)
@unittest.mock.patch("sys.stdout", new_callable=StringIO)
class TestRingBuffer(unittest.TestCase):
    def test_ringbuffer(self, mock_stdout, mock_stderr):
        q = ringbuffer(10)
        self.assertGreaterEqual(q.size, 10)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))

    def test_peek(self, mock_stdout, mock_stderr):
        q = ringbuffer(5)
        for v in range(1, 6):
            rb_append(q, v)
        rb_pop(q)
        rb_popleft(q)
        self.assertEqual(4, rb_peek(q))
        self.assertEqual(2, rb_peekleft(q))
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))

    def test_size(self, mock_stdout, mock_stderr):
        q = ringbuffer(10)
        for v in range(1, 6):
            rb_append(q, v)
        self.assertEqual(5, rb_size(q))
        rb_pop(q)
        rb_popleft(q)
        self.assertEqual(3, rb_size(q))
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))

    def test_lifo(self, mock_stdout, mock_stderr):
        q = ringbuffer(5)
        for v in range(1, 6):
            rb_append(q, v)
        for v in range(5, 2, -1):
            self.assertEqual(rb_pop(q), v)
        for v in range(101, 103):
            rb_append(q, v)
        for v in range(102, 100, -1):
            self.assertEqual(rb_pop(q), v)
        for v in range(2, 0, -1):
            self.assertEqual(rb_pop(q), v)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))

    def test_left_fifo(self, mock_stdout, mock_stderr):
        q = ringbuffer(5)
        for v in range(1, 6):
            rb_append(q, v)
        for v in range(1, 4):
            self.assertEqual(rb_popleft(q), v)
        for v in range(101, 103):
            rb_append(q, v)
        for v in range(4, 6):
            self.assertEqual(rb_popleft(q), v)
        for v in range(101, 103):
            self.assertEqual(rb_popleft(q), v)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))

    def test_right_fifo(self, mock_stdout, mock_stderr):
        q = ringbuffer(5)
        for v in range(1, 6):
            rb_appendleft(q, v)
        for v in range(1, 4):
            self.assertEqual(rb_pop(q), v)
        for v in range(101, 103):
            rb_appendleft(q, v)
        for v in range(4, 6):
            self.assertEqual(rb_pop(q), v)
        for v in range(101, 103):
            self.assertEqual(rb_pop(q), v)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))
