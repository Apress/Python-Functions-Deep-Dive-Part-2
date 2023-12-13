import time


def add_time_function(function):
    def timed_function(*args, **kwargs):
        number_of_repeats = 10
        total_time = 0
        for _ in range(number_of_repeats):
            start_time = time.time()
            result = function(*args, **kwargs)
            duration = time.time() - start_time
            total_time += duration
        average_time = total_time / number_of_repeats
        print(function.__name__, average_time, 'seconds')
        return result
    return timed_function


@add_time_function
def slow_integer_multiplication(a, b):
    result = 0
    for _ in range(a):
        for _ in range(b):
            result += 1
    return result


print(slow_integer_multiplication(5_000, 5_000))
