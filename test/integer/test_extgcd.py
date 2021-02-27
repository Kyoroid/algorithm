from io import StringIO
import unittest
import unittest.mock
from lib.integer.extgcd import *


@unittest.mock.patch("sys.stderr", new_callable=StringIO)
@unittest.mock.patch("sys.stdout", new_callable=StringIO)
class TestExtGCD(unittest.TestCase):
    def test_extgcd(self, mock_stdout, mock_stderr):
        actual = extgcd(8, 6)
        self.assertTupleEqual((2, 1, -1), actual)
        actual = extgcd(6, 8)
        self.assertTupleEqual((2, -1, 1), actual)
        actual = extgcd(111, 30)
        self.assertTupleEqual((3, 3, -11), actual)
        actual = extgcd(30, 111)
        self.assertTupleEqual((3, -11, 3), actual)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))

    def test_extgcd_zero(self, mock_stdout, mock_stderr):
        actual = extgcd(0, 3)
        self.assertTupleEqual((3, 0, 1), actual)
        actual = extgcd(3, 0)
        self.assertTupleEqual((3, 1, 0), actual)
        actual = extgcd(0, 0)
        self.assertTupleEqual((0, 0, 0), actual)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))


@unittest.mock.patch("sys.stderr", new_callable=StringIO)
@unittest.mock.patch("sys.stdout", new_callable=StringIO)
class TestSolveLinearEquation(unittest.TestCase):
    def test_solve_linear_equation(self, mock_stdout, mock_stderr):
        actual = solve_linear_equation(8, 6, 10)
        self.assertTupleEqual((True, 5, -5), actual)
        actual = solve_linear_equation(8, 6, 2)
        self.assertTupleEqual((True, 1, -1), actual)
        actual = solve_linear_equation(8, 6, 3)
        self.assertTupleEqual((False, 0, 0), actual)
        self.assertEqual(0, len(mock_stdout.getvalue()))
        self.assertEqual(0, len(mock_stderr.getvalue()))
