from functools import wraps


def first_decorator(func):
    @wraps(func)  # Задекорировали обёртку
    def wrapper1():
        """Это декоратор first_decorator."""
        print(f'Докстринг декорируемой функции: {func.__doc__}')
        print(f'Декорируется функция {func.__name__}')
        return func()
    return wrapper1


def second_decorator(func):
    @wraps(func)  # И здесь задекорировали обёртку
    def wrapper2():
        """Это декоратор second_decorator."""
        print(f'Докстринг декорируемой функции: {func.__doc__}')
        print(f'Декорируется функция {func.__name__}')
        return func()
    return wrapper2


@first_decorator
@second_decorator
def do_nothing():
    """Я ничего не знаю. Я никуда не летаю."""
    ...


do_nothing()