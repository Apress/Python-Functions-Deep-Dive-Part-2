import random

def say_hello():
    print('Hello')

def say_bonjour():
    print('Bonjour')

def say_hola():
    print('Hola')

def say_hoi():
    print('Hoi')

def function_for_language(language):
    functions = dict(
        English=say_hello,
        French=say_bonjour,
        Spanish=say_hola,
        Dutch=say_hoi
    )
    return functions[language]

greeting = function_for_language('French')
greeting()
