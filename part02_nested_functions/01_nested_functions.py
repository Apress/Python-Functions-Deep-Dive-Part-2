def outer():
    def inner():
        print(f'Inner function called\n')

    print('Outer function called\n')

    print('In outer function, calling inner function')
    inner()

print('In main code, calling outer function')
outer()

print('In main code, trying to call inner function')
try:
    inner()
except NameError as e:
    print('Exception raised:', e, '\n')
