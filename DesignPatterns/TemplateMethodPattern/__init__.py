# -*- coding: utf-8 -*-
# @Time : 2021/2/13 11:05 
# @Author : kimihiro
# @File : __init__.py.py 
# @Software: PyCharm
import abc


class AbstractTemplateClass(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def do_something(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def do_anything(self, *args, **kwargs):
        pass

    def template_method(self):
        self.do_something()
        self.do_anything()

    def i_am_five(self):
        setattr(self, "a", 5)


class ConcreteClassA(AbstractTemplateClass):
    def __init__(self):
        self.a = None
        self.b = None

    def do_something(self, *args, **kwargs):
        self.a = 1

    def do_anything(self, *args, **kwargs):
        self.b = 2


class ConcreteClassB(AbstractTemplateClass):
    def __init__(self):
        self.a = None
        self.b = None

    def do_something(self, *args, **kwargs):
        self.a = 3

    def do_anything(self, *args, **kwargs):
        self.b = 4


class Client:

    def run(self):
        cls_a = ConcreteClassA()
        cls_b = ConcreteClassB()
        cls_a.template_method()
        cls_b.template_method()
        return cls_a, cls_b
