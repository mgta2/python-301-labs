# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.

import time

def timeit(given_func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        given_func(*args, **kwargs)
        time_end = time.time()
        time_diff = time_end - time_start
        print(time_diff)
        return time_diff
    return wrapper

@timeit
def find_primes(n):
    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            primes.append(i)
    return primes

find_primes(1000) # 0.06249713897705078
find_primes(10000) # 7.535640001296997