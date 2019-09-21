import unittest
from geld import *


class GeldTests(unittest.TestCase):
    def test_solve_for_e(self):
        e = solve_for_e(1000, 4, 10)
        assert round(e, 2) == 1480.24

    def test_solve_for_b(self):
        b = solve_for_b(1480.24, 4, 10)
        assert round(b) == 1000

    def test_solve_for_t(self):
        t = solve_for_t(1000, 4, 1480.24)
        assert round(t) == 10

    def test_solve_for_p(self):
        p = solve_for_p(10, 1480.24, 1000)
        assert round(p) == 4


if __name__ == '__main__':
    unittest.main()
