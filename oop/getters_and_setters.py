"""Пишем геттеры и сеттеры для безопасной работы с приватными или защищёнными
атрибутами объекта"""


class SomeClass:
    def __init__(self):
        print('Создаю экземпляр класса')
        self.__some_private_attribute: int = 0

    @property
    def some_private_attribute(self):
        print('Геттер вернул значение.')
        return self.__some_private_attribute

    @some_private_attribute.setter
    def some_private_attribute(self, value):
        if isinstance(value, int):
            print(f'Сеттер изменяет значение аттрибута, текущее значение '
                  f'{self.some_private_attribute} заменено на {value}')
            self.__some_private_attribute = value
        else:
            print(f"Данное значение не может быть установлено т.к. имеет тип "
                  f"{type(value)}, а ожидается <class 'int'>.")


if __name__ == '__main__':
    new_instance = SomeClass()
    print(new_instance.some_private_attribute)
    new_instance.some_private_attribute = 'str'
    print(new_instance.some_private_attribute)
    new_instance.some_private_attribute = 3
    print(new_instance.some_private_attribute)
