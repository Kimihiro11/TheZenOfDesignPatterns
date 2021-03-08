# -*- coding: utf-8 -*-
# @Time : 2021/2/7 16:01 
# @Author : kimihiro
# @File : __init__.py.py 
# @Software: PyCharm
import threading


class Singleton(object):
    """
    单例模式 类的实现形式
    """
    # 确保线程安全
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        # __new__ 不重写时 做的事情
        # return super().__new__(cls, *args, **kwargs)
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = super().__new__(cls)
        return Singleton._instance


def singleton_decorator(cls):
    _instance = {}
    lock = threading.Lock()

    def _singleton(*arg, **kwargs):
        if not _instance.get(cls):
            with lock:
                if not _instance.get(cls):
                    _instance[cls] = cls(*arg, **kwargs)
        return _instance[cls]

    return _singleton
