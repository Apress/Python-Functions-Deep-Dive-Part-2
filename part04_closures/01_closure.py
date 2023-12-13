def create_plus_function(increment_word):
    word_to_integer = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    increment = word_to_integer[increment_word]

    def plus_function(n):
        return n + increment

    return plus_function


plus_two = create_plus_function('two')
plus_five = create_plus_function('five')

print('4 plus two = ', plus_two(4))
print('6 plus five = ', plus_five(6))
