"""Модуль демонстрирующий один из принципов SOLID, а именно interface
segregation principle, демонстрирующий 3 отдельных тонких интерфейса"""
from abc import ABC, abstractmethod


class Device(ABC):
    ...


class CallDevice(Device):

    @abstractmethod
    def call(self):
        ...


class SmsDevice(Device):

    @abstractmethod
    def sms(self):
        ...


class SearchDevice(Device):

    @abstractmethod
    def search(self):
        ...
