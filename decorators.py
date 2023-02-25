import time


def average_function_speed_decorator(func):
    """Декоратор печатающий среднее время выполнения функции"""
    def wrapper(*args, **kwargs):
        start = time.time()
        for _ in range(1000):
            func(*args, **kwargs)
        end = time.time()
        print((end - start) / 1000)
    return wrapper


@average_function_speed_decorator
def last_sequence_number(number: int):
    for cur_number in range(number + 1):
        if cur_number == number:
            return cur_number


last_sequence_number(1000)