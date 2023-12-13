def say_hello():
    global first_name
    print('Hello', first_name)
    first_name = 'Amara'

first_name = 'Fred'
say_hello()
print('first_name, after calling say_hello:', first_name)
