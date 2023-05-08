"""Переопределение поведения метода через super()"""


class SomeClass:
    @classmethod
    def __new__(cls, *args, **kwargs):
        print('Вызов метода __new__')
        instance = super().__new__(cls)
        print('Можем поменять instance, созданный методом __new__.')
        return instance

    def __init__(self):
        print('Создаю экземпляр класса.')
        self.some_attribute: int = 0


if __name__ == '__main__':
    new_instance = SomeClass()

