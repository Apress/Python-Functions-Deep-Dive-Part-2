def do_multiple_times(function, times):
    for _ in range(times):
        function()


def say_hello():
    print('Hello')


do_multiple_times(say_hello, 5)
