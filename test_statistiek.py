# Lars Rotgers (lars.rotgers@student.nhlstenden.com), 21-9-2019
import unittest
from statistiek import median, mean, spread, sd, descriptive_statistics
from math import sqrt

class MyTestCase(unittest.TestCase):
    def test_check_numbers(self):
        try:
            mean(['a', 'b', 'c'])
            assert False, 'Exception not raised'
        except ValueError:
            pass

    def test_median_even(self):
        m = median([1, 2, 3, 4, 5, 6])
        assert m == (3 + 4) / 2, 'Invalid value for median'

    def test_median_odd(self):
        m = median([1, 2, 3, 4, 5])
        assert m == 3, 'Invalid value for median'

    def test_median_sort(self):
        m = median([5, 2, 4, 1, 3])
        assert m == 3, 'Invalid value for median'

    def test_mean(self):
        m = mean([1, 2, 3, 4, 5])
        assert m == 3, 'Invalid value for mean'

    def test_spread(self):
        s = spread([-10, 10])
        assert s == 20, 'Invalid value for spread'

    def test_sd(self):
        stddev = sd([1, 2, 3, 4, 5])
        assert stddev == sqrt(2)

    def test_descriptive_statistics(self):
        values = [1, 2, 3, 4, 5]
        med, avg, spr, stddev = descriptive_statistics(values)
        assert med == 3
        assert spr == 4
        assert avg == 3
        assert stddev == sqrt(2)


if __name__ == '__main__':
    unittest.main()
