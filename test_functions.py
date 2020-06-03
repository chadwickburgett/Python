"""
Program: test_functions.py
Author: Chadwick Burgett
Last date modified: 06/03/2019
The purpose of this program is to
test the camper_age_input program.
"""
import unittest
from main import camper_age_input

class FunctionTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(120, camper_age_input.convert_to_months(10))
        self.assertEqual(0, camper_age_input.convert_to_months(0))
        self.assertEqual(1200, camper_age_input.convert_to_months(100))

if __name__ == '__main__':
    unittest.main()
