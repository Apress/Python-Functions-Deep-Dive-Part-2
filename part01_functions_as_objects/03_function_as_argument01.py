def do_twice(function):
    function()
    function()


def say_hello():
    print('Hello')


do_twice(say_hello)

