"""Декоратор измеряющий время выполнения функции/метода"""
import time


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'время выполнения функции: {func.__name__} составило: '
              f'{end - start} секунд.')
        return result
    return wrapper


@time_decorator
def sum_(a, b):
    for _ in range(1_000_000):
        continue
    return a + b


if __name__ == '__main__':
    sum_(5, 10)
