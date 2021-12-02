# Write two unittest test cases for the `subtract_divide()` function
# in `mymath.py`
#
# 1. Check for correct results by providing example input.
# 2. Check that a `ZeroDivisionError` gets raised correctly.

import unittest
import mymath

class TestMyMath(unittest.TestCase):
    def test_correct_division(self):
        self.assertEqual(mymath.subtract_divide(9, 5, 2), 3.0)
    def test_raise_zero_error(self):
        self.assertEqual(type(mymath.subtract_divide(9, 6, 6)), str)

if __name__ == "__main__":
    unittest.main()