# -*- coding: utf-8 -*-
# @Time : 2021/4/17 14:32 
# @Author : kimihiro
# @File : __init__.py.py 
# @Software: PyCharm
import copy


class PrototypeClass:
    def __init__(self):
        self._array = []
        print("init")

    def get_a(self):
        return self._array

    def set_a(self, val):
        self._array.append(val)

    def clone(self):
        return copy.copy(self)

    def deep_clone(self):
        return copy.deepcopy(self)


class Client:
    @staticmethod
    def main():
        a = PrototypeClass()
        b = a.clone()
        c = a.deep_clone()
        print(a.get_a())
        print(b.get_a())
        print(c.get_a())
        a.set_a(3)
        print(a.get_a())
        print(b.get_a())
        print(c.get_a())
        b.set_a(4)
        print(a.get_a())
        print(b.get_a())
        print(c.get_a())
        c.set_a(5)
        print(a.get_a())
        print(b.get_a())
        print(c.get_a())
        return a.get_a(), b.get_a(), c.get_a()
