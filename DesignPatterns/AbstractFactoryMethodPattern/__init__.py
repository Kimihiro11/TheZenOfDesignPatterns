# -*- coding: utf-8 -*-
# @Time : 2021/2/11 15:19 
# @Author : kimihiro
# @File : __init__.py.py 
# @Software: PyCharm
import abc


class AbstractProductA(metaclass=abc.ABCMeta):

    def public_method(self):
        pass

    @abc.abstractmethod
    def do_something(self):
        pass


class AbstractProductB(metaclass=abc.ABCMeta):

    def public_method(self):
        pass

    @abc.abstractmethod
    def do_something(self):
        pass


class ProductA(AbstractProductA):
    def do_something(self):
        return "pro A"


class ProductB(AbstractProductB):
    def do_something(self):
        return "pro B"


class AbstractCreator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_product_a(self):
        pass

    @abc.abstractmethod
    def create_product_b(self):
        pass


class Creator(AbstractCreator):
    def create_product_a(self):
        return ProductA()

    def create_product_b(self):
        return ProductB()


class Client:
    @classmethod
    def main(self):
        creator = Creator()
        p_a = creator.create_product_a()
        p_b = creator.create_product_b()
        return [p_a.do_something(), p_b.do_something()]
