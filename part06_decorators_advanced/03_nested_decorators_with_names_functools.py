import functools

def timing_decorator(function):
    @functools.wraps(function)
    def timed_function(*args, **kwargs):
        result = function(*args, **kwargs)
        print(function.__name__, 'took ... seconds to run')
        return result
    return timed_function

def tracing_decorator(function):
    @functools.wraps(function)
    def traced_function(*args, **kwargs):
        print('Entering', function.__name__)
        result = function(*args, **kwargs)
        print('Exited', function.__name__)
        return result
    return traced_function

@timing_decorator
@tracing_decorator
def example_c():
    ...

print()
example_c()
