# Write a script that demonstrates TDD. Using pseudocode, plan out
# a couple of small functions. They could be as fundamental as adding
# and subtracting numbers with each other,
# or more complex such as functions that read and write to files.
#
# Instead of writing the functions, however, only write the tests for them.
# Think about how your functions might fail and write tests that will check 
# for that and identify these failures.
#
# You do not need to implement the actual functions after writing the tests 
# but of course you can do that, too.

import unittest

# First function will add numbers f(a,b) = a + b
def fun_one():
    pass

# Second function will try to read a file which doesn't exist.
def fun_two():
    pass

class TestFunctions(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(fun_one(15, 17), 32)
    def test_type_error(self):
        self.assertRaises(TypeError, fun_one, 2, "s")
    def test_file_exists(self):
        self.assertRaises(IOError, fun_two)


if __name__ == "__main__":
    unittest.main()