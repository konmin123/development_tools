"""Реализуем для своих объектов методы __add__, __iadd__, __sub__, __isub__."""


class SomeClass:
    def __init__(self, value: int):
        self.__value = value

    def __add__(self, other):
        new_object = SomeClass(self.__value)
        new_object.__value += other.__value
        return new_object

    def __iadd__(self, other):
        self.__value += other.__value
        return self

    def __sub__(self, other):
        new_object = SomeClass(self.__value)
        new_object.__value -= other.__value
        return new_object

    def __isub__(self, other):
        self.__value -= other.__value
        return self

    def __str__(self):
        return str(self.__value)


if __name__ == '__main__':
    first_object = SomeClass(10)
    second_object = SomeClass(20)
    print(second_object - first_object)
    print(second_object + first_object)
    first_object -= second_object
    print(first_object)
    first_object += second_object
    print(first_object)
