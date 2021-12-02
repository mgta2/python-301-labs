# Write a unittest test suite with at least two methods that test
# the functionality of the built-in `math` module.

import unittest
import math

class TestMath(unittest.TestCase):
    def test_floor_rounds_down(self):
        self.assertEqual(math.floor(3.4), 3)
    def test_ceil_rounds_up(self):
        self.assertEqual(math.ceil(3.4), 4)


if __name__ == "__main__":
    unittest.main()