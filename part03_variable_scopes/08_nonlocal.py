def outer():
    def inner_global():
        global first_name
        print(first_name)
        first_name = 'Hendrik'

    def inner_nonlocal():
        nonlocal first_name
        print(first_name)
        first_name = 'Luca'

    first_name = 'Fred'
    inner_global()
    inner_nonlocal()


first_name = 'Sophia'
outer()
print(first_name)
