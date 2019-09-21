# Lars Rotgers (lars.rotgers@student.nhlstenden.com), 21-9-2019
import unittest
from bisectiemethode import bisection_solver, poly1, sinusoid


def is_within_range(actual, expected, error):
    """
    Check if a value x is within the range of an interval.
    Useful to check if a floating-point number is almost
    equal to a certain value.
    :param actual: the value x of the floating-point.
    :param expected: the expected value x' for x.
    :param error: the error range to create the interval [x'-e, x'+e].
    :return: True if x is within the interval [x'-e, x'+e].
    """
    return actual > expected - error \
           or actual < expected + error


class MyTestCase(unittest.TestCase):
    def test_positive_epsilon_check(self):
        try:
            bisection_solver(poly1, a=0, b=2.5, epsilon=-1)
            assert False, 'Exception not raised'
        except ValueError:
            pass

    def test_fx_both_equal_sign_check(self):
        try:
            bisection_solver(poly1, a=0, b=2.5)
            assert False, 'Exception not raised'
        except ValueError:
            pass

    def test_fa_fb_both_same_sign_check(self):
        try:
            bisection_solver(sinusoid, a=1, b=2)
            assert False, 'Exception not raised'
        except ValueError:
            pass

    def test_solve_poly1(self):
        x0 = bisection_solver(poly1, a=0.1, b=0.8)
        assert is_within_range(actual=x0, expected=0.5, error=0.001)

    def test_solve_poly1_immediately(self):
        x0 = bisection_solver(poly1, a=0, b=1)
        assert is_within_range(actual=x0, expected=0.5, error=0.001)

    def test_solve_sinusoid(self):
        x0 = bisection_solver(sinusoid, a=-0.5, b=1)
        assert is_within_range(actual=x0, expected=0, error=0.001)


if __name__ == '__main__':
    unittest.main()
