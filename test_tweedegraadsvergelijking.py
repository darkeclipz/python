import unittest
from tweedegraadsvergelijking import solve


class TweedegraadsvergelijkingTests(unittest.TestCase):
    def test_a_and_b_is_zero(self):
        try:
            solve(0, 0, 0)
            assert False
        except ValueError:
            assert True

    def test_first_degree(self):
        s1, s2 = solve(0, 4, 20)
        assert s1 == -5
        assert s2 is None

    def test_negative_discriminant(self):
        try:
            solve(1, 2, 20)
            assert False
        except ValueError:
            assert True

    def test_poly1(self):
        s1, s2 = solve(3, 12, 12)
        assert s1 == -2
        assert s2 is None

    def test_poly2(self):
        s1, s2 = solve(1, -6, 8)
        assert s1 == 2
        assert s2 == 4


if __name__ == '__main__':
    unittest.main()
