# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

file_name = 'integers.txt'

try:
    with open(file_name, "r") as fin:
        data = fin.read()

except IOError:
    print("File not found.")

else:
    int_list = data.splitlines()
    
    try:
        my_int = int(int_list[0])
        if my_int < 0:
            raise ValueError
        for i in range(0, my_int+1):
            final_num = i
        print(final_num)
    
    except ValueError:
        print(f"{my_int} is not a positive integer.")
