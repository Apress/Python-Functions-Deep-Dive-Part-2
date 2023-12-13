import time

def slow_integer_multiplication(a, b):
    start_time = time.time()
    result = 0
    for _ in range(a):
        for _ in range(b):
            result += 1
    print('slow_integer_multiplication', time.time() - start_time, 'seconds')
    return result


def herons_square_root(n):
    start_time = time.time()
    guess = 1
    while abs(guess ** 2 - n) > 0.00000001:
        guess = (guess + n / guess) / 2
    print('herons_square_root', time.time() - start_time, 'seconds')
    return guess

print(slow_integer_multiplication(5_000, 5_000))
print(herons_square_root(23.712 ** 2))
