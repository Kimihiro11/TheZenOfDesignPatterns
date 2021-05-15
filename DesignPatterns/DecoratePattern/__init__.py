# -*- coding: utf-8 -*-
# @Time : 2021/5/15 13:31 
# @Author : kimihiro
# @File : __init__.py.py 
# @Software: PyCharm
import abc


class Component(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def operate(self):
        pass


class ConcreteComponent(Component):

    def operate(self):
        return 1


class Decorator(Component):

    def __init__(self, component: Component):
        self._com = component

    def operate(self):
        self._com.operate()


class ConcreteDecorator(Decorator):

    @classmethod
    def do_other_things(cls):
        return 2

    def operate(self):
        self.do_other_things()
        super(ConcreteDecorator, self).operate()


class Client:
    def run(self):
        c = ConcreteDecorator(ConcreteComponent())
        c.operate()
