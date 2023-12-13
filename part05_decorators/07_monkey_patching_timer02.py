import time


def add_time_function(function):
    def timed_function(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        print(function.__name__, time.time() - start_time, 'seconds')
        return result
    return timed_function


def slow_integer_multiplication(a, b):
    result = 0
    for _ in range(a):
        for _ in range(b):
            result += 1
    return result
slow_integer_multiplication = add_time_function(slow_integer_multiplication)


def herons_square_root(n):
    guess = 1
    while abs(guess ** 2 - n) > 0.00000001:
        guess = (guess + n / guess) / 2
    return guess
herons_square_root = add_time_function(herons_square_root)


print(slow_integer_multiplication(5_000, 5_000))
print(herons_square_root(23.712 ** 2))
