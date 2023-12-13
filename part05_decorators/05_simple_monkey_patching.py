def my_len(x):
    return f'The length of {x} is {x.__len__()}'

print('Before monkey patching len() returns:\n', len('Hello'), '\n')
len = my_len
print('After monkey patching len() returns:\n', len('Hello'))
