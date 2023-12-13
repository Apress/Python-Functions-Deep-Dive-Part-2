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
    if language == 'English':
        return say_hello

    if language == 'French':
        return say_bonjour

    if language == 'Spanish':
        return say_hola

    if language == 'Dutch':
        return say_hoi

greeting = function_for_language('French')
greeting()
