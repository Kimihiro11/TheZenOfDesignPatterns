# -*- coding: utf-8 -*-
# @Time : 2021/2/9 21:46 
# @Author : kimihiro
# @File : test_factory_method_pattern.py 
# @Software: PyCharm
from DesignPatterns.FactoryMethodPattern import *


def test_factory_method_pattern():
    client = Client()
    p1 = client.get_product(ConcreteProduct1)
    p2 = client.get_product(ConcreteProduct2)
    assert p1.abs_method() == ConcreteProduct1().abs_method()
    assert p2.abs_method() == ConcreteProduct2().abs_method()
    # base method
    assert p1.pub_method() == ConcreteProduct2().pub_method()
    assert p2.pub_method() == ConcreteProduct1().pub_method()
