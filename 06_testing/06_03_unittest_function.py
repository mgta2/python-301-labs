# Demonstrate your knowledge of unittest by first creating a function 
# with input parameters and a return value.
# Once you have a function, write at least two tests for the function 
# that use different assertions. The tests should pass.
# Then, include another test that doesn't pass.
#
# NOTE: You can write both the code as well as the tests for it in this file.
# However, feel free to adhere to best practices and separate your tests and
# the functions you are testing into different files.
# Keep in mind that you will run into an error when you'll attempt to import
# this file, because Python modules can't begin with a number.
# You can rename the file to make it work :)

import unittest

def my_funct(a, b):
    x = (-1)**(a + b)
    return x


class TestMyFunct(unittest.TestCase):
    def test_equal_output(self): # Test passes
        self.assertEqual(my_funct(5, 12), -1)
    def test_type_error_raises(self): # Test passes
        self.assertRaises(TypeError, my_funct, "5", "12")
    def test_index_error_raises(self): # Test fails
        self.assertRaises(IndexError, my_funct, 5, 12)

if __name__ == "__main__":
    unittest.main()