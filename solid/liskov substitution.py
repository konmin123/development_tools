"""Модуль демонстрирующий один из принципов SOLID, а именно liskov substitution
 principle, демонстрирующий возможность подстановки дочернего класса"""


class Printer:
    def __init__(self, name):
        self.name = name

    def print_text(self):
        print(f'Принтер {self.name} печатает текст!')


class PhotoPrinter(Printer):

    def print_photo(self):
        print(f'Принтер {self.name} печатает фото!')


black_1128 = Printer('black_1128')
black_1128.print_text()


color_3512 = PhotoPrinter('color_3512')
color_3512.print_text()  # Можно заменить родительский класс на дочерний.
color_3512.print_photo()
