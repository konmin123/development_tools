"""Миксин позволяющий методам работать класса в многопоточном режиме."""
import threading
from time import time, sleep


class ThreadMixin:
    def __init__(self):
        self.change_methods()

    @staticmethod
    def threading_method(method):
        th = threading.Thread(target=method)
        return th.start

    def change_methods(self):
        for index, str_method in enumerate(self.__dir__()[1::]):
            if str_method == '__doc__':
                break
            method = self.__getattribute__(str_method)
            self.__setattr__(str_method, self.threading_method(method))


class Parser(ThreadMixin):
    @staticmethod
    def send_request():
        print("Отправляю запрос...")
        sleep(1)
        print('выполнена send_request')

    @staticmethod
    def pars_request():
        print("Парсю результат...")
        sleep(0.75)
        print('выполнена pars_request')


avito = Parser()
start = time()
avito.send_request()
avito.pars_request()
end = time()
print(end - start)
