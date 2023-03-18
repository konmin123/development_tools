"""Буду складывать сюда декораторы для дальнейшего использования"""
import time

# Основная идея декоратора в добавлении дополнительного поведения функции или
# классу. Пример ниже.


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


#  В декоратор можно передать аргумент.

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
