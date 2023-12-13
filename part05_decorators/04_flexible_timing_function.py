import time


def slow_integer_multiplication(a, b):
    result = 0
    for _ in range(a):
        for _ in range(b):
            result += 1
    return result


def herons_square_root(n):
    guess = 1
    while abs(guess ** 2 - n) > 0.00000001:
        guess = (guess + n / guess) / 2
    return guess


def time_function(function, *args, **kwargs):
    start_time = time.time()
    result = function(*args, **kwargs)
    print(function.__name__, time.time() - start_time, 'seconds')
    return result


print(time_function(slow_integer_multiplication, 5_000, 5_000))
print(time_function(herons_square_root, 23.712 ** 2))
