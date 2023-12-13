import time


def slow_integer_multiplication(a, b):
    result = 0
    for _ in range(a):
        for _ in range(b):
            result += 1
    return result


def time_function_with_two_arguments(function, a, b):
    start_time = time.time()
    result = function(a, b)
    print(function.__name__, time.time() - start_time, 'seconds')
    return result


print(time_function_with_two_arguments(slow_integer_multiplication, 5_000, 5_000))
