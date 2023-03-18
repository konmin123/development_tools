"""Буду складывать сюда декораторы для дальнейшего использования"""
import time

# Основная идея декоратора в добавлении дополнительного поведения функции или
# классу. Пример ниже.
from typing import Any


def some_decorator(func):
    def wrapper(*args, **kwargs):
        print('Поведение до выполнения функции')
        func(*args, **kwargs)
        print('Поведение после выполнения функции')
    return wrapper


@some_decorator
def print_hi():
    print('Hi')



print_hi()


# В декоратор можно передать дополнительный аргумент, например.

def pre_decorator(milliseconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            t = time.time() - start
            if milliseconds:
                print(f'прошло {t * 1000} миллисекунд')
            else:
                print(f'прошло {t} секунд')
            return result
        return wrapper
    return decorator


@pre_decorator(True)
def sleep_time(t: int):
    time.sleep(t)


sleep_time(5)



# def average_function_speed_decorator(func):
#     """Декоратор печатающий среднее время выполнения функции"""
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         for _ in range(1000):
#             func(*args, **kwargs)
#         end = time.time()
#         print((end - start) / 1000)
#     return wrapper
#
#
# @average_function_speed_decorator
# def last_sequence_number(number: int):
#     for cur_number in range(number + 1):
#         if cur_number == number:
#             return cur_number
#
#
# last_sequence_number(1000)