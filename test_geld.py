# Lars Rotgers (lars.rotgers@student.nhlstenden.com), 21-9-2019
import unittest
from geld import *


class GeldTests(unittest.TestCase):
    def test_calculate_closing_value(self):
        e = calculate_closing_value(1000, 4, 10)
        assert round(e, 2) == 1480.24, 'Invalid result for e'

    def test_calculate_start_capital(self):
        b = calculate_start_capital(1480.24, 4, 10)
        assert round(b) == 1000, 'Invalid result for b'

    def test_calculate_period(self):
        t = calculate_period(1000, 4, 1480.24)
        assert round(t) == 10, 'Invalid result for t'

    def test_calculate_interest(self):
        p = calculate_interest(1000, 10, 1480.24)
        assert round(p) == 4, 'Invalid result for p'


if __name__ == '__main__':
    unittest.main()
