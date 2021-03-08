# -*- coding: utf-8 -*-
# @Time : 2021/2/9 20:35 
# @Author : kimihiro
# @File : __init__.py.py 
# @Software: PyCharm
import abc


# 抽象产品类
class AbstractProduct(metaclass=abc.ABCMeta):
    def __init__(self):
        self.name = "base product"

    def pub_method(self):
        return self.name

    @abc.abstractmethod
    def abs_method(self):
        pass


# 产品类
class ConcreteProduct1(AbstractProduct):

    def abs_method(self):
        return "ConcreteProduct1"


# 产品类
class ConcreteProduct2(AbstractProduct):

    def abs_method(self):
        return "ConcreteProduct2"


# 抽象工厂类
class AbstractCreator(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_product(self, *args, **kwargs):
        pass


# 工厂类
class Creator(AbstractCreator):
    def create_product(self, product):
        return product()


# 客户
class Client:
    def get_product(self, product):
        creator = Creator()
        product = creator.create_product(product)
        return product
