"""
Program: test_average.py
Author: Chadwick Burgett
Last date modified: 06/04/2020

The purpose of this unit_test is to test the average funcion
in average_scores.
"""
from format_output import average_scores as avg
import unittest
import unittest.mock as mock


class MyTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[85,90,95]):
            assert avg.average() == 90


if __name__ == '__main__':
    unittest.main()
