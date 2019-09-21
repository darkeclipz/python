# Lars Rotgers (lars.rotgers@student.nhlstenden.com), 21-9-2019
import unittest
from paasdatum import easter_date
from datetime import datetime

class MyTestCase(unittest.TestCase):
    def test_greater_than_1900(self):
        try:
            easter_date(1)
            assert False, 'Exception not raised'
        except ValueError:
            pass

    def test_date1(self):
        date = easter_date(2016)
        assert date == datetime(2016, 3, 27), 'Date is incorrect'

    def test_date2(self):
        date = easter_date(2020)
        assert date == datetime(2020, 4, 12), 'Date is incorrect'


if __name__ == '__main__':
    unittest.main()
