# -*- coding: utf-8 -*-
# @Time : 2021/5/4 12:59 
# @Author : kimihiro
# @File : __init__.py.py 
# @Software: PyCharm
import abc


class AbsRequest(metaclass=abc.ABCMeta):
    def __init__(self, level):
        self.level = level


class AbsHandler(metaclass=abc.ABCMeta):

    def __init__(self, level):
        self._next_handler = None
        self.__level = level

    def set_next(self, handler):
        setattr(self, "_next_handler", handler)

    def handler_message(self, request: AbsRequest):
        response = None
        if self.__level == request.level:
            response = self.echo(request)
        else:
            if self._next_handler is None:
                pass
            else:
                response = self._next_handler.handler_message(request)
        return response

    @abc.abstractmethod
    def echo(self, request: AbsRequest):
        pass


class ConcreteHandler1(AbsHandler):
    def echo(self, request: AbsRequest):
        return "c1 do"


class ConcreteHandler2(AbsHandler):
    def echo(self, request: AbsRequest):
        return "c2 do"


class Request(AbsRequest):
    pass


class Client:
    def run(self):
        req = Request(2)
        c1 = ConcreteHandler1(1)
        c2 = ConcreteHandler2(2)
        c1.set_next(c2)
        response = c1.handler_message(req)
        return response



