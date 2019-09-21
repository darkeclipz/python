import unittest
from tweedegraadsvergelijking import solve


class TweedegraadsvergelijkingTests(unittest.TestCase):
    def test_a_and_b_is_zero(self):
        try:
            solve(0, 0, 0)
            assert False, 'Exception not raised'
        except ValueError:
            pass

    def test_first_degree(self):
        s1, s2 = solve(0, 4, 20)
        assert s1 == -5, 'Solution 1 is incorrect'
        assert s2 is None, 'Solution 2 is not None'

    def test_negative_discriminant(self):
        try:
            solve(1, 2, 20)
            assert False, 'Exception not raised for negative discriminant'
        except ValueError:
            pass

    def test_poly1(self):
        s1, s2 = solve(3, 12, 12)
        assert s1 == -2, 'Solution 1 is incorrect'
        assert s2 is None, 'Solution 2 is not None'

    def test_poly2(self):
        s1, s2 = solve(1, -6, 8)
        assert s1 == 2, 'Solution 1 is incorrect'
        assert s2 == 4, 'Solution 2 is incorrect'


if __name__ == '__main__':
    unittest.main()
