# -*- coding: utf-8 -*-
# @Time : 2021/3/20 14:10 
# @Author : kimihiro
# @File : __init__.py.py 
# @Software: PyCharm
import abc


class Product:
    def __init__(self):
        self._name = None

    def do_something(self):
        return getattr(self, "_name", "Base")


class AbstractBuilder(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def set_part(self):
        pass

    @abc.abstractmethod
    def build_product(self):
        pass


class ConcreteBuilder(AbstractBuilder):
    def __init__(self):
        self._product = Product()

    def set_part(self):
        setattr(self._product, "_name", "pro_a")

    def build_product(self):
        return self._product


class Director:
    def __init__(self):
        self._builder = ConcreteBuilder()

    def get_product_a(self):
        self._builder.set_part()
        return self._builder.build_product()
