import time


def slow_integer_multiplication(a, b):
    result = 0
    for _ in range(a):
        for _ in range(b):
            result += 1
    return result


# def time_function(function, *args, **kwargs):
#     start_time = time.time()
#     result = function(*args, **kwargs)
#     print(function.__name__, time.time() - start_time, 'seconds')
#     return result
def add_time_function(function):
    def timed_function(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        print(function.__name__, time.time() - start_time, 'seconds')
        return result
    return timed_function

# print(time_function(slow_integer_multiplication, 5_000, 5_000))
slow_integer_multiplication = add_time_function(slow_integer_multiplication)
print(slow_integer_multiplication(5_000, 5_000))
