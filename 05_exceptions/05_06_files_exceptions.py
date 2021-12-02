# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?

wap_str = "books/war_and_peace.txt"
cap_str = "books/crime_and_punishment.txt"
pap_str = "books/pride_and_prejudice.txt"
book_list = [wap_str, cap_str, pap_str]

# Getting decoding errors (probably due to letters like á, ë etc.)
# Will just ignore them with 'errors' keyword as below.

with open(wap_str, "r", errors='ignore') as wap:
    x = wap.read()

with open(cap_str, "w") as cap:
    cap.write("")

for i in range(0,3):
    with open(book_list[i], "r", errors='ignore') as fin:
        data = fin.read()
    
    try:
        print(data[0])
    
    except IndexError:
        print(f"{book_list[i]} has no characters in it.")

# Trying to access the 0 index of an empty string will fail with an IndexError.

# Output is as expected:
"""
W
books/crime_and_punishment.txt has no characters in it.
I
"""