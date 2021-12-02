# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.

def decorator(given_func):
    def wrapper(*args):
        return '"' + given_func(*args) + '"'
    return wrapper

def func(n):
    return n

print(func("Hello world!")) # Hello world!
print(decorator(func)("Hello world!")) # "Hello world!"