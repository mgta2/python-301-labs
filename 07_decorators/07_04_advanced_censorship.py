# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".

def bad_words(*new_args):
    def censor(given_func):
        def wrapper(*args, **kwargs):
            my_str = given_func(*args, **kwargs)
            for arg in new_args:
                if arg in my_str:
                    length = len(arg)
                    new_string = ""
                    for i in range(0, length-1):
                        new_string += "*"
                    my_str = my_str.replace(arg[1:], new_string)
            return my_str
        return wrapper
    return censor

@bad_words("Shoot", "toe")
def bad_func():
    return "I bumped my toe! Shoot!"

@bad_words("shoot", "crab")
def another_bad_func():
    return "Oh shoot! I've lost my crab."

print(bad_func()) # I bumped my t**! S****!
print(another_bad_func()) # Oh s****! I've lost my c***.