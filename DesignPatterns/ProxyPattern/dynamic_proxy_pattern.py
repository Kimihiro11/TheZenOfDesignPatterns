# -*- coding: utf-8 -*-
# @Time : 2021/3/21 17:20 
# @Author : kimihiro
# @File : dynamic_proxy_pattern.py
# @Software: PyCharm

# python 中的装饰器 可以理解为 在装饰器（方法）中增强被装饰的方法
# class  中的 __call__ 方法 可以让类 能像方法一样被直接调用
# 需要理解 class 中的 __getattr__  方法
"""
class Example:
    pass
ex  =Example()
ex.a
# 这时会 raise AttributeError: 'ex' object has no attribute 'a'
# 赋值
ex.a =1 # 这里就是调用默认的 __setter__
ex.a # 就不会 报错 且 输出 1
"""
import types

"""
# 类装饰器例子
class Wrapper:
    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, attr):
        ret = None  # 可以找不到返回 None，也可以抛出异常。
        if hasattr(self.obj, attr):
            ret = getattr(self.obj, attr)
        return ret

    def __call__(self, *args, **kwargs):
        self.obj = self.obj(*args, **kwargs)
        return self


@Wrapper
class Sample:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def minus(self):
        return self.x - self.y
"""

import abc


# 代理增强
class PrintProxy:
    def __init__(self, obj, method):
        self.obj = obj
        self.method = method

    def __call__(self, *args, **kwargs):
        print('Log: ' + str(self.obj) + ' call ' + self.method.__name__)
        ret = self.method(*args, **kwargs)
        print('Log: ' + str(self.obj) + ' call ' + self.method.__name__ + ' finished')
        return ret


# 动态 proxy
class DynamicProxy:
    def __init__(self, need_proxy_cls, enhance_proxy):
        self.npc = need_proxy_cls
        self.ep = enhance_proxy
        self._lazy_proxy_cache = {}

    def __getattr__(self, attr):
        ret = None  # 可以找不到返回 None，也可以抛出异常。
        if hasattr(self.obj, attr):
            ret = getattr(self.obj, attr)
            if isinstance(ret, types.MethodType):  # 如果该成员是方法
                if ret not in self._lazy_proxy_cache:  # 如果该方法的代理没有被生成
                    self._lazy_proxy_cache[ret] = self.ep(self.obj, ret)  # 创建该方法的代理
                return self._lazy_proxy_cache[ret]
        return ret

    def __call__(self, *args, **kwargs):
        #  初始化 被装饰类 赋值给动态代理类
        self.obj = self.npc(*args, **kwargs)
        return self


# proxy 工厂 装饰器模式
class ProxyFactory:
    def __init__(self, enhance_proxy):
        """
        初始化
        :param enhance_proxy: 增强类
        """
        self.ep = enhance_proxy

    def __call__(self, need_proxy_cls):
        """
        调用
        :param need_proxy_cls: 传入需要 动态代理的 类
        :return:
        """
        return DynamicProxy(need_proxy_cls, self.ep)


class AbstractGamePlayer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def login(self, user: str, password: str):
        pass

    @abc.abstractmethod
    def kill_boss(self):
        pass

    @abc.abstractmethod
    def upgrade(self):
        pass


@ProxyFactory(PrintProxy)
class GamePlayer(AbstractGamePlayer):
    def __init__(self, name):
        self._name = name
        self.level = 0

    def login(self, user: str, password: str):
        return "User {0} login as {1} successful.".format(user, self._name)

    def kill_boss(self):
        return "%s is killing boos" % self._name

    def upgrade(self):
        self.level += 1


class Client:
    def main(self):
        palyer = GamePlayer("J")
        l = palyer.login("J.P", "any")
        print(l)
        k = palyer.kill_boss()
        print(k)
        palyer.upgrade()
        return palyer


if __name__ == '__main__':
    c = Client()
    a = c.main()
    print(a.level)
