# -*- coding: utf-8 -*-
# @Time : 2021/5/3 10:52 
# @Author : kimihiro
# @File : __init__.py.py 
# @Software: PyCharm
import abc


class AbsReceiver(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def do(self):
        pass


class ConcreteReceiver(AbsReceiver):
    def do(self):
        pass


class AbsCommand(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self):
        pass


class ConcreteCommand(AbsCommand):
    def __init__(self, receiver: AbsReceiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.do()


class Invoker:
    def __init__(self, command: AbsCommand):
        self._command = command

    def action(self):
        self._command.execute()


class Client:
    def run(self):
        rev = ConcreteReceiver()
        cmd = ConcreteCommand(rev)
        inv = Invoker(cmd)
        inv.action()
