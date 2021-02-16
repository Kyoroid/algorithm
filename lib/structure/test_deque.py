import unittest
from lib.structure.deque import *


class TestRingBuffer(unittest.TestCase):
    
    def test_ringbuffer(self):
        q = ringbuffer(10)
        self.assertGreaterEqual(q.size, 10)
    
    def test_peek(self):
        q = ringbuffer(5)
        for v in range(1, 6):
            rb_append(q, v)
        rb_pop(q)
        rb_popleft(q)
        self.assertEqual(4, rb_peek(q))
        self.assertEqual(2, rb_peekleft(q))

    def test_size(self):
        q = ringbuffer(10)
        for v in range(1, 6):
            rb_append(q, v)
        self.assertEqual(5, rb_size(q))
        rb_pop(q)
        rb_popleft(q)
        self.assertEqual(3, rb_size(q))

    def test_lifo(self):
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

    def test_left_fifo(self):
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

    def test_right_fifo(self):
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
