# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************

def decorate(n):
    def decorator(given_func):
        def wrapper(*args, **kwargs):
            my_str = given_func(*args, **kwargs)
            return f"{n}{n}{n}{n}{n}\n" + my_str + f"\n{n}{n}{n}{n}{n}"
        return wrapper
    return decorator

@decorate("*")
def say_hello():
    return "Hello"

print(say_hello())

# Output
"""
*****
Hello
*****
"""