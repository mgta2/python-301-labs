# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".

class PrinceException(Exception):
    
    def __str__(self):
        return "This book contains 'Prince' in the first 100 letters"

wap_str = "books/war_and_peace.txt"
cap_str = "books/crime_and_punishment_copy.txt"
pap_str = "books/pride_and_prejudice.txt"
book_list = [wap_str, cap_str, pap_str]

for i in range(0,3):
    with open(book_list[i], "r", errors='ignore') as fin:
        data = fin.read()
    
    if "Prince" in data[0:100]:
        print(book_list[i])
        raise PrinceException

# books/war_and_peace.txt contains "Prince" in the first 100 letters.