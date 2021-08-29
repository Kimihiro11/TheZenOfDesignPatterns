# -*- coding: utf-8 -*-
# @Time : 2021/8/29 15:57 
# @Author : kimihiro
# @File : __init__.py.py 
# @Software: PyCharm
import abc


class AbsStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def do_something(self, *args, **kwargs):
        pass


class ConcreteStrategyOne(AbsStrategy):
    def do_something(self, *args, **kwargs):
        print("strategy one")


class ConcreteStrategyTwo(AbsStrategy):
    def do_something(self, *args, **kwargs):
        print("strategy two")


class Context:
    def __init__(self, strategy: AbsStrategy):
        self._stragegy = strategy

    def do_anything(self, *args, **kwargs):
        self._stragegy.do_something(*args, **kwargs)


class Client:
    def main(self):
        strategy = ConcreteStrategyOne()
        context = Context(strategy)
        context.do_anything()
