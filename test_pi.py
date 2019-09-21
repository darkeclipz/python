import unittest
from pi import approximate_pi_euler, approximate_pi_gregory_leibniz, approximate_pi_brent_salamin
from math import pi as PI

class PiApproximationTests(unittest.TestCase):
    def test_approximate_pi_euler_n0(self):
        try:
            approximate_pi_euler(0)
            assert False, 'Exception not raised'
        except ValueError:
            pass

    def test_approximate_pi_euler_n1(self):
        approximate_pi_euler(1)
        pass

    def test_approximate_pi_euler_n100(self):
        pi = approximate_pi_euler(100)
        assert round(pi, 3) == 3.132, 'Invalid approximation.'

    def test_approximate_pi_gregory_leibniz_n0(self):
        try:
            approximate_pi_gregory_leibniz(0)
            assert False, 'Exception not raised'
        except ValueError:
            pass

    def test_approximate_pi_gregory_leibniz_n1(self):
        approximate_pi_gregory_leibniz(1)
        pass

    def test_approximate_pi_gregory_leibniz_n100(self):
        pi = approximate_pi_gregory_leibniz(100)
        assert round(pi, 3) == 3.151, 'Invalid approximation.'

    def test_approximate_pi_brent_salamin_n0(self):
        approximate_pi_brent_salamin(0)
        pass

    def test_approximate_pi_brent_salamin_n_negative(self):
        try:
            approximate_pi_brent_salamin(-1)
            assert False, 'Exception not raised'
        except ValueError:
            pass

    def test_approximate_pi_brent_salamin_n3(self):
        pi = approximate_pi_brent_salamin(3)
        assert round(pi, 7), round(PI, 7)

if __name__ == '__main__':
    unittest.main()