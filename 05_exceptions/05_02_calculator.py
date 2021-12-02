# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.

try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(x/y)
except ValueError:
    print("You did not enter an integer.")
except ZeroDivisionError:
    print("You cannot divide by zero.")