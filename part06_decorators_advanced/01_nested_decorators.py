def timing_decorator(function):
    def timed_function(*args, **kwargs):
        print('Start of timed_function')
        result = function(*args, **kwargs)
        print('End of timed_function')
        return result
    return timed_function


def tracing_decorator(function):
    def traced_function(*args, **kwargs):
        print('Start of traced_function')
        result = function(*args, **kwargs)
        print('End of traced_function')
        return result
    return traced_function


@timing_decorator
@tracing_decorator
def target_function():
    print('target_function started')
    ...  # do some work
    print('target_function finished')


target_function()
