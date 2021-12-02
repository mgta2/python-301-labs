# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"

def censor(given_func):
    def wrapper(*args, **kwargs):
        my_str = given_func(*args, **kwargs)
        if "Shoot" in my_str:
            return my_str.replace("hoot", "****")
        else:
            return my_str
    return wrapper

@censor
def bad_func():
    return "I bumped my toe! Shoot!"

@censor
def another_bad_func():
    return "Shoot!"

print(bad_func()) # I bumped my toe! Shoot!
print(another_bad_func()) # S****!