# -*- coding: utf-8 -*-
# @Time : 2021/5/4 14:06 
# @Author : kimihiro
# @File : test_chain_of_responsibility_pattern.py 
# @Software: PyCharm
from DesignPatterns.ChainOfResponsibilityPattern import Client


def test_chain_of_responsibility_pattern():
    c=Client()
    r = c.run()
    assert r == "c2 do"