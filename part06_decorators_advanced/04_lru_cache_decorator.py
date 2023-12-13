import functools
import time

def fibonacci_undecorated(n):
    if n <= 2:
        return 1

    return fibonacci_undecorated(n - 1) + fibonacci_undecorated(n - 2)

@functools.lru_cache
def fibonacci_decorated(n):
    if n <= 2:
        return 1

    return fibonacci_decorated(n - 1) + fibonacci_decorated(n - 2)

start_time = time.time()
fibonacci_undecorated(35)
undecorated_duration = time.time() - start_time

start_time = time.time()
fibonacci_decorated(35)
decorated_duration = time.time() - start_time

print(f'Undecorated version: {undecorated_duration:0.6f} seconds')
print(f'Decorated version: {decorated_duration:0.6f} seconds')
print(f'Faster by a factor of {undecorated_duration/decorated_duration:.0f}')