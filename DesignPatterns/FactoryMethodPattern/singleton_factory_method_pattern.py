# -*- coding: utf-8 -*-
# @Time : 2021/2/11 14:11 
# @Author : kimihiro
# @File : singleton_factory_method_pattern.py 
# @Software: PyCharm

from DesignPatterns.SingletonPattern import Singleton


class SingletonFactory:
    def __init__(self):
        self._cls = {}

    def create_singleton_cls(self, cls_name: str, cls_func: dict):
        """
        摘要:
        延迟加载框架时可以扩展的，例如限制某一个产品类的最大实例化数量
        还可以用在对象初始化比较复杂的情况下，例如硬件访问，涉及多方面的交互，则可以通过延迟加载降低对象的产生和销毁带来的复杂性

        """
        # 懒加载的一种形式
        if self._cls.get(cls_name):
            new_cls = self._cls[cls_name]
        else:
            # type('叫什么类','继承谁','里面有什么方法')
            new_cls = type(cls_name, (Singleton,), cls_func)
            self._cls.update({cls_name: new_cls})
        return new_cls


class Client:
    def __init__(self):
        self.singleton_factory = SingletonFactory()

    def get_singleton_cls(self, name: str, cls_func: dict):
        new_cls = self.singleton_factory.create_singleton_cls(name, cls_func)
        return new_cls

