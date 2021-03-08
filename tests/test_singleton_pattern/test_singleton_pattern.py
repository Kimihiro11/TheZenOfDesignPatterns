# -*- coding: utf-8 -*-
# @Time : 2021/2/7 16:05 
# @Author : kimihiro
# @File : test_singleton_pattern.py 
# @Software: PyCharm
import threading

from DesignPatterns.SingletonPattern import singleton_decorator, Singleton


def test_singleton_decorator():
    @singleton_decorator
    class A:
        pass

    a1 = A()
    a2 = A()
    assert a1 == a2
    t_objs = []

    # 多线程测试
    def task(arg):
        obj = A()
        t_objs.append(obj)

    for i in range(10):
        t = threading.Thread(target=task, args=[i, ])
        t.start()

    for i in t_objs:
        assert i == a1


def test_singleton_class():
    obj1 = Singleton()
    obj2 = Singleton()
    assert obj1 == obj2

    t_objs = []

    # 多线程测试
    def task(arg):
        obj = Singleton()
        t_objs.append(obj)

    for i in range(10):
        t = threading.Thread(target=task, args=[i, ])
        t.start()

    for i in t_objs:
        assert i == obj1
