# -*- coding: utf-8 -*-
# @Time : 2021/4/17 15:30 
# @Author : kimihiro
# @File : test_prototype_pattern.py 
# @Software: PyCharm

from DesignPatterns.PrototypePattern import Client


def test_prototype_pattern():
    a, b, c = Client.main()
    assert a == [3, 4]
    assert b == [3, 4]
    assert c == [5]
