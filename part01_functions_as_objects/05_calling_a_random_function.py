import random

def say_hello():
    print('Hello')

def say_bonjour():
    print('Bonjour')

def say_hola():
    print('Hola')

def say_hoi():
    print('Hoi')

greeting_functions = [say_hello, say_bonjour, say_hola, say_hoi]

print('Running the first function in our list')
greeting_functions[0]()
print()

print('Running 5 random functions, one after another')
for _ in range(5):
    random.choice(greeting_functions)()
